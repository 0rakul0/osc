# Rondonia (RO)

## Visao geral

Rondonia soma 2.323 registros e R$ 834.973.682,02 em valor total. No ranking geral da base, a UF esta em 22o lugar por valor, 18o por quantidade de registros, 19o por ticket medio e 16o por concentracao dos 5 maiores beneficiarios.

O perfil dominante da UF e base mais distribuida. O ticket medio e de R$ 359.437,66, a mediana e de R$ 100.000,00 e os 5 maiores beneficiarios concentram 34,4% do valor total.

_Fonte local deste bloco: `processada/RO.parquet`; campos e agregacoes usados: `valor_total`, `nome_osc`, `cnpj`, `ano`, agregacoes por UF, ranks e shares dos maiores beneficiarios._

## Leitura narrativa

Comparando com o conjunto nacional, RO aparece entre as UFs lideres por valor em `PR, SP, PB, MS, SE`, por volume em `SE, PB, PR, MG, RS`, por ticket medio em `PE, RR, RJ, AM, AC` e por concentracao em `AC, RR, PR, CE, PE`.

Na pratica, isso indica que Rondonia cresce principalmente por base mais distribuida. A participacao da UF no total nacional desta pasta e de 0,2%.

_Fonte local deste bloco: `processada/RO.parquet`; campos e agregacoes usados: benchmark nacional entre UFs, com comparacao de `valor_num`, `registros`, `ticket_medio` e `top5_share_pct`._

## Principais entidades

1. `49150352001607` - FUNDACAO PIO XII: R$ 138.930.010,25 em 7 registros.
2. `05903125000145` - MUNICIPIO DE PORTO VELHO: R$ 40.444.115,41 em 60 registros.
3. `04104816000116` - MUNICIPIO DE ARIQUEMES: R$ 39.889.531,18 em 90 registros.
4. `04092706000181` - MUNICIPIO DE VILHENA: R$ 37.283.781,84 em 64 registros.
5. `04092714000128` - MUNICIPIO DE CACOAL: R$ 30.375.007,25 em 82 registros.

_Fonte local deste bloco: `processada/RO.parquet`; campos e agregacoes usados: agrupamento por `nome_osc` e `cnpj`, soma de `valor_num` e contagem de registros._

## Gastos e objetivos

Termos mais frequentes nos objetos da UF: `ESPECIALIZADA, SAUDE, UNIDADE, ATENCAO, RECURSOS, REALIZACAO, SEMINARIO, CONSTRUCAO, RONDONIA, HIDRICOS, AMPLIACAO`.

Registros de maior valor que ajudam a explicar os objetivos do gasto:

1. `CONSELHO REGIONAL DE ENGENHARIA E AGRONOMIA DO ESTADO DE RONDONIA` - R$ 328.486,00 (ano 2022): REALIZACAO DO II SEMINARIO ESTADUAL DE RECURSOS HIDRICOS DO ESTADO DE RONDONIA..
2. `FUNDO MUNICIPAL DE SAUDE DE SERINGUEIRAS` - R$ 290.000,00 (ano 2021): AMPLIACAO DE UNIDADE DE ATENCAO ESPECIALIZADA EM SAUDE.
3. `FUNDO MUNICIPAL DE SAUDE DE NOVA MAMORE` - R$ 200.000,00 (ano 2022): CONSTRUCAO DE UNIDADE DE ATENCAO ESPECIALIZADA EM SAUDE.
4. `FUNDO MUNICIPAL DE SAUDE DE CACAULANDIA` - R$ 135.000,00 (ano 2022): CONSTRUCAO DE UNIDADE DE ATENCAO ESPECIALIZADA EM SAUDE.
5. `FUNDO MUNICIPAL DE SAUDE DE NOVA MAMORE` - R$ 90.125,98 (ano 2020): CONSTRUCAO DE UNIDADE DE ATENCAO ESPECIALIZADA EM SAUDE.

O maior registro individual da UF foi para `FUNDACAO PIO XII` no valor de R$ 46.408.308,51. O objeto associado foi: .

_Fonte local deste bloco: `processada/RO.parquet`; campos e agregacoes usados: campos `objeto`, `valor_total`, `ano`; selecao dos maiores registros por `valor_num`._

## Evolucao temporal

Anos de maior volume:

1. `2022` - R$ 170.677.860,24 em 441 registros.
2. `2025` - R$ 134.655.922,19 em 264 registros.
3. `2021` - R$ 117.129.768,50 em 301 registros.

Ultimos anos da serie:

