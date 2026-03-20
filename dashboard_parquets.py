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
AUDIT_REPORT_PATH = BASE_DIR / "auditoria_processada.xlsx"
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


def derive_instrument_type(data: pd.DataFrame) -> pd.Series:
    modalidade = data["modalidade"].fillna("").astype("string").str.lower()
    objeto = data["objeto"].fillna("").astype("string").str.lower()
    instrument_type = pd.Series("Outros", index=data.index, dtype="string")

    no_info = modalidade.eq("") & objeto.eq("")
    instrument_type.loc[no_info] = "Nao classificado"

    convenio_mask = modalidade.str.contains("convenio|convênio", regex=True) | objeto.str.contains("convenio|convênio", regex=True)
    instrument_type.loc[convenio_mask] = "Convenio"

    parceria_mask = (
        modalidade.str.contains("termo de fomento|termo de colaboracao|termo de colaboração|termo de cooperacao|termo de cooperação|termo de parceria|parceria", regex=True)
        | objeto.str.contains("termo de fomento|termo de colaboracao|termo de colaboração|termo de cooperacao|termo de cooperação|termo de parceria|parceria", regex=True)
    )
    instrument_type.loc[parceria_mask] = "Parceria / termo"

    transferencia_mask = (
        modalidade.str.contains("transferencia|transferência|repasse|auxilio|auxílio|subvenc|contribui", regex=True)
        | objeto.str.contains("transferencia|transferência|repasse|auxilio|auxílio|subvenc|contribui", regex=True)
    )
    instrument_type.loc[transferencia_mask] = "Transferencia / auxilio"

    licitacao_mask = (
        modalidade.str.contains("pregao|pregão|concorr|licit|tomada de preco|tomada de preço|dispensa|dispensad|inexig", regex=True)
        | objeto.str.contains("pregao|pregão|concorr|licit|tomada de preco|tomada de preço|dispensa|inexig", regex=True)
    )
    instrument_type.loc[licitacao_mask] = "Licitacao / contratacao"

    status_mask = modalidade.str.contains(
        "prestacao de contas|prestação de contas|em execucao|em execução|encerrado|vigente|finalizada|formalizada|extinto|rescind|cadastrado|aprovado|lançado|lancado|cancelado",
        regex=True,
    )
    instrument_type.loc[status_mask & instrument_type.isin(["Outros", "Nao classificado"])] = "Status / prestacao de contas"

    return instrument_type.fillna("Outros")


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
    data["tipo_instrumento"] = derive_instrument_type(data)

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


@st.cache_data(show_spinner=False)
def load_audit_summary_sheet(audit_path: str) -> pd.DataFrame:
    path = Path(audit_path)
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_excel(path, sheet_name="Resumo")
    except Exception:
        return pd.DataFrame()


@st.cache_data(show_spinner=False)
def load_audit_sheet_names(audit_path: str) -> list[str]:
    path = Path(audit_path)
    if not path.exists():
        return []
    try:
        return pd.ExcelFile(path).sheet_names
    except Exception:
        return []


def resolve_audit_sheet_name(uf: str, audit_path: str) -> str | None:
    suffix = f" - {uf}"
    return next((name for name in load_audit_sheet_names(audit_path) if name.endswith(suffix)), None)


@st.cache_data(show_spinner=False)
def load_audit_sheet_detail(audit_path: str, sheet_name: str) -> dict[str, pd.DataFrame]:
    path = Path(audit_path)
    if not path.exists() or not sheet_name:
        return {}

    try:
        df = pd.read_excel(path, sheet_name=sheet_name)
    except Exception:
        return {}

    def section(start: int, end: int, columns: list[str]) -> pd.DataFrame:
        chunk = df.iloc[:, start:end].copy()
        chunk.columns = columns
        chunk = chunk.dropna(how="all")
        if chunk.empty:
            return chunk
        first_col = columns[0]
        chunk = chunk[chunk[first_col].notna()].copy()
        for column in chunk.columns:
            if chunk[column].dtype == "object":
                chunk[column] = chunk[column].astype("string").str.strip()
        return chunk.reset_index(drop=True)

    return {
        "metrics": section(0, 2, ["metrica", "valor"]),
        "years": section(4, 6, ["ano", "quantidade"]),
        "empty_columns": section(8, 9, ["coluna_sem_dados"]),
        "missing_cnpj_examples": section(11, 12, ["exemplo_nome_osc_sem_cnpj"]),
        "source_files": section(14, 15, ["arquivo_bruto"]),
        "mapping": section(16, 19, ["campo_schema", "origem_bruta", "regra"]),
    }


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


