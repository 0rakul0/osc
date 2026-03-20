from __future__ import annotations

from io import BytesIO
import math
import re
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DATA_DIR = BASE_DIR / "processada"
HISTORY_DIR = BASE_DIR / "historia"
STANDARD_COLUMNS = [
    "uf",
    "ano",
    "valor_total",
    "cnpj",
    "nome_osc",
    "mes",
    "cod_municipio",
    "municipio",
    "objeto",
    "modalidade",
    "data_inicio",
    "data_fim",
]
NULL_TOKENS = {"", "nan", "none", "null", "nat", "<na>"}
QUALITY_COLUMNS = [
    "cnpj",
    "nome_osc",
    "mes",
    "cod_municipio",
    "municipio",
    "objeto",
    "modalidade",
    "data_inicio",
    "data_fim",
]
STOPWORDS = {
    "a", "ao", "aos", "as", "com", "da", "das", "de", "do", "dos", "e", "em",
    "na", "nas", "no", "nos", "o", "os", "ou", "para", "por", "que", "se",
    "sem", "sob", "sobre", "um", "uma", "uns", "umas", "pela", "pelas",
    "pelo", "pelos", "referente", "objeto", "convenio", "execucao", "servicos",
    "servico", "projeto", "apoio", "estado", "municipio", "municipal", "estadual",
}


def format_int(value: float | int | None) -> str:
    if value is None or pd.isna(value):
        return "0"
    return f"{int(round(float(value))):,}".replace(",", ".")


def format_pct(value: float | None) -> str:
    if value is None or pd.isna(value):
        return "0,0%"
    return f"{float(value):.1f}%".replace(".", ",")


def format_money(value: float | None) -> str:
    if value is None or pd.isna(value):
        return "R$ 0,00"
    text = f"{float(value):,.2f}"
    return f"R$ {text.replace(',', 'X').replace('.', ',').replace('X', '.')}"


def clean_text(series: pd.Series) -> pd.Series:
    values = series.astype("string").str.strip()
    lower = values.str.lower()
    values = values.mask(lower.isin(NULL_TOKENS))
    values = values.mask(values.isin(["-", "--"]))
    return values


def parse_money(value: object) -> float:
    if pd.isna(value):
        return np.nan
    text = str(value).strip()
    if not text or text.lower() in NULL_TOKENS:
        return np.nan
    compact = text.replace("\xa0", "").replace(" ", "").removeprefix("R$")
    if compact.startswith("(") and compact.endswith(")"):
        compact = f"-{compact[1:-1]}"
    if "," in compact and "." in compact:
        if compact.rfind(",") > compact.rfind("."):
            compact = compact.replace(".", "").replace(",", ".")
        else:
            compact = compact.replace(",", "")
    elif "," in compact:
        compact = compact.replace(".", "").replace(",", ".")
    elif compact.count(".") > 1:
        compact = compact.replace(".", "")
    compact = re.sub(r"[^0-9.+\-eE]", "", compact)
    if not compact:
        return np.nan
    try:
        return float(compact)
    except ValueError:
        return np.nan


def parse_int_like(series: pd.Series) -> pd.Series:
    cleaned = clean_text(series).str.replace(r"\.0+$", "", regex=True)
    return pd.to_numeric(cleaned, errors="coerce").astype("Float64")


def parse_dates(series: pd.Series) -> pd.Series:
    cleaned = clean_text(series)
    parsed = pd.to_datetime(cleaned, errors="coerce", format="mixed", dayfirst=True)
    retry = parsed.isna() & cleaned.notna()
    if retry.any():
        parsed.loc[retry] = pd.to_datetime(cleaned.loc[retry], errors="coerce", format="mixed", dayfirst=False)
    return parsed


def ensure_schema(frame: pd.DataFrame) -> pd.DataFrame:
    for column in STANDARD_COLUMNS:
        if column not in frame.columns:
            frame[column] = pd.NA
    return frame[STANDARD_COLUMNS].copy()