- `2021`: R$ 117.129.768,50 em 301 registros, variacao n/d.
- `2022`: R$ 170.677.860,24 em 441 registros, variacao 45,7%.
- `2023`: R$ 81.786.879,49 em 257 registros, variacao -52,1%.
- `2024`: R$ 111.162.776,16 em 361 registros, variacao 35,9%.
- `2025`: R$ 134.655.922,19 em 264 registros, variacao 21,1%.

_Fonte local deste bloco: `processada/RO.parquet`; campos e agregacoes usados: agregacao anual por `ano_num`, soma de `valor_num`, contagem de registros e variacao percentual._

## Territorio e cobertura

Municipios com maior valor acumulado no recorte:

1. `PORTO VELHO` - R$ 202.126.979,39 em 85 registros.
2. `ARIQUEMES` - R$ 44.948.748,06 em 125 registros.
3. `CACOAL` - R$ 40.098.489,58 em 90 registros.
4. `VILHENA` - R$ 39.621.635,36 em 72 registros.
5. `PIMENTA BUENO` - R$ 35.366.873,95 em 81 registros.

Cobertura observada: CNPJ valido em 100,0%, municipio em 98,1%, objeto em 0,5% e modalidade em 100,0%. Ha 0 registros negativos e 198 registros marcados como duplicado aparente.

_Fonte local deste bloco: `processada/RO.parquet`; campos e agregacoes usados: campos `municipio`, `cod_municipio`, `objeto`, `modalidade`, `cnpj`, `duplicado_aparente`, `valor_negativo`._

## Fontes extras

### Dados locais

- Arquivo principal desta historia: `processada/RO.parquet`.
- Todas as afirmacoes sobre gasto, volume, anos, concentracao, objetivos e municipios foram derivadas desse parquet.

### Fontes externas verificadas por entidade

- [Consulta oficial de CNPJ (gov.br)](https://www.gov.br/pt-br/servicos/consultar-cadastro-nacional-de-pessoas-juridicas)
- [Comprovante de inscricao e situacao cadastral (Receita)](https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp)
- [Convenios e transferencias federais (gov.br / Transferegov)](https://www.gov.br/planejamento/pt-br/acesso-a-informacao/convenios-e-transparencias)

- `FUNDACAO PIO XII` (49150352001607): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/49150352001607) - situacao ATIVA; municipio/UF PORTO VELHO/RO; porte DEMAIS; atividade principal Atividades de atendimento hospitalar, exceto pronto-socorro e unidades para atendimento a urgencias.
- `MUNICIPIO DE PORTO VELHO` (05903125000145): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/05903125000145) - situacao ATIVA; municipio/UF PORTO VELHO/RO; porte DEMAIS; atividade principal Administracao publica em geral.
- `MUNICIPIO DE ARIQUEMES` (04104816000116): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/04104816000116) - situacao ATIVA; municipio/UF ARIQUEMES/RO; porte DEMAIS; atividade principal Administracao publica em geral.
- `MUNICIPIO DE VILHENA` (04092706000181): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/04092706000181) - situacao ATIVA; municipio/UF VILHENA/RO; porte DEMAIS; atividade principal Administracao publica em geral.
- `MUNICIPIO DE CACOAL` (04092714000128): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/04092714000128) - situacao ATIVA; municipio/UF CACOAL/RO; porte DEMAIS; atividade principal Administracao publica em geral.

### Investigacao complementar

- [FUNDACAO PIO XII - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=49150352001607+FUNDACAO+PIO+XII+Rondonia+convenio+contrato+gestao)
- [MUNICIPIO DE PORTO VELHO - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=05903125000145+MUNICIPIO+DE+PORTO+VELHO+Rondonia+convenio+contrato+gestao)
- [MUNICIPIO DE ARIQUEMES - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=04104816000116+MUNICIPIO+DE+ARIQUEMES+Rondonia+convenio+contrato+gestao)
- [MUNICIPIO DE VILHENA - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=04092706000181+MUNICIPIO+DE+VILHENA+Rondonia+convenio+contrato+gestao)
- [MUNICIPIO DE CACOAL - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=04092714000128+MUNICIPIO+DE+CACOAL+Rondonia+convenio+contrato+gestao)

## Conclusao

Rondonia deve ser lido como uma UF puxada por base mais distribuida. Se o objetivo for auditar volume financeiro, os principais focos sao as entidades lideres e os anos de pico. Se o objetivo for comparar com outras UFs, os melhores eixos sao quantidade de registros, ticket medio, concentracao e cobertura dos campos territoriais.