def build_runtime_audit_summary(data: pd.DataFrame) -> pd.DataFrame:
    if data.empty:
        return pd.DataFrame()

    rows: list[dict[str, object]] = []
    for uf, frame in data.groupby("uf", dropna=False):
        invalid_year_mask = frame["ano"].notna() & ~frame["ano_valido"]
        invalid_month_mask = frame["mes"].notna() & ~frame["mes_valido"]
        invalid_cnpj_mask = frame["cnpj"].notna() & ~frame["tem_cnpj_valido"]
        empty_columns = [
            column
            for column in STANDARD_COLUMNS
            if column != "uf" and frame[column].notna().sum() == 0
        ]
        completeness_components = [
            frame["ano"].notna().mean(),
            frame["tem_cnpj_valido"].mean(),
            frame["tem_municipio"].mean(),
            frame["tem_objeto"].mean(),
            frame["tem_modalidade"].mean(),
            frame["data_inicio"].notna().mean(),
            frame["data_fim"].notna().mean(),
        ]
        rows.append(
            {
                "uf": uf,
                "registros": len(frame),
                "valor_total": float(frame["valor_num"].sum()),
                "valor_zero": int(frame["valor_zero"].sum()),
                "valor_negativo": int(frame["valor_negativo"].sum()),
                "linhas_sem_ano": int(frame["ano"].isna().sum()),
                "anos_invalidos": int(invalid_year_mask.sum()),
                "meses_invalidos": int(invalid_month_mask.sum()),
                "cnpj_invalidos": int(invalid_cnpj_mask.sum()),
                "sem_municipio": int((~frame["tem_municipio"]).sum()),
                "sem_objeto": int((~frame["tem_objeto"]).sum()),
                "sem_modalidade": int((~frame["tem_modalidade"]).sum()),
                "duplicados_aparentes": int(frame["duplicado_aparente"].sum()),
                "colunas_sem_dados_qtd": len(empty_columns),
                "colunas_sem_dados_lista": ", ".join(empty_columns) if empty_columns else "(nenhuma)",
                "completude_pct": float(np.mean(completeness_components) * 100),
            }
        )

    summary = pd.DataFrame(rows)
    summary["indice_alerta"] = (
        (summary["valor_negativo"] > 0).astype(int) * 4
        + (summary["anos_invalidos"] > 0).astype(int) * 3
        + (summary["linhas_sem_ano"] > 0).astype(int) * 2
        + (summary["meses_invalidos"] > 0).astype(int) * 2
        + (summary["cnpj_invalidos"] > 0).astype(int) * 2
        + (summary["colunas_sem_dados_qtd"] > 0).astype(int) * 2
        + (summary["sem_objeto"] > 0).astype(int)
        + (summary["sem_municipio"] > 0).astype(int)
        + (summary["sem_modalidade"] > 0).astype(int)
        + (summary["duplicados_aparentes"] > 0).astype(int)
        + (summary["valor_zero"] > 0).astype(int)
    )
    return summary.sort_values(["indice_alerta", "registros"], ascending=[False, False]).reset_index(drop=True)


def build_year_distribution(frame: pd.DataFrame) -> pd.DataFrame:
    if frame.empty:
        return pd.DataFrame(columns=["ano", "quantidade"])

    years = frame["ano"].astype("string").str.strip()
    years = years.fillna("(sem ano)")
    years = years.replace({"<NA>": "(sem ano)"})
    years = years.str.replace(r"\.0+$", "", regex=True)
    counts = years.value_counts(dropna=False).rename_axis("ano").reset_index(name="quantidade")
    return counts.sort_values("ano").reset_index(drop=True)


def build_missing_cnpj_examples_runtime(frame: pd.DataFrame, limit: int = 10) -> pd.DataFrame:
    if frame.empty:
        return pd.DataFrame(columns=["exemplo_nome_osc_sem_cnpj"])

    examples = (
        frame.loc[frame["cnpj"].isna(), "nome_osc"]
        .dropna()
        .astype("string")
        .str.strip()
        .replace({"": pd.NA})
        .dropna()
        .drop_duplicates()
        .head(limit)
        .tolist()
    )
    if not examples:
        examples = ["(nenhum)"]
    return pd.DataFrame({"exemplo_nome_osc_sem_cnpj": examples})


def build_field_completeness(frame: pd.DataFrame) -> pd.DataFrame:
    if frame.empty:
        return pd.DataFrame(columns=["campo", "preenchidos", "faltantes", "cobertura_pct"])

    rows: list[dict[str, object]] = []
    total = len(frame)
    for column in STANDARD_COLUMNS:
        filled = int(frame[column].notna().sum())
        rows.append(
            {
                "campo": column,
                "preenchidos": filled,
                "faltantes": total - filled,
                "cobertura_pct": (filled / total * 100) if total else 0,
            }
        )
    return pd.DataFrame(rows).sort_values(["cobertura_pct", "campo"], ascending=[True, True]).reset_index(drop=True)