@st.cache_data(show_spinner="Lendo os parquets...")
def load_data(data_dir: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    parquet_paths = sorted(Path(data_dir).glob("*.parquet"))
    if not parquet_paths:
        return pd.DataFrame(columns=STANDARD_COLUMNS), pd.DataFrame()

    frames: list[pd.DataFrame] = []
    file_rows: list[dict[str, object]] = []
    for path in parquet_paths:
        frame = ensure_schema(pd.read_parquet(path))
        frame["arquivo_origem"] = path.name
        frame["uf_arquivo"] = path.stem.upper()
        frames.append(frame)
        file_rows.append(
            {
                "arquivo": path.name,
                "uf": path.stem.upper(),
                "linhas": len(frame),
                "tamanho_mb": round(path.stat().st_size / (1024 * 1024), 2),
                "atualizado_em": pd.Timestamp(path.stat().st_mtime, unit="s"),
            }
        )

    data = pd.concat(frames, ignore_index=True)
    for column in STANDARD_COLUMNS:
        data[column] = clean_text(data[column])

    data["valor_num"] = data["valor_total"].map(parse_money)
    data["ano_num"] = parse_int_like(data["ano"])
    data["mes_num"] = parse_int_like(data["mes"])
    data["data_inicio_dt"] = parse_dates(data["data_inicio"])
    data["data_fim_dt"] = parse_dates(data["data_fim"])
    data["duracao_dias"] = (data["data_fim_dt"] - data["data_inicio_dt"]).dt.days.astype("Float64")

    current_year = pd.Timestamp.today().year
    data["tem_cnpj_valido"] = data["cnpj"].str.replace(r"\D", "", regex=True).str.len().eq(14)
    data["tem_municipio"] = data["municipio"].notna()
    data["tem_objeto"] = data["objeto"].notna()
    data["tem_modalidade"] = data["modalidade"].notna()
    data["valor_zero"] = data["valor_num"].fillna(0).eq(0)
    data["valor_negativo"] = data["valor_num"].lt(0).fillna(False)
    data["ano_valido"] = data["ano_num"].between(1990, current_year + 2)
    data["mes_valido"] = data["mes_num"].between(1, 12)
    data["entidade_base"] = data["cnpj"].where(data["tem_cnpj_valido"], data["nome_osc"]).fillna("Sem identificacao")
    data["municipio_base"] = data["municipio"].fillna("Nao informado")
    data["modalidade_base"] = data["modalidade"].fillna("Nao informada")

    valid_period = data["ano_valido"] & data["mes_valido"]
    data["ano_mes"] = pd.NaT
    if valid_period.any():
        data.loc[valid_period, "ano_mes"] = pd.to_datetime(
            {
                "year": data.loc[valid_period, "ano_num"].astype(int),
                "month": data.loc[valid_period, "mes_num"].astype(int),
                "day": 1,
            },
            errors="coerce",
        )

    dup_cols = ["uf", "ano", "mes", "valor_total", "cnpj", "nome_osc", "municipio", "objeto", "modalidade"]
    data["duplicado_aparente"] = data[dup_cols].fillna("<vazio>").duplicated(keep=False)

    files_df = pd.DataFrame(file_rows).sort_values(["linhas", "arquivo"], ascending=[False, True]).reset_index(drop=True)
    return data, files_df


@st.cache_data(show_spinner=False)
def load_history_documents(history_dir: str) -> dict[str, str]:
    base = Path(history_dir)
    if not base.exists():
        return {}
    docs: dict[str, str] = {}
    for path in sorted(base.glob("*.md")):
        docs[path.stem.upper()] = path.read_text(encoding="utf-8")
    return docs


def history_anchor_id(markdown_text: str, fallback_key: str) -> str:
    first_line = next((line.strip() for line in markdown_text.splitlines() if line.strip().startswith("#")), fallback_key)
    title = re.sub(r"^#+\s*", "", first_line).strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", title).strip("-")
    return slug or fallback_key.lower()


def split_history_markdown(markdown_text: str, fallback_key: str) -> tuple[str, str]:
    lines = markdown_text.splitlines()
    title_line = next((line for line in lines if line.strip().startswith("#")), f"# {fallback_key}")
    title = re.sub(r"^#+\s*", "", title_line).strip()
    title_index = lines.index(title_line) if title_line in lines else 0
    body = "\n".join(lines[title_index + 1:]).strip()
    return title, body


def history_display_label(markdown_text: str, fallback_key: str) -> str:
    title, _ = split_history_markdown(markdown_text, fallback_key)
    match = re.match(r"^(.*?)\s*\(([A-Z]{2})\)\s*$", title)
    if match:
        state_name = match.group(1).strip()
        uf = match.group(2).strip()
        return f"{uf} - {state_name}"
    return fallback_key


def apply_filters(
    data: pd.DataFrame,
    selected_ufs: list[str],
    year_range: tuple[int, int] | None,
    selected_months: list[int],
    selected_modalities: list[str],
    minimum_value: float,
    only_valid_cnpj: bool,
    exclude_zero_negative: bool,
    search_text: str,
) -> pd.DataFrame:
    filtered = data.copy()
    if selected_ufs:
        filtered = filtered[filtered["uf"].isin(selected_ufs)]
    if year_range:
        filtered = filtered[filtered["ano_num"].between(year_range[0], year_range[1], inclusive="both")]
    if selected_months:
        filtered = filtered[filtered["mes_num"].isin(selected_months)]
    if selected_modalities:
        filtered = filtered[filtered["modalidade_base"].isin(selected_modalities)]
    if minimum_value > 0:
        filtered = filtered[filtered["valor_num"].ge(minimum_value)]
    if only_valid_cnpj:
        filtered = filtered[filtered["tem_cnpj_valido"]]
    if exclude_zero_negative:
        filtered = filtered[filtered["valor_num"].gt(0)]
    if search_text:
        mask = (
            filtered["nome_osc"].fillna("").str.contains(search_text, case=False, regex=False)
            | filtered["objeto"].fillna("").str.contains(search_text, case=False, regex=False)
            | filtered["municipio"].fillna("").str.contains(search_text, case=False, regex=False)
            | filtered["cnpj"].fillna("").str.contains(search_text, case=False, regex=False)
        )
        filtered = filtered[mask]
    return filtered.reset_index(drop=True)


def build_uf_summary(filtered: pd.DataFrame) -> pd.DataFrame:
    if filtered.empty:
        return pd.DataFrame()
    grouped = (
        filtered.groupby("uf", dropna=False)
        .agg(
            registros=("uf", "size"),
            valor_total=("valor_num", "sum"),
            ticket_medio=("valor_num", "mean"),
            ticket_mediano=("valor_num", "median"),
            entidades=("nome_osc", lambda values: values.dropna().nunique()),
            cnpjs=("cnpj", lambda values: values.dropna().nunique()),
            municipios=("municipio", lambda values: values.dropna().nunique()),
            cobertura_cnpj=("tem_cnpj_valido", "mean"),
            cobertura_municipio=("tem_municipio", "mean"),
            cobertura_objeto=("tem_objeto", "mean"),
            cobertura_modalidade=("tem_modalidade", "mean"),
        )
        .reset_index()
    )
    for column in ["cobertura_cnpj", "cobertura_municipio", "cobertura_objeto", "cobertura_modalidade"]:
        grouped[column] = grouped[column] * 100
    return grouped.sort_values(["valor_total", "registros"], ascending=[False, False]).reset_index(drop=True)


def build_entity_summary(filtered: pd.DataFrame) -> pd.DataFrame:
    if filtered.empty:
        return pd.DataFrame()
    entities = (
        filtered.groupby("entidade_base", dropna=False)
        .agg(
            nome_osc=("nome_osc", lambda values: values.dropna().mode().iat[0] if not values.dropna().empty else "Sem nome"),
            cnpj=("cnpj", lambda values: values.dropna().iat[0] if not values.dropna().empty else pd.NA),
            registros=("entidade_base", "size"),
            valor_total=("valor_num", "sum"),
            ticket_medio=("valor_num", "mean"),
            ufs=("uf", lambda values: values.dropna().nunique()),
            municipios=("municipio", lambda values: values.dropna().nunique()),
            primeiro_ano=("ano_num", "min"),
            ultimo_ano=("ano_num", "max"),
        )
        .reset_index()
    )
    entities["identificador"] = entities["cnpj"].fillna(entities["nome_osc"])
    return entities.sort_values(["valor_total", "registros"], ascending=[False, False]).reset_index(drop=True)


def build_state_benchmark(data: pd.DataFrame) -> pd.DataFrame:
    if data.empty:
        return pd.DataFrame()
    rows: list[dict[str, object]] = []
    for uf, frame in data.groupby("uf", dropna=False):
        entity_values = frame.groupby("nome_osc", dropna=False)["valor_num"].sum().sort_values(ascending=False)
        total = float(frame["valor_num"].sum())
        rows.append(
            {
                "uf": uf,
                "registros": len(frame),
                "valor_total": total,
                "ticket_medio": float(frame["valor_num"].mean()),
                "ticket_mediano": float(frame["valor_num"].median()),
                "entidades": int(frame["nome_osc"].dropna().nunique()),
                "cnpjs": int(frame.loc[frame["tem_cnpj_valido"], "cnpj"].dropna().nunique()),
                "cob_municipio": float(frame["tem_municipio"].mean() * 100),
                "cob_objeto": float(frame["tem_objeto"].mean() * 100),
                "cob_modalidade": float(frame["tem_modalidade"].mean() * 100),
                "top1_share_pct": float(entity_values.head(1).sum() / total * 100) if total else 0.0,
                "top5_share_pct": float(entity_values.head(5).sum() / total * 100) if total else 0.0,
                "top10_share_pct": float(entity_values.head(10).sum() / total * 100) if total else 0.0,
            }
        )
    benchmark = pd.DataFrame(rows)
    national_total = benchmark["valor_total"].sum()
    benchmark["share_nacional_pct"] = benchmark["valor_total"] / national_total * 100
    benchmark["rank_valor_total"] = benchmark["valor_total"].rank(method="min", ascending=False).astype(int)
    benchmark["rank_registros"] = benchmark["registros"].rank(method="min", ascending=False).astype(int)
    benchmark["rank_ticket_medio"] = benchmark["ticket_medio"].rank(method="min", ascending=False).astype(int)
    benchmark["rank_concentracao"] = benchmark["top5_share_pct"].rank(method="min", ascending=False).astype(int)
    return benchmark.sort_values("valor_total", ascending=False).reset_index(drop=True)


def build_word_frequency(series: pd.Series, top_n: int = 20) -> pd.DataFrame:
    tokens = (
        series.dropna()
        .astype("string")
        .str.upper()
        .str.replace(r"[^A-Z0-9À-Ú]+", " ", regex=True)
        .str.split()
        .explode()
    )
    if tokens.empty:
        return pd.DataFrame(columns=["termo", "frequencia"])
    tokens = tokens[tokens.notna()]
    tokens = tokens[tokens.str.len().ge(4)]
    tokens = tokens[~tokens.str.lower().isin(STOPWORDS)]
    freq = tokens.value_counts().head(top_n)
    return freq.rename_axis("termo").reset_index(name="frequencia")


def build_benchmark_export_frames(filtered: pd.DataFrame, full_data: pd.DataFrame) -> dict[str, pd.DataFrame]:
    benchmark_full = build_state_benchmark(full_data)
    benchmark_current = build_state_benchmark(filtered)
    uf_summary = build_uf_summary(filtered)
    top_entities = build_entity_summary(filtered).head(200)
    narrativa = build_executive_narrative_rows(filtered, full_data)

    annual = (
        filtered.loc[filtered["ano_valido"]]
        .groupby(["uf", "ano_num"])
        .agg(registros=("uf", "size"), valor_total=("valor_num", "sum"), ticket_medio=("valor_num", "mean"))
        .reset_index()
        .rename(columns={"ano_num": "ano"})
    )

    quality = (
        filtered.groupby("uf")[QUALITY_COLUMNS]
        .apply(lambda frame: frame.isna().mean() * 100)
        .reset_index()
        .melt(id_vars="uf", var_name="campo", value_name="faltante_pct")
    )

    return {
        "resumo_executivo": narrativa,
        "benchmark_atual": benchmark_current,
        "benchmark_nacional": benchmark_full,
        "resumo_uf": uf_summary,
        "top_entidades": top_entities,
        "serie_anual": annual,
        "qualidade": quality,
    }


def dataframe_to_excel_bytes(frames: dict[str, pd.DataFrame]) -> bytes:
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        for sheet_name, frame in frames.items():
            safe_name = re.sub(r"[^A-Za-z0-9_]", "_", sheet_name)[:31]
            frame.to_excel(writer, sheet_name=safe_name, index=False)
    output.seek(0)
    return output.getvalue()


def classify_state_driver(row: pd.Series, benchmark: pd.DataFrame) -> str:
    high_rows = row["registros"] >= benchmark["registros"].quantile(0.75)
    high_ticket = row["ticket_medio"] >= benchmark["ticket_medio"].quantile(0.75)
    high_concentration = row["top5_share_pct"] >= benchmark["top5_share_pct"].quantile(0.75)
    if high_rows and high_ticket:
        return "volume e ticket"
    if high_rows and not high_ticket:
        return "volume"
    if high_ticket and high_concentration:
        return "ticket e concentracao"
    if high_ticket:
        return "ticket medio"
    if high_concentration:
        return "concentracao"
    return "base mais distribuida"


def build_state_narrative(uf: str, benchmark: pd.DataFrame) -> str:
    row = benchmark.loc[benchmark["uf"] == uf]
    if row.empty:
        return f"`{uf}` nao esta presente no conjunto atual."
    row = row.iloc[0]
    driver = classify_state_driver(row, benchmark)
    return (
        f"`{uf}` tem `rank {int(row['rank_valor_total'])}` em valor total, `rank {int(row['rank_registros'])}` em volume de registros, "
        f"`rank {int(row['rank_ticket_medio'])}` em ticket medio e `rank {int(row['rank_concentracao'])}` em concentracao dos 5 maiores. "
        f"O perfil dominante dessa UF e `{driver}`. "
        f"Ela soma {format_money(row['valor_total'])}, com {format_int(row['registros'])} registros, "
        f"ticket medio de {format_money(row['ticket_medio'])} e concentracao top 5 de {format_pct(row['top5_share_pct'])}."
    )


def render_benchmark_narratives(benchmark: pd.DataFrame) -> None:
    top_value = benchmark.sort_values("valor_total", ascending=False).head(5)["uf"].tolist()
    top_rows = benchmark.sort_values("registros", ascending=False).head(5)["uf"].tolist()
    top_ticket = benchmark.sort_values("ticket_medio", ascending=False).head(5)["uf"].tolist()
    top_concentration = benchmark.sort_values("top5_share_pct", ascending=False).head(5)["uf"].tolist()

    st.markdown("**Leitura guiada**")
    st.write(
        f"No conjunto nacional, as UFs que mais pesam em valor sao `{', '.join(top_value[:5])}`; em quantidade de linhas, `{', '.join(top_rows[:5])}`; "
        f"em ticket medio, `{', '.join(top_ticket[:5])}`; e em concentracao dos 5 maiores beneficiarios, `{', '.join(top_concentration[:5])}`."
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(
            "**Por que SP destoa?**\n\n"
            + build_state_narrative("SP", benchmark)
            + "\n\nLeitura: SP e grande porque combina base volumosa com ticket ainda alto, alem de ter estrutura mais diversificada do que estados muito concentrados."
        )
    with col2:
        st.warning(
            "**Por que AM destoa?**\n\n"
            + build_state_narrative("AM", benchmark)
            + "\n\nLeitura: AM sobe no ranking menos por quantidade de linhas e mais por contratos muito grandes concentrados em poucas entidades."
        )
    with col3:
        median_rows = benchmark["registros"].median()
        median_ticket = benchmark["ticket_medio"].median()
        st.success(
            "**Padrao geral das UFs**\n\n"
            f"A mediana do conjunto e de {format_int(median_rows)} registros por UF e ticket medio de {format_money(median_ticket)}. "
            "Estados acima da mediana de registros tendem a crescer por massa de dados; estados acima da mediana de ticket tendem a crescer por contratos maiores. "
            "Quando a concentracao top 5 sobe muito, poucos beneficiarios passam a explicar boa parte do valor total."
        )


def build_executive_narrative_rows(filtered: pd.DataFrame, full_data: pd.DataFrame) -> pd.DataFrame:
    benchmark_full = build_state_benchmark(full_data)
    benchmark_current = build_state_benchmark(filtered)
    reference = benchmark_current if not benchmark_current.empty else benchmark_full

    top_value = benchmark_full.sort_values("valor_total", ascending=False).head(5)["uf"].tolist()
    top_rows = benchmark_full.sort_values("registros", ascending=False).head(5)["uf"].tolist()
    top_ticket = benchmark_full.sort_values("ticket_medio", ascending=False).head(5)["uf"].tolist()
    top_concentration = benchmark_full.sort_values("top5_share_pct", ascending=False).head(5)["uf"].tolist()

    rows = [
        {
            "secao": "Resumo executivo",
            "texto": (
                f"O recorte atual contem {format_int(len(filtered))} registros e {format_money(filtered['valor_num'].sum())} em valor total. "
                f"No conjunto nacional, as maiores UFs por valor sao {', '.join(top_value[:5])}; por quantidade de registros, {', '.join(top_rows[:5])}; "
                f"por ticket medio, {', '.join(top_ticket[:5])}; e por concentracao dos 5 maiores beneficiarios, {', '.join(top_concentration[:5])}."
            ),
        },
        {
            "secao": "Por que SP destoa?",
            "texto": build_state_narrative("SP", benchmark_full)
            + " Leitura executiva: SP se destaca principalmente por volume de base combinado com ticket relevante, formando um total muito alto sem depender tanto de poucos beneficiarios.",
        },
        {
            "secao": "Por que AM destoa?",
            "texto": build_state_narrative("AM", benchmark_full)
            + " Leitura executiva: AM se destaca menos por quantidade e mais por contratos muito grandes concentrados em poucas entidades.",
        },
        {
            "secao": "Padrao geral",
            "texto": (
                f"No recorte atual, a mediana entre as UFs e de {format_int(reference['registros'].median())} registros e ticket medio de {format_money(reference['ticket_medio'].median())}. "
                "Isso ajuda a separar estados puxados por massa de dados daqueles puxados por ticket medio alto ou forte concentracao."
            ),
        },
    ]
    return pd.DataFrame(rows)


def render_header(data: pd.DataFrame, files_df: pd.DataFrame, data_dir: str) -> None:
    last_update = files_df["atualizado_em"].max() if not files_df.empty else None
    updated_text = last_update.strftime("%d/%m/%Y %H:%M") if pd.notna(last_update) else "n/d"
    st.markdown(
        """
        <style>
        .hero {padding: 1.1rem 1.3rem; border-radius: 18px; color: white;
        background: linear-gradient(135deg, rgba(15,76,92,0.95), rgba(227,100,20,0.90));
        box-shadow: 0 18px 40px rgba(15,76,92,0.18); margin-bottom: 1rem;}
        .hero h1 {margin: 0; font-size: 2rem;}
        .hero p {margin: .35rem 0 0; opacity: .95;}
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="hero">
            <h1>Dashboard Analitico dos Parquets</h1>
            <p>Leitura de <strong>{data_dir}</strong> com {format_int(len(data))} registros, valor agregado de <strong>{format_money(data['valor_num'].sum())}</strong> e ultima atualizacao em <strong>{updated_text}</strong>.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar(data: pd.DataFrame, files_df: pd.DataFrame) -> tuple[list[str], tuple[int, int] | None, list[int], list[str], float, bool, bool, str]:
    st.sidebar.header("Filtros")
    available_ufs = sorted(data["uf"].dropna().unique().tolist())
    selected_ufs = st.sidebar.multiselect("UFs", available_ufs, default=available_ufs)
    valid_years = sorted(int(v) for v in data.loc[data["ano_valido"], "ano_num"].dropna().unique().tolist())
    year_range = None
    if valid_years:
        year_range = st.sidebar.slider("Faixa de ano", min(valid_years), max(valid_years), (min(valid_years), max(valid_years)))
    valid_months = sorted(int(v) for v in data.loc[data["mes_valido"], "mes_num"].dropna().unique().tolist())
    selected_months = st.sidebar.multiselect("Meses", valid_months, default=valid_months)
    modalities = data["modalidade_base"].value_counts().head(25).index.tolist()
    selected_modalities = st.sidebar.multiselect("Modalidades", modalities, default=[])
    minimum_value = st.sidebar.number_input("Valor minimo", min_value=0.0, value=0.0, step=50000.0)
    only_valid_cnpj = st.sidebar.checkbox("Somente CNPJ valido", value=False)
    exclude_zero_negative = st.sidebar.checkbox("Excluir zero e negativos", value=False)
    search_text = st.sidebar.text_input("Busca textual")
    st.sidebar.divider()
    st.sidebar.caption(f"Arquivos lidos: {format_int(len(files_df))}")
    return selected_ufs, year_range, selected_months, selected_modalities, minimum_value, only_valid_cnpj, exclude_zero_negative, search_text


def render_overview(filtered: pd.DataFrame, full_data: pd.DataFrame) -> None:
    st.subheader("Panorama")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Registros", format_int(len(filtered)))
    col2.metric("Valor total", format_money(filtered["valor_num"].sum()))
    col3.metric("Ticket medio", format_money(filtered["valor_num"].mean()))
    col4.metric("Mediana", format_money(filtered["valor_num"].median()))
    col5.metric("Entidades", format_int(filtered["nome_osc"].dropna().nunique()))
    col6.metric("CNPJs validos", format_int(filtered.loc[filtered["tem_cnpj_valido"], "cnpj"].dropna().nunique()))

    summary = build_uf_summary(filtered)
    left, right = st.columns([1.2, 0.8])
    with left:
        fig = px.bar(
            summary.sort_values("valor_total").tail(15),
            x="valor_total",
            y="uf",
            orientation="h",
            title="Valor total por UF",
            color="valor_total",
            color_continuous_scale=["#d8f3dc", "#0f4c5c"],
        )
        fig.update_layout(height=440, margin=dict(l=10, r=10, t=60, b=10), coloraxis_showscale=False)
        st.plotly_chart(fig, width='stretch')
    with right:
        positive = filtered.loc[filtered["valor_num"].gt(0), "valor_num"].dropna()
        if positive.empty:
            st.info("Sem valores positivos para distribuicao.")
        else:
            hist = pd.DataFrame({"log10_valor": np.log10(positive.clip(lower=1))})
            fig = px.histogram(hist, x="log10_valor", nbins=40, title="Distribuicao dos valores (log10)", color_discrete_sequence=["#e36414"])
            fig.update_layout(height=440, margin=dict(l=10, r=10, t=60, b=10))
            st.plotly_chart(fig, width='stretch')

    display = summary.copy()
    for column in ["valor_total", "ticket_medio", "ticket_mediano"]:
        display[column] = display[column].map(format_money)
    for column in ["cobertura_cnpj", "cobertura_municipio", "cobertura_objeto", "cobertura_modalidade"]:
        display[column] = display[column].map(format_pct)
    st.dataframe(display, width='stretch', hide_index=True)
    st.caption(f"O recorte atual representa {format_pct(len(filtered) / max(len(full_data), 1) * 100)} da base carregada.")


def render_temporal(filtered: pd.DataFrame) -> None:
    st.subheader("Temporal")
    annual = (
        filtered.loc[filtered["ano_valido"]]
        .groupby("ano_num")
        .agg(valor_total=("valor_num", "sum"), registros=("ano_num", "size"), ticket_medio=("valor_num", "mean"))
        .reset_index()
    )
    if annual.empty:
        st.info("Nao ha anos validos no recorte.")
        return
    metric = st.radio("Metrica", ["Valor total", "Registros", "Ticket medio"], horizontal=True)
    y_map = {"Valor total": "valor_total", "Registros": "registros", "Ticket medio": "ticket_medio"}
    left, right = st.columns([1.1, 0.9])
    with left:
        fig = px.line(annual, x="ano_num", y=y_map[metric], markers=True, title=f"Evolucao anual - {metric.lower()}", color_discrete_sequence=["#0f4c5c"])
        fig.update_layout(height=400, margin=dict(l=10, r=10, t=60, b=10))
        st.plotly_chart(fig, width='stretch')
    with right:
        by_uf_year = filtered.loc[filtered["ano_valido"]].groupby(["uf", "ano_num"])["valor_num"].sum().reset_index()
        if by_uf_year.empty:
            st.info("Sem combinacoes de UF e ano.")
        else:
            heat = by_uf_year.pivot(index="uf", columns="ano_num", values="valor_num")
            fig = px.imshow(heat, aspect="auto", color_continuous_scale=["#fff4e6", "#fb8b24", "#9a031e"], title="Heatmap de valor por UF e ano")
            fig.update_layout(height=400, margin=dict(l=10, r=10, t=60, b=10))
            st.plotly_chart(fig, width='stretch')


def render_territory(filtered: pd.DataFrame) -> None:
    st.subheader("Territorio")
    geo = (
        filtered.groupby(["uf", "municipio_base"], dropna=False)
        .agg(registros=("municipio_base", "size"), valor_total=("valor_num", "sum"))
        .reset_index()
        .sort_values(["valor_total", "registros"], ascending=[False, False])
    )
    left, right = st.columns([1.1, 0.9])
    with left:
        fig = px.bar(geo.head(25).sort_values("valor_total"), x="valor_total", y="municipio_base", orientation="h", color="uf", title="Top municipios por valor")
        fig.update_layout(height=520, margin=dict(l=10, r=10, t=60, b=10))
        st.plotly_chart(fig, width='stretch')
    with right:
        fig = px.treemap(geo.head(120), path=["uf", "municipio_base"], values="valor_total", color="registros", title="Treemap territorial")
        fig.update_layout(height=520, margin=dict(l=10, r=10, t=60, b=10))
        st.plotly_chart(fig, width='stretch')


def render_entities(filtered: pd.DataFrame) -> None:
    st.subheader("Entidades")
    entities = build_entity_summary(filtered)
    if entities.empty:
        st.info("Sem entidades para o recorte.")
        return
    left, right = st.columns(2)
    with left:
        fig = px.bar(entities.head(20).sort_values("valor_total"), x="valor_total", y="identificador", orientation="h", title="Top entidades por valor", color="valor_total", color_continuous_scale=["#ffd6a5", "#9a031e"])
        fig.update_layout(height=520, margin=dict(l=10, r=10, t=60, b=10), coloraxis_showscale=False)
        st.plotly_chart(fig, width='stretch')
    with right:
        top_rows = entities.sort_values(["registros", "valor_total"], ascending=[False, False]).head(20).sort_values("registros")
        fig = px.bar(top_rows, x="registros", y="identificador", orientation="h", title="Top entidades por quantidade de registros", color="valor_total", color_continuous_scale=["#d8f3dc", "#0f4c5c"])
        fig.update_layout(height=520, margin=dict(l=10, r=10, t=60, b=10))
        st.plotly_chart(fig, width='stretch')
    display = entities.head(200).copy()
    display["valor_total"] = display["valor_total"].map(format_money)
    display["ticket_medio"] = display["ticket_medio"].map(format_money)
    st.dataframe(display[["identificador", "nome_osc", "registros", "valor_total", "ticket_medio", "ufs", "municipios", "primeiro_ano", "ultimo_ano"]], width='stretch', hide_index=True)


def render_quality(filtered: pd.DataFrame) -> None:
    st.subheader("Qualidade")
    left, right = st.columns([1.05, 0.95])
    with left:
        missing = (
            filtered.groupby("uf")[QUALITY_COLUMNS]
            .apply(lambda frame: frame.isna().mean() * 100)
            .reset_index()
            .melt(id_vars="uf", var_name="campo", value_name="faltante_pct")
        )
        heat = missing.pivot(index="uf", columns="campo", values="faltante_pct")
        fig = px.imshow(heat, aspect="auto", color_continuous_scale=["#eff7f6", "#ffbf69", "#d90429"], title="% de vazio por campo e UF")
        fig.update_layout(height=460, margin=dict(l=10, r=10, t=60, b=10))
        st.plotly_chart(fig, width='stretch')
    with right:
        alerts = pd.DataFrame(
            {
                "indicador": ["Valor zero", "Valor negativo", "Ano invalido", "Mes invalido", "Sem municipio", "Sem objeto", "Sem modalidade", "Duplicado aparente"],
                "quantidade": [
                    int(filtered["valor_zero"].sum()),
                    int(filtered["valor_negativo"].sum()),
                    int((~filtered["ano_valido"]).sum()),
                    int((filtered["mes"].notna() & ~filtered["mes_valido"]).sum()),
                    int((~filtered["tem_municipio"]).sum()),
                    int((~filtered["tem_objeto"]).sum()),
                    int((~filtered["tem_modalidade"]).sum()),
                    int(filtered["duplicado_aparente"].sum()),
                ],
            }
        )
        fig = px.bar(alerts.sort_values("quantidade"), x="quantidade", y="indicador", orientation="h", title="Alertas de qualidade", color="quantidade", color_continuous_scale=["#ffe5d9", "#9a031e"])
        fig.update_layout(height=460, margin=dict(l=10, r=10, t=60, b=10), coloraxis_showscale=False)
        st.plotly_chart(fig, width='stretch')


def render_texts(filtered: pd.DataFrame) -> None:
    st.subheader("Textos")
    source_label = st.selectbox("Campo textual", ["Objeto", "Nome da OSC", "Modalidade", "Municipio"])
    source_column = {"Objeto": "objeto", "Nome da OSC": "nome_osc", "Modalidade": "modalidade", "Municipio": "municipio"}[source_label]
    left, right = st.columns([0.8, 1.2])
    with left:
        freq = build_word_frequency(filtered[source_column], top_n=25)
        if freq.empty:
            st.info("Sem termos suficientes.")
        else:
            fig = px.bar(freq.sort_values("frequencia"), x="frequencia", y="termo", orientation="h", title="Termos mais frequentes", color="frequencia", color_continuous_scale=["#fff4e6", "#e36414"])
            fig.update_layout(height=500, margin=dict(l=10, r=10, t=60, b=10), coloraxis_showscale=False)
            st.plotly_chart(fig, width='stretch')
    with right:
        table = filtered[[source_column, "uf", "ano", "valor_total", "nome_osc", "municipio"]].rename(columns={source_column: "texto"}).dropna(subset=["texto"]).head(150)
        st.dataframe(table, width='stretch', hide_index=True)


def render_benchmark(filtered: pd.DataFrame, full_data: pd.DataFrame) -> None:
    st.subheader("Benchmark entre estados")
    benchmark = build_state_benchmark(full_data)
    current = build_state_benchmark(filtered)
    if benchmark.empty:
        st.info("Sem dados para benchmark.")
        return
    compare = current if len(filtered) != len(full_data) else benchmark
    render_benchmark_narratives(benchmark)

    export_frames = build_benchmark_export_frames(filtered, full_data)
    csv_bytes = export_frames["benchmark_atual"].to_csv(index=False, encoding="utf-8-sig").encode("utf-8-sig")
    excel_bytes = dataframe_to_excel_bytes(export_frames)

    download_col1, download_col2 = st.columns(2)
    with download_col1:
        st.download_button(
            "Baixar benchmark em CSV",
            data=csv_bytes,
            file_name="benchmark_ufs_recorte_atual.csv",
            mime="text/csv",
            width='stretch',
        )
    with download_col2:
        st.download_button(
            "Baixar Excel com resumo executivo",
            data=excel_bytes,
            file_name="relatorio_comparativo_ufs.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            width='stretch',
        )

    left, right = st.columns([1.1, 0.9])
    with left:
        fig = px.scatter(
            compare,
            x="registros",
            y="ticket_medio",
            size="valor_total",
            color="top5_share_pct",
            hover_name="uf",
            title="Volume x ticket medio x concentracao",
            color_continuous_scale=["#d8f3dc", "#e36414", "#9a031e"],
            log_x=True,
        )
        fig.update_layout(height=430, margin=dict(l=10, r=10, t=60, b=10))
        st.plotly_chart(fig, width='stretch')
    with right:
        fig = px.bar(
            compare.sort_values("valor_total", ascending=False).head(15),
            x="uf",
            y="share_nacional_pct" if "share_nacional_pct" in compare.columns else "valor_total",
            color="rank_ticket_medio",
            title="Peso relativo das UFs",
            color_continuous_scale=["#eff7f6", "#0f4c5c"],
        )
        fig.update_layout(height=430, margin=dict(l=10, r=10, t=60, b=10))
        st.plotly_chart(fig, width='stretch')

    display = benchmark.copy()
    for column in ["valor_total", "ticket_medio", "ticket_mediano"]:
        display[column] = display[column].map(format_money)
    for column in ["share_nacional_pct", "top1_share_pct", "top5_share_pct", "top10_share_pct", "cob_municipio", "cob_objeto", "cob_modalidade"]:
        display[column] = display[column].map(format_pct)
    st.dataframe(
        display[["uf", "rank_valor_total", "rank_registros", "rank_ticket_medio", "rank_concentracao", "valor_total", "registros", "ticket_medio", "ticket_mediano", "share_nacional_pct", "top1_share_pct", "top5_share_pct", "top10_share_pct", "entidades", "cob_municipio", "cob_objeto", "cob_modalidade"]],
        width='stretch',
        hide_index=True,
    )


def render_histories() -> None:
    st.subheader("Historias")
    docs = load_history_documents(str(HISTORY_DIR))
    if not docs:
        st.warning("Nenhum markdown foi encontrado em `historia/`. Rode `python gerar_historias.py` para gerar as narrativas.")
        return

    ordered_keys = [key for key in sorted(docs.keys()) if key != "INDEX"]
    anchors = {key: history_anchor_id(docs[key], key) for key in ordered_keys}
    labels = {key: history_display_label(docs[key], key) for key in ordered_keys}
    st.markdown(
        """
        <style>
        .history-nav {
            position: sticky;
            top: 1rem;
            max-height: calc(100vh - 3rem);
            overflow-y: auto;
            padding: 0.9rem 1rem;
            border: 1px solid rgba(15,76,92,0.10);
            border-radius: 16px;
            background: rgba(255,255,255,0.92);
        }
        .history-nav h4 {
            margin: 0 0 0.75rem 0;
            font-size: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    nav_col, content_col = st.columns([0.28, 0.72], gap="large")

    with nav_col:
        st.markdown('<div class="history-nav">', unsafe_allow_html=True)
        st.markdown("#### Navegacao")
        mode = st.radio("Visao", ["Corrido", "Selecionar UF"], label_visibility="collapsed")
        if mode == "Selecionar UF":
            label_options = [labels[key] for key in ordered_keys]
            selected_label = st.selectbox("Escolha a UF", label_options, index=0, label_visibility="collapsed")
            selected = next(key for key in ordered_keys if labels[key] == selected_label)
            markdown = docs.get(selected, "")
            st.download_button(
                "Baixar markdown",
                data=markdown.encode("utf-8"),
                file_name=f"{selected}.md",
                mime="text/markdown",
                width='stretch',
            )
        else:
            st.caption("Clique para navegar na mesma pagina.")
            summary_links = "\n".join(f"- [{labels[key]}](#{anchors[key]})" for key in ordered_keys)
            st.markdown(summary_links)
        st.markdown('</div>', unsafe_allow_html=True)

    with content_col:
        if mode == "Selecionar UF":
            markdown = docs.get(selected, "")
            title, body = split_history_markdown(markdown, selected)
            st.caption(f"Lendo `{selected}.md` da pasta `historia/`.")
            st.header(title, anchor=anchors[selected])
            if body:
                st.markdown(body)
        else:
            st.caption("Leitura encadeada em formato corrido, como uma wiki sequencial por UF.")
            st.header("Sumario", anchor="sumario")
            for key in ordered_keys:
                title, body = split_history_markdown(docs[key], key)
                st.header(title, anchor=anchors[key])
                if body:
                    st.markdown(body)
                st.markdown("[Voltar ao sumario](#sumario)")


def main() -> None:
    st.set_page_config(page_title="Dashboard Parquets OSC", page_icon=":bar_chart:", layout="wide")
    data_dir = st.sidebar.text_input("Pasta dos parquets", value=str(DEFAULT_DATA_DIR))
    data, files_df = load_data(data_dir)
    if data.empty:
        st.error(f"Nenhum arquivo .parquet foi encontrado em {data_dir}.")
        return

    render_header(data, files_df, data_dir)
    selected_ufs, year_range, selected_months, selected_modalities, minimum_value, only_valid_cnpj, exclude_zero_negative, search_text = render_sidebar(data, files_df)
    filtered = apply_filters(
        data,
        selected_ufs,
        year_range,
        selected_months,
        selected_modalities,
        minimum_value,
        only_valid_cnpj,
        exclude_zero_negative,
        search_text,
    )
    st.caption("O dashboard cruza volume, temporalidade, concentracao, cobertura e benchmarking entre UFs a partir dos parquets consolidados.")
    with st.expander("Premissas de leitura"):
        st.markdown(
            """
            - `valor_num` e derivado de `valor_total`.
            - `ano_num` e `mes_num` sao lidos como inteiros quando possivel.
            - `tem_cnpj_valido` usa 14 digitos apos limpeza.
            - `duplicado_aparente` considera igualdade nos campos centrais do schema.
            - O benchmark entre UFs ajuda a distinguir estados puxados por volume, ticket medio ou concentracao.
            """
        )
    if filtered.empty:
        st.warning("Os filtros atuais nao retornaram registros.")
        return

    tabs = st.tabs(["Panorama", "Temporal", "Territorio", "Entidades", "Qualidade", "Textos", "Benchmark UFs", "Historias"])
    with tabs[0]:
        render_overview(filtered, data)
    with tabs[1]:
        render_temporal(filtered)
    with tabs[2]:
        render_territory(filtered)
    with tabs[3]:
        render_entities(filtered)
    with tabs[4]:
        render_quality(filtered)
    with tabs[5]:
        render_texts(filtered)
    with tabs[6]:
        render_benchmark(filtered, data)
    with tabs[7]:
        render_histories()


if __name__ == "__main__":
    main()
