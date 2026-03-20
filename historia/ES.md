# Espirito Santo (ES)

## Visao geral

Espirito Santo soma 4.045 registros e R$ 2.693.692.617,15 em valor total. No ranking geral da base, a UF esta em 14o lugar por valor, 14o por quantidade de registros, 14o por ticket medio e 15o por concentracao dos 5 maiores beneficiarios.

O perfil dominante da UF e base mais distribuida. O ticket medio e de R$ 665.931,43, a mediana e de R$ 74.728,38 e os 5 maiores beneficiarios concentram 34,8% do valor total.

_Fonte local deste bloco: `processada/ES.parquet`; campos e agregacoes usados: `valor_total`, `nome_osc`, `cnpj`, `ano`, agregacoes por UF, ranks e shares dos maiores beneficiarios._

## Leitura narrativa

Comparando com o conjunto nacional, ES aparece entre as UFs lideres por valor em `PR, SP, PB, MS, SE`, por volume em `SE, PB, PR, MG, RS`, por ticket medio em `PE, RR, RJ, AM, AC` e por concentracao em `AC, RR, PR, CE, PE`.

Na pratica, isso indica que Espirito Santo cresce principalmente por base mais distribuida. A participacao da UF no total nacional desta pasta e de 0,7%.

_Fonte local deste bloco: `processada/ES.parquet`; campos e agregacoes usados: benchmark nacional entre UFs, com comparacao de `valor_num`, `registros`, `ticket_medio` e `top5_share_pct`._

## Principais entidades

1. `28127926000161` - ASSOCIACAO EVANGELICA BENEFICENTE E.SANTENSE: R$ 303.169.978,90 em 33 registros.
2. `27193705000129` - HECI HOSP EVANGELICO DE CACHOEIRO DE ITAPEMIRIM: R$ 205.528.714,15 em 12 registros.
3. `28141200000000` - SANTA CASA DE MISERICORDIA DE VITORIA: R$ 145.966.288,08 em 14 registros.
4. `27187087000104` - SANTA CASA DE MISERICORDIA DE CACHOEIRO DE IT: R$ 126.072.312,10 em 20 registros.
5. `28137925000106` - AFECC - HOSPITAL SANTA RITA DE CASSIA: R$ 107.473.465,20 em 13 registros.

_Fonte local deste bloco: `processada/ES.parquet`; campos e agregacoes usados: agrupamento por `nome_osc` e `cnpj`, soma de `valor_num` e contagem de registros._

## Gastos e objetivos

Termos mais frequentes nos objetos da UF: `PROC, AQUISICAO, MUNICIPIO, REALIZACAO, EQUIPAMENTOS, DESPESAS, CUSTEIO, 2010, ATENDIMENTO, CONSTRUCAO, 2009, PERMANENTE`.

Registros de maior valor que ajudam a explicar os objetivos do gasto:

1. `ASSOCIACAO EVANGELICA BENEFICENTE E.SANTENSE` - R$ 93.611.188,96 (ano 2013): INTEGRAR O CONVENENTE AO SISTEMA UNICO DE SAUDE - SUS                        PROC. 60275359.
2. `ASSOCIACAO EVANGELICA BENEFICENTE E.SANTENSE` - R$ 76.512.552,17 (ano 2012): INTEGRARA O CONVENENTE AO SUS. INSERCAO NA REDE REGIONALIZADA E HIERARQUIZADA DE ACOES E SERVICOS DE SAUDE. POA. PROC. 55838090.
3. `ASSOCIACAO EVANGELICA BENEFICENTE E.SANTENSE` - R$ 73.882.599,32 (ano 2011): PACTUACAO PARA PRESTACAO DE SERVICOS DE ATENDIMENTO AOS USUARIOS DO SUS NA   REGIAO ADSTRITA AO HOSPITAL. (PROC.49598325/2010).
4. `HECI HOSP EVANGELICO DE CACHOEIRO DE ITAPEMIRIM` - R$ 71.720.281,72 (ano 2013): INTEGRAR A CONVENENTE AO SISTEMA UNICO DE SAUDE - SUS PROC(60273844).
5. `HECI HOSP EVANGELICO DE CACHOEIRO DE ITAPEMIRIM` - R$ 61.389.433,86 (ano 2012): INTEGRAR O CONVENENTE AO SUS E A INSERCAO NA REDE REGIONALIZADA E HIERARQUIZADA DE ACOES E SERVICOS DE SAUDE. PROC. 55837778.

O maior registro individual da UF foi para `ASSOCIACAO EVANGELICA BENEFICENTE E.SANTENSE` no valor de R$ 93.611.188,96. O objeto associado foi: INTEGRAR O CONVENENTE AO SISTEMA UNICO DE SAUDE - SUS                        PROC. 60275359.

_Fonte local deste bloco: `processada/ES.parquet`; campos e agregacoes usados: campos `objeto`, `valor_total`, `ano`; selecao dos maiores registros por `valor_num`._