def build_invalid_year_examples(frame: pd.DataFrame, limit: int = 10) -> str:
    values = (
        frame.loc[frame["ano"].notna() & ~frame["ano_valido"], "ano"]
        .astype("string")
        .str.strip()
        .replace({"": pd.NA})
        .dropna()
        .drop_duplicates()
        .head(limit)
        .tolist()
    )
    return ", ".join(values) if values else "(nenhum)"


def apply_filters(
    data: pd.DataFrame,
    selected_ufs: list[str],
    year_range: tuple[int, int] | None,
    selected_modalities: list[str],
    selected_instrument_types: list[str],
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
    if selected_modalities:
        filtered = filtered[filtered["modalidade_base"].isin(selected_modalities)]
    if selected_instrument_types:
        filtered = filtered[filtered["tipo_instrumento"].isin(selected_instrument_types)]
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


def render_sidebar(data: pd.DataFrame, files_df: pd.DataFrame) -> tuple[list[str], tuple[int, int] | None, list[str], list[str], float, bool, bool, str]:
    st.sidebar.header("Filtros")
    available_ufs = sorted(data["uf"].dropna().unique().tolist())
    selected_ufs = st.sidebar.multiselect("UFs", available_ufs, default=available_ufs)
    valid_years = sorted(int(v) for v in data.loc[data["ano_valido"], "ano_num"].dropna().unique().tolist())
    year_range = None
    if valid_years:
        year_range = st.sidebar.slider("Faixa de ano", min(valid_years), max(valid_years), (min(valid_years), max(valid_years)))
    modalities = data["modalidade_base"].value_counts().head(25).index.tolist()
    selected_modalities = st.sidebar.multiselect("Modalidades", modalities, default=[])
    instrument_types = data["tipo_instrumento"].value_counts().index.tolist()
    selected_instrument_types = st.sidebar.multiselect("Tipo do instrumento", instrument_types, default=[])
    minimum_value = st.sidebar.number_input("Valor minimo", min_value=0.0, value=0.0, step=50000.0)
    only_valid_cnpj = st.sidebar.checkbox("Somente CNPJ valido", value=False)
    exclude_zero_negative = st.sidebar.checkbox("Excluir zero e negativos", value=False)
    search_text = st.sidebar.text_input("Busca textual")
    st.sidebar.divider()
    st.sidebar.caption(f"Arquivos lidos: {format_int(len(files_df))}")
    return selected_ufs, year_range, selected_modalities, selected_instrument_types, minimum_value, only_valid_cnpj, exclude_zero_negative, search_text


def render_tab_guide() -> None:
    st.markdown("**Guia das abas**")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            "**Panorama**\n\n"
            "Resumo geral do recorte: volume, valor, ticket medio e quadro comparativo por UF."
        )
        st.info(
            "**Temporal**\n\n"
            "Evolucao por ano, com serie historica e heatmap para ver mudancas de ritmo."
        )
        st.info(
            "**Territorio**\n\n"
            "Distribuicao territorial dos recursos por UF e municipio."
        )

    with col2:
        st.info(
            "**Entidades**\n\n"
            "Ranking e perfil das OSCs ou beneficiarios com maior peso financeiro ou maior volume de registros."
        )
        st.info(
            "**Auditoria**\n\n"
            "Painel de revisao por UF, com subsecao de qualidade dos dados e subsecao de benchmark entre estados."
        )

    with col3:
        st.info(
            "**Historias**\n\n"
            "Narrativas corridas por UF, em formato de wiki, com interpretacao analitica e fontes."
        )


def render_overview(filtered: pd.DataFrame, full_data: pd.DataFrame, overview_base: pd.DataFrame) -> None:
    st.subheader("Panorama")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Registros", format_int(len(filtered)))
    col2.metric("Valor total", format_money(filtered["valor_num"].sum()))
    col3.metric("Ticket medio", format_money(filtered["valor_num"].mean()))
    col4.metric("Mediana", format_money(filtered["valor_num"].median()))
    col5.metric("Entidades", format_int(filtered["nome_osc"].dropna().nunique()))
    col6.metric("CNPJs validos", format_int(filtered.loc[filtered["tem_cnpj_valido"], "cnpj"].dropna().nunique()))

    valid_years = sorted(int(year) for year in overview_base.loc[overview_base["ano_valido"], "ano_num"].dropna().unique().tolist())
    mode_col1, mode_col2 = st.columns([0.38, 0.62])
    with mode_col1:
        overview_mode = st.radio(
            "Janela temporal do panorama",
            ["Recorte atual", "Ano isolado", "Faixa acumulada"],
            horizontal=True,
            key="overview_time_mode",
        )

    comparison_source = filtered
    comparison_label = "recorte atual"

    with mode_col2:
        if overview_mode == "Ano isolado" and valid_years:
            selected_year = st.selectbox(
                "Ano do panorama",
                valid_years,
                index=len(valid_years) - 1,
                key="overview_single_year",
            )
            comparison_source = overview_base.loc[overview_base["ano_num"].eq(selected_year)].copy()
            comparison_label = f"ano {selected_year}"
        elif overview_mode == "Faixa acumulada" and valid_years:
            selected_range = st.slider(
                "Faixa acumulada do panorama",
                min_value=min(valid_years),
                max_value=max(valid_years),
                value=(min(valid_years), max(valid_years)),
                key="overview_year_range",
            )
            comparison_source = overview_base.loc[
                overview_base["ano_num"].between(selected_range[0], selected_range[1], inclusive="both")
            ].copy()
            comparison_label = f"acumulado de {selected_range[0]} a {selected_range[1]}"

    summary = build_uf_summary(comparison_source)
    left, right = st.columns([1.2, 0.8])
    with left:
        fig = px.bar(
            summary.sort_values("valor_total").tail(15),
            x="valor_total",
            y="uf",
            orientation="h",
            title=f"Valor total por UF ({comparison_label})",
            color="valor_total",
            color_continuous_scale=["#d8f3dc", "#0f4c5c"],
        )
        fig.update_layout(height=440, margin=dict(l=10, r=10, t=60, b=10), coloraxis_showscale=False)
        st.plotly_chart(fig, width="stretch")
    with right:
        positive = filtered.loc[filtered["valor_num"].gt(0), "valor_num"].dropna()
        if positive.empty:
            st.info("Sem valores positivos para distribuicao.")
        else:
            hist = pd.DataFrame({"log10_valor": np.log10(positive.clip(lower=1))})
            fig = px.histogram(hist, x="log10_valor", nbins=40, title="Distribuicao dos valores (log10)", color_discrete_sequence=["#e36414"])
            fig.update_layout(height=440, margin=dict(l=10, r=10, t=60, b=10))
            st.plotly_chart(fig, width="stretch")

    st.markdown("**Leitura por tipo do instrumento**")
    instrument_summary = (
        comparison_source.groupby("tipo_instrumento", dropna=False)
        .agg(registros=("tipo_instrumento", "size"), valor_total=("valor_num", "sum"))
        .reset_index()
        .sort_values(["valor_total", "registros"], ascending=[False, False])
    )
    instrument_summary["share_valor_pct"] = instrument_summary["valor_total"] / max(instrument_summary["valor_total"].sum(), 1) * 100

    left, right = st.columns([1.0, 1.0])
    with left:
        fig = px.bar(
            instrument_summary.sort_values("valor_total", ascending=True),
            x="valor_total",
            y="tipo_instrumento",
            orientation="h",
            title="Valor total por tipo do instrumento",
            color="tipo_instrumento",
        )
        fig.update_layout(height=420, margin=dict(l=10, r=10, t=60, b=10), showlegend=False)
        st.plotly_chart(fig, width="stretch")
    with right:
        fig = px.pie(
            instrument_summary,
            names="tipo_instrumento",
            values="valor_total",
            title="Participacao no valor total",
            hole=0.45,
        )
        fig.update_traces(textposition="inside", textinfo="percent+label")
        fig.update_layout(height=420, margin=dict(l=10, r=10, t=60, b=10))
        st.plotly_chart(fig, width="stretch")

    instrument_display = instrument_summary.copy()
    instrument_display["valor_total"] = instrument_display["valor_total"].map(format_money)
    instrument_display["share_valor_pct"] = instrument_display["share_valor_pct"].map(format_pct)
    st.dataframe(instrument_display, width="stretch", hide_index=True)

    display = summary.copy()
    for column in ["valor_total", "ticket_medio", "ticket_mediano"]:
        display[column] = display[column].map(format_money)
    for column in ["cobertura_cnpj", "cobertura_municipio", "cobertura_objeto", "cobertura_modalidade"]:
        display[column] = display[column].map(format_pct)
    st.dataframe(display, width="stretch", hide_index=True)
    st.caption(
        f"O recorte atual representa {format_pct(len(filtered) / max(len(full_data), 1) * 100)} da base carregada. "
        f"Os graficos comparativos acima estao mostrando `{comparison_label}`."
    )


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
        st.plotly_chart(fig, width="stretch")
    with right:
        by_uf_year = filtered.loc[filtered["ano_valido"]].groupby(["uf", "ano_num"])["valor_num"].sum().reset_index()
        if by_uf_year.empty:
            st.info("Sem combinacoes de UF e ano.")
        else:
            heat = by_uf_year.pivot(index="uf", columns="ano_num", values="valor_num")
            fig = px.imshow(heat, aspect="auto", color_continuous_scale=["#fff4e6", "#fb8b24", "#9a031e"], title="Heatmap de valor por UF e ano")
            fig.update_layout(height=400, margin=dict(l=10, r=10, t=60, b=10))
            st.plotly_chart(fig, width="stretch")

    instrument_year = (
        filtered.loc[filtered["ano_valido"]]
        .groupby(["ano_num", "tipo_instrumento"], dropna=False)
        .agg(valor_total=("valor_num", "sum"), registros=("tipo_instrumento", "size"))
        .reset_index()
    )
    if not instrument_year.empty:
        st.markdown("**Evolucao por tipo do instrumento**")
        instrument_metric = st.radio(
            "Leitura por tipo",
            ["Valor total por tipo", "Registros por tipo"],
            horizontal=True,
            key="temporal_instrument_metric",
        )
        instrument_y = "valor_total" if instrument_metric == "Valor total por tipo" else "registros"
        fig = px.area(
            instrument_year,
            x="ano_num",
            y=instrument_y,
            color="tipo_instrumento",
            title=f"Evolucao anual por tipo do instrumento - {instrument_metric.lower()}",
        )
        fig.update_layout(height=430, margin=dict(l=10, r=10, t=60, b=10))
        st.plotly_chart(fig, width="stretch")

    st.markdown("**Corte anual por UF**")
    st.caption("Este grafico soma `valor_num` por UF no ano escolhido. Ele e o formato mais seguro para comparar estados em um ano especifico.")

    available_years = sorted(int(year) for year in annual["ano_num"].dropna().unique().tolist())
    default_year = available_years[-1]
    control_col1, control_col2 = st.columns([0.35, 0.65])
    with control_col1:
        selected_year = st.selectbox("Ano para comparar UFs", available_years, index=len(available_years) - 1)
    with control_col2:
        top_n = st.slider("Quantidade de UFs no ranking", min_value=5, max_value=min(len(by_uf_year["uf"].unique()), 27), value=min(15, len(by_uf_year["uf"].unique())))

    annual_cut = (
        filtered.loc[filtered["ano_num"].eq(selected_year)]
        .groupby("uf", dropna=False)
        .agg(valor_total=("valor_num", "sum"), registros=("uf", "size"), ticket_medio=("valor_num", "mean"))
        .reset_index()
        .sort_values(["valor_total", "registros"], ascending=[False, False])
    )

    if annual_cut.empty:
        st.info(f"Nao ha registros para {selected_year} no recorte atual.")
        return

    annual_type_cut = (
        filtered.loc[filtered["ano_num"].eq(selected_year)]
        .groupby(["uf", "tipo_instrumento"], dropna=False)
        .agg(valor_total=("valor_num", "sum"))
        .reset_index()
    )

    cut_left, cut_right = st.columns([1.0, 1.0])
    with cut_left:
        top_cut = annual_cut.head(top_n).sort_values("valor_total", ascending=True)
        fig = px.bar(
            top_cut,
            x="valor_total",
            y="uf",
            orientation="h",
            title=f"Valor repassado por UF ({selected_year})",
            text="valor_total",
            color="valor_total",
            color_continuous_scale=["#d8f3dc", "#0f4c5c"],
        )
        fig.update_traces(
            texttemplate="%{text:,.2f}",
            textposition="outside",
            hovertemplate="<b>%{y}</b><br>Valor total: %{x:,.2f}<extra></extra>",
            cliponaxis=False,
        )
        fig.update_layout(
            height=520,
            margin=dict(l=10, r=80, t=60, b=10),
            coloraxis_showscale=False,
            xaxis_title="Valor total",
            yaxis_title="UF",
        )
        st.plotly_chart(fig, width="stretch")
    with cut_right:
        annual_type_top = (
            annual_type_cut.groupby("uf", dropna=False)["valor_total"].sum().reset_index()
            .sort_values("valor_total", ascending=False)
            .head(top_n)["uf"]
            .tolist()
        )
        type_plot = annual_type_cut.loc[annual_type_cut["uf"].isin(annual_type_top)].copy()
        fig = px.bar(
            type_plot,
            x="uf",
            y="valor_total",
            color="tipo_instrumento",
            title=f"Composicao por tipo do instrumento ({selected_year})",
        )
        fig.update_layout(height=520, margin=dict(l=10, r=10, t=60, b=10), xaxis_title="UF", yaxis_title="Valor total")
        st.plotly_chart(fig, width="stretch")

    display = annual_cut.copy()
    display["valor_total"] = display["valor_total"].map(format_money)
    display["ticket_medio"] = display["ticket_medio"].map(format_money)
    st.dataframe(display, width="stretch", hide_index=True)


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
        st.plotly_chart(fig, width="stretch")
    with right:
        fig = px.treemap(geo.head(120), path=["uf", "municipio_base"], values="valor_total", color="registros", title="Treemap territorial")
        fig.update_layout(height=520, margin=dict(l=10, r=10, t=60, b=10))
        st.plotly_chart(fig, width="stretch")


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
        st.plotly_chart(fig, width="stretch")
    with right:
        top_rows = entities.sort_values(["registros", "valor_total"], ascending=[False, False]).head(20).sort_values("registros")
        fig = px.bar(top_rows, x="registros", y="identificador", orientation="h", title="Top entidades por quantidade de registros", color="valor_total", color_continuous_scale=["#d8f3dc", "#0f4c5c"])
        fig.update_layout(height=520, margin=dict(l=10, r=10, t=60, b=10))
        st.plotly_chart(fig, width="stretch")
    display = entities.head(200).copy()
    display["valor_total"] = display["valor_total"].map(format_money)
    display["ticket_medio"] = display["ticket_medio"].map(format_money)
    st.dataframe(display[["identificador", "nome_osc", "registros", "valor_total", "ticket_medio", "ufs", "municipios", "primeiro_ano", "ultimo_ano"]], width="stretch", hide_index=True)


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
        st.plotly_chart(fig, width="stretch")
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
        st.plotly_chart(fig, width="stretch")