## Evolucao temporal

Anos de maior volume:

1. `2012` - R$ 726.508.312,13 em 686 registros.
2. `2011` - R$ 564.095.622,78 em 752 registros.
3. `2013` - R$ 516.872.618,08 em 330 registros.

Ultimos anos da serie:

- `2011`: R$ 564.095.622,78 em 752 registros, variacao n/d.
- `2012`: R$ 726.508.312,13 em 686 registros, variacao 28,8%.
- `2013`: R$ 516.872.618,08 em 330 registros, variacao -28,9%.
- `2015`: R$ 188.962.780,55 em 204 registros, variacao -63,4%.
- `2017`: R$ 69.480.626,44 em 347 registros, variacao -63,2%.

_Fonte local deste bloco: `processada/ES.parquet`; campos e agregacoes usados: agregacao anual por `ano_num`, soma de `valor_num`, contagem de registros e variacao percentual._

## Territorio e cobertura

Municipios com maior valor acumulado no recorte:

1. `VITORIA` - R$ 561.707.901,39 em 480 registros.
2. `CACHOEIRO DE ITAPEMIRIM` - R$ 419.935.419,14 em 123 registros.
3. `VILA VELHA` - R$ 406.423.125,94 em 141 registros.
4. `SEM MUNICIPIO INFORMADO` - R$ 217.833.034,38 em 314 registros.
5. `LINHARES` - R$ 96.272.659,93 em 67 registros.

Cobertura observada: CNPJ valido em 100,0%, municipio em 100,0%, objeto em 100,0% e modalidade em 0,6%. Ha 0 registros negativos e 2 registros marcados como duplicado aparente.

_Fonte local deste bloco: `processada/ES.parquet`; campos e agregacoes usados: campos `municipio`, `cod_municipio`, `objeto`, `modalidade`, `cnpj`, `duplicado_aparente`, `valor_negativo`._

## Fontes extras

### Dados locais

- Arquivo principal desta historia: `processada/ES.parquet`.
- Todas as afirmacoes sobre gasto, volume, anos, concentracao, objetivos e municipios foram derivadas desse parquet.

### Fontes externas verificadas por entidade

- [Consulta oficial de CNPJ (gov.br)](https://www.gov.br/pt-br/servicos/consultar-cadastro-nacional-de-pessoas-juridicas)
- [Comprovante de inscricao e situacao cadastral (Receita)](https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp)
- [Convenios e transferencias federais (gov.br / Transferegov)](https://www.gov.br/planejamento/pt-br/acesso-a-informacao/convenios-e-transparencias)

- `ASSOCIACAO EVANGELICA BENEFICENTE E.SANTENSE` (28127926000161): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/28127926000161) - status da consulta 429.
- `HECI HOSP EVANGELICO DE CACHOEIRO DE ITAPEMIRIM` (27193705000129): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/27193705000129) - status da consulta 429.
- `SANTA CASA DE MISERICORDIA DE VITORIA` (28141200000000): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/28141200000000) - status da consulta 429.
- `SANTA CASA DE MISERICORDIA DE CACHOEIRO DE IT` (27187087000104): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/27187087000104) - status da consulta 429.
- `AFECC - HOSPITAL SANTA RITA DE CASSIA` (28137925000106): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/28137925000106) - status da consulta 429.

### Investigacao complementar

- [ASSOCIACAO EVANGELICA BENEFICENTE E.SANTENSE - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=28127926000161+ASSOCIACAO+EVANGELICA+BENEFICENTE+E.SANTENSE+Espirito+Santo+convenio+contrato+gestao)
- [HECI HOSP EVANGELICO DE CACHOEIRO DE ITAPEMIRIM - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=27193705000129+HECI+HOSP+EVANGELICO+DE+CACHOEIRO+DE+ITAPEMIRIM+Espirito+Santo+convenio+contrato+gestao)
- [SANTA CASA DE MISERICORDIA DE VITORIA - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=28141200000000+SANTA+CASA+DE+MISERICORDIA+DE+VITORIA+Espirito+Santo+convenio+contrato+gestao)
- [SANTA CASA DE MISERICORDIA DE CACHOEIRO DE IT - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=27187087000104+SANTA+CASA+DE+MISERICORDIA+DE+CACHOEIRO+DE+IT+Espirito+Santo+convenio+contrato+gestao)
- [AFECC - HOSPITAL SANTA RITA DE CASSIA - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=28137925000106+AFECC+-+HOSPITAL+SANTA+RITA+DE+CASSIA+Espirito+Santo+convenio+contrato+gestao)

## Conclusao

Espirito Santo deve ser lido como uma UF puxada por base mais distribuida. Se o objetivo for auditar volume financeiro, os principais focos sao as entidades lideres e os anos de pico. Se o objetivo for comparar com outras UFs, os melhores eixos sao quantidade de registros, ticket medio, concentracao e cobertura dos campos territoriais.