def render_audit(filtered: pd.DataFrame, full_data: pd.DataFrame, data_dir: str) -> None:
    st.subheader("Auditoria")
    subsection = st.radio(
        "Subsecao de auditoria",
        ["Painel", "Qualidade", "Benchmark UFs"],
        horizontal=True,
        label_visibility="collapsed",
    )

    if subsection == "Qualidade":
        st.caption("Cobertura dos campos e alertas de dados faltantes, anos invalidos, valores negativos e duplicidades aparentes.")
        render_quality(filtered)
        return

    if subsection == "Benchmark UFs":
        st.caption("Comparacao entre estados para identificar quem cresce por volume, ticket medio ou concentracao.")
        render_benchmark(filtered, full_data)
        return

    st.caption("A melhor estrategia e ler a auditoria em duas camadas: primeiro o painel nacional de riscos, depois o detalhe da UF com colunas vazias, anos suspeitos e trilha de origem.")

    scope = st.radio("Escopo da auditoria", ["Base completa", "Recorte atual"], horizontal=True)
    audit_data = full_data if scope == "Base completa" else filtered
    summary = build_runtime_audit_summary(audit_data)
    if summary.empty:
        st.info("Sem dados para auditoria.")
        return

    audit_available = AUDIT_REPORT_PATH.exists()
    audit_summary_sheet = load_audit_summary_sheet(str(AUDIT_REPORT_PATH)) if audit_available else pd.DataFrame()

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("UFs auditadas", format_int(summary["uf"].nunique()))
    col2.metric("Registros auditados", format_int(summary["registros"].sum()))
    col3.metric("UFs com anos suspeitos", format_int((summary["anos_invalidos"] > 0).sum()))
    col4.metric("UFs com colunas vazias", format_int((summary["colunas_sem_dados_qtd"] > 0).sum()))
    col5.metric("UFs com valor zero/negativo", format_int(((summary["valor_zero"] + summary["valor_negativo"]) > 0).sum()))

    left, right = st.columns([1.1, 0.9])
    with left:
        heat_source = summary[
            [
                "uf",
                "linhas_sem_ano",
                "anos_invalidos",
                "meses_invalidos",
                "cnpj_invalidos",
                "sem_municipio",
                "sem_objeto",
                "sem_modalidade",
                "valor_zero",
                "valor_negativo",
                "duplicados_aparentes",
                "colunas_sem_dados_qtd",
            ]
        ].copy()
        heat_source = heat_source.rename(
            columns={
                "linhas_sem_ano": "sem_ano",
                "anos_invalidos": "ano_invalido",
                "meses_invalidos": "mes_invalido",
                "cnpj_invalidos": "cnpj_invalido",
                "sem_municipio": "sem_municipio",
                "sem_objeto": "sem_objeto",
                "sem_modalidade": "sem_modalidade",
                "valor_zero": "valor_zero",
                "valor_negativo": "valor_negativo",
                "duplicados_aparentes": "duplicado",
                "colunas_sem_dados_qtd": "colunas_vazias",
            }
        )
        heat = heat_source.set_index("uf")
        fig = px.imshow(heat, aspect="auto", color_continuous_scale=["#eff7f6", "#ffbf69", "#9a031e"], title="Mapa de alertas por UF")
        fig.update_layout(height=470, margin=dict(l=10, r=10, t=60, b=10))
        st.plotly_chart(fig, width="stretch")
    with right:
        fig = px.scatter(
            summary,
            x="linhas_sem_ano",
            y="colunas_sem_dados_qtd",
            size="registros",
            color="indice_alerta",
            hover_name="uf",
            custom_data=["anos_invalidos", "valor_zero", "valor_negativo", "sem_objeto"],
            title="Prioridade de revisao por UF",
            color_continuous_scale=["#d8f3dc", "#e36414", "#9a031e"],
        )
        fig.update_traces(
            hovertemplate=(
                "<b>%{hovertext}</b><br>"
                + "Linhas sem ano: %{x}<br>"
                + "Colunas vazias: %{y}<br>"
                + "Anos invalidos: %{customdata[0]}<br>"
                + "Valores zero: %{customdata[1]}<br>"
                + "Valores negativos: %{customdata[2]}<br>"
                + "Sem objeto: %{customdata[3]}<extra></extra>"
            )
        )
        fig.update_layout(height=470, margin=dict(l=10, r=10, t=60, b=10))
        st.plotly_chart(fig, width="stretch")

    display = summary.copy()
    display["valor_total"] = display["valor_total"].map(format_money)
    display["completude_pct"] = display["completude_pct"].map(format_pct)
    st.dataframe(
        display[
            [
                "uf",
                "indice_alerta",
                "registros",
                "valor_total",
                "completude_pct",
                "linhas_sem_ano",
                "anos_invalidos",
                "meses_invalidos",
                "cnpj_invalidos",
                "valor_zero",
                "valor_negativo",
                "sem_municipio",
                "sem_objeto",
                "sem_modalidade",
                "duplicados_aparentes",
                "colunas_sem_dados_qtd",
                "colunas_sem_dados_lista",
            ]
        ],
        width="stretch",
        hide_index=True,
    )

    st.markdown("**Detalhe por UF**")
    ordered_ufs = summary.sort_values(["indice_alerta", "registros"], ascending=[False, False])["uf"].tolist()
    selected_uf = st.selectbox("Escolha a UF para investigar", ordered_ufs, index=0)
    state_frame = audit_data.loc[audit_data["uf"] == selected_uf].copy()
    state_row = summary.loc[summary["uf"] == selected_uf].iloc[0]
    parquet_path = Path(data_dir) / f"{selected_uf}.parquet"

    audit_detail: dict[str, pd.DataFrame] = {}
    sheet_name = resolve_audit_sheet_name(selected_uf, str(AUDIT_REPORT_PATH)) if audit_available else None
    if sheet_name:
        audit_detail = load_audit_sheet_detail(str(AUDIT_REPORT_PATH), sheet_name)

    top1, top2, top3, top4 = st.columns(4)
    top1.metric("Registros", format_int(state_row["registros"]))
    top2.metric("Completude", format_pct(state_row["completude_pct"]))
    top3.metric("Indice de alerta", format_int(state_row["indice_alerta"]))
    top4.metric("Valor zero/negativo", format_int(state_row["valor_zero"] + state_row["valor_negativo"]))

    summary_text = [
        f"Fonte principal desta UF: `{parquet_path}`.",
        f"O estado tem {format_int(state_row['registros'])} registros, valor agregado de {format_money(state_row['valor_total'])} e completude media de {format_pct(state_row['completude_pct'])}.",
        f"Os principais alertas sao: {format_int(state_row['linhas_sem_ano'])} linhas sem ano, {format_int(state_row['anos_invalidos'])} anos invalidos, {format_int(state_row['cnpj_invalidos'])} CNPJs invalidos e {format_int(state_row['colunas_sem_dados_qtd'])} colunas totalmente vazias.",
        f"Exemplos de anos suspeitos: {build_invalid_year_examples(state_frame)}.",
    ]
    if audit_available and not audit_summary_sheet.empty:
        summary_text.append(f"Fonte complementar da auditoria: `{AUDIT_REPORT_PATH}`.")
    st.info("\n\n".join(summary_text))

    detail_tabs = st.tabs(["Alertas", "Anos", "Campos", "Origem"])
    with detail_tabs[0]:
        alert_table = pd.DataFrame(
            {
                "indicador": [
                    "linhas_sem_ano",
                    "anos_invalidos",
                    "meses_invalidos",
                    "cnpj_invalidos",
                    "valor_zero",
                    "valor_negativo",
                    "sem_municipio",
                    "sem_objeto",
                    "sem_modalidade",
                    "duplicados_aparentes",
                ],
                "quantidade": [
                    int(state_row["linhas_sem_ano"]),
                    int(state_row["anos_invalidos"]),
                    int(state_row["meses_invalidos"]),
                    int(state_row["cnpj_invalidos"]),
                    int(state_row["valor_zero"]),
                    int(state_row["valor_negativo"]),
                    int(state_row["sem_municipio"]),
                    int(state_row["sem_objeto"]),
                    int(state_row["sem_modalidade"]),
                    int(state_row["duplicados_aparentes"]),
                ],
            }
        )
        fig = px.bar(alert_table.sort_values("quantidade"), x="quantidade", y="indicador", orientation="h", title=f"Alertas da UF {selected_uf}", color="quantidade", color_continuous_scale=["#ffe5d9", "#9a031e"])
        fig.update_layout(height=420, margin=dict(l=10, r=10, t=60, b=10), coloraxis_showscale=False)
        st.plotly_chart(fig, width="stretch")

        examples = audit_detail.get("missing_cnpj_examples", pd.DataFrame())
        if examples.empty:
            examples = build_missing_cnpj_examples_runtime(state_frame)
        st.dataframe(examples, width="stretch", hide_index=True)

    with detail_tabs[1]:
        years = audit_detail.get("years", pd.DataFrame())
        if years.empty:
            years = build_year_distribution(state_frame)
        st.dataframe(years, width="stretch", hide_index=True)

    with detail_tabs[2]:
        completeness = build_field_completeness(state_frame)
        completeness["cobertura_pct"] = completeness["cobertura_pct"].map(format_pct)
        st.dataframe(completeness, width="stretch", hide_index=True)

        empty_columns = audit_detail.get("empty_columns", pd.DataFrame())
        if empty_columns.empty:
            empty_columns = pd.DataFrame({"coluna_sem_dados": state_row["colunas_sem_dados_lista"].split(", ")})
        st.caption("Colunas totalmente vazias")
        st.dataframe(empty_columns, width="stretch", hide_index=True)

    with detail_tabs[3]:
        if audit_available:
            st.download_button(
                "Baixar auditoria_processada.xlsx",
                data=AUDIT_REPORT_PATH.read_bytes(),
                file_name="auditoria_processada.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                width="stretch",
            )
        else:
            st.caption("A planilha `auditoria_processada.xlsx` nao esta presente neste ambiente.")

        source_files = audit_detail.get("source_files", pd.DataFrame())
        mapping = audit_detail.get("mapping", pd.DataFrame())
        if not source_files.empty:
            st.markdown("**Arquivos brutos usados**")
            st.dataframe(source_files, width="stretch", hide_index=True)
        else:
            st.info("Os arquivos brutos usados nao estao disponiveis aqui. Se a planilha de auditoria estiver no deploy, esse bloco aparece automaticamente.")

        if not mapping.empty:
            st.markdown("**Mapeamento do schema**")
            st.dataframe(mapping, width="stretch", hide_index=True)
        else:
            st.info("O mapeamento campo a campo da origem bruta nao esta disponivel neste ambiente.")


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
            width="stretch",
        )
    with download_col2:
        st.download_button(
            "Baixar Excel com resumo executivo",
            data=excel_bytes,
            file_name="relatorio_comparativo_ufs.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            width="stretch",
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
        st.plotly_chart(fig, width="stretch")
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
        st.plotly_chart(fig, width="stretch")

    display = benchmark.copy()
    for column in ["valor_total", "ticket_medio", "ticket_mediano"]:
        display[column] = display[column].map(format_money)
    for column in ["share_nacional_pct", "top1_share_pct", "top5_share_pct", "top10_share_pct", "cob_municipio", "cob_objeto", "cob_modalidade"]:
        display[column] = display[column].map(format_pct)
    st.dataframe(
        display[["uf", "rank_valor_total", "rank_registros", "rank_ticket_medio", "rank_concentracao", "valor_total", "registros", "ticket_medio", "ticket_mediano", "share_nacional_pct", "top1_share_pct", "top5_share_pct", "top10_share_pct", "entidades", "cob_municipio", "cob_objeto", "cob_modalidade"]],
        width="stretch",
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
                width="stretch",
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
    selected_ufs, year_range, selected_modalities, selected_instrument_types, minimum_value, only_valid_cnpj, exclude_zero_negative, search_text = render_sidebar(data, files_df)
    filtered = apply_filters(
        data,
        selected_ufs,
        year_range,
        selected_modalities,
        selected_instrument_types,
        minimum_value,
        only_valid_cnpj,
        exclude_zero_negative,
        search_text,
    )
    filtered_without_year = apply_filters(
        data,
        selected_ufs,
        None,
        selected_modalities,
        selected_instrument_types,
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
            - A aba de auditoria combina sinais calculados direto dos parquets com a planilha `auditoria_processada.xlsx` quando ela estiver presente.
            """
        )
    render_tab_guide()
    if filtered.empty:
        st.warning("Os filtros atuais nao retornaram registros.")
        return

    sections = ["Panorama", "Temporal", "Territorio", "Entidades", "Auditoria", "Historias"]
    selected_section = st.radio("Secao", sections, horizontal=True, label_visibility="collapsed")

    if selected_section == "Panorama":
        render_overview(filtered, data, filtered_without_year)
    elif selected_section == "Temporal":
        render_temporal(filtered)
    elif selected_section == "Territorio":
        render_territory(filtered)
    elif selected_section == "Entidades":
        render_entities(filtered)
    elif selected_section == "Auditoria":
        render_audit(filtered, data, data_dir)
    elif selected_section == "Historias":
        render_histories()


if __name__ == "__main__":
    main()
