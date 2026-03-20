# Paraiba (PB)

## Visao geral

Paraiba soma 129.357 registros e R$ 48.548.653.875,69 em valor total. No ranking geral da base, a UF esta em 3o lugar por valor, 2o por quantidade de registros, 18o por ticket medio e 14o por concentracao dos 5 maiores beneficiarios.

O perfil dominante da UF e volume de dados. O ticket medio e de R$ 375.307,51, a mediana e de R$ 100.000,00 e os 5 maiores beneficiarios concentram 34,9% do valor total.

_Fonte local deste bloco: `processada/PB.parquet`; campos e agregacoes usados: `valor_total`, `nome_osc`, `cnpj`, `ano`, agregacoes por UF, ranks e shares dos maiores beneficiarios._

## Leitura narrativa

Comparando com o conjunto nacional, PB aparece entre as UFs lideres por valor em `PR, SP, PB, MS, SE`, por volume em `SE, PB, PR, MG, RS`, por ticket medio em `PE, RR, RJ, AM, AC` e por concentracao em `AC, RR, PR, CE, PE`.

Na pratica, isso indica que Paraiba cresce principalmente por volume de dados. A participacao da UF no total nacional desta pasta e de 13,2%.

_Fonte local deste bloco: `processada/PB.parquet`; campos e agregacoes usados: benchmark nacional entre UFs, com comparacao de `valor_num`, `registros`, `ticket_medio` e `top5_share_pct`._

## Principais entidades

1. `09125444000128` - SUPERINTENDENCIA DE OBRAS DO PLANO DE DESENVOLVIMENTO DO ESTADO DA PARAIBA: R$ 11.159.968.133,21 em 16.822 registros.
2. `02221962000104` - SECRETARIA DE ESTADO DA INFRAESTRUTURA E DOS RECURSOS HIDRICOS: R$ 2.935.858.942,47 em 1.780 registros.
3. `08999674000153` - PREFEITURA MUNICIPAL DE SOUSA: R$ 1.152.557.188,97 em 783 registros.
4. `09112236000194` - FUNDACAO NAPOLEAO LAUREANO: R$ 847.399.395,13 em 340 registros.
5. `08741688000172` - PREFEITURA MUNICIPAL DE POCINHOS: R$ 843.800.870,37 em 883 registros.

_Fonte local deste bloco: `processada/PB.parquet`; campos e agregacoes usados: agrupamento por `nome_osc` e `cnpj`, soma de `valor_num` e contagem de registros._

## Gastos e objetivos

Termos mais frequentes nos objetos da UF: `PROG, ESCOLAR, TRANSPORTE, TECNICA, REFORMA, ESCOLAS, FINANCEIRA, ADMINIST, COOPER, CONST, AQUISICAO, REALIZACAO`.

Registros de maior valor que ajudam a explicar os objetivos do gasto:

1. `COMPANHIA ESTADUAL DE HABITACAO POPULAR` - R$ 61.444.257,62 (ano 2013): PROG. DE MELHORIA HABITACIONAL.
2. `COMPANHIA ESTADUAL DE HABITACAO POPULAR` - R$ 61.444.257,62 (ano 2013): PROG. DE MELHORIA HABITACIONAL.
3. `COMPANHIA ESTADUAL DE HABITACAO POPULAR` - R$ 61.444.257,62 (ano 2013): PROG. DE MELHORIA HABITACIONAL.
4. `COMPANHIA ESTADUAL DE HABITACAO POPULAR` - R$ 61.444.257,62 (ano 2013): PROG. DE MELHORIA HABITACIONAL.
5. `COMPANHIA ESTADUAL DE HABITACAO POPULAR` - R$ 61.444.257,62 (ano 2013): PROG. DE MELHORIA HABITACIONAL.

O maior registro individual da UF foi para `COMPANHIA ESTADUAL DE HABITACAO POPULAR` no valor de R$ 61.444.257,62. O objeto associado foi: PROG. DE MELHORIA HABITACIONAL.

_Fonte local deste bloco: `processada/PB.parquet`; campos e agregacoes usados: campos `objeto`, `valor_total`, `ano`; selecao dos maiores registros por `valor_num`._

## Evolucao temporal

Anos de maior volume:

1. `2025` - R$ 14.207.690.445,30 em 24.862 registros.
2. `2024` - R$ 5.399.287.177,43 em 13.113 registros.
3. `2021` - R$ 2.893.826.409,89 em 7.144 registros.

Ultimos anos da serie:

- `2022`: R$ 2.118.410.224,02 em 12.175 registros, variacao n/d.
- `2023`: R$ 2.474.614.158,88 em 8.825 registros, variacao 16,8%.
- `2024`: R$ 5.399.287.177,43 em 13.113 registros, variacao 118,2%.
- `2025`: R$ 14.207.690.445,30 em 24.862 registros, variacao 163,1%.
- `2026`: R$ 960.645.401,32 em 931 registros, variacao -93,2%.

_Fonte local deste bloco: `processada/PB.parquet`; campos e agregacoes usados: agregacao anual por `ano_num`, soma de `valor_num`, contagem de registros e variacao percentual._

## Territorio e cobertura

Municipios com maior valor acumulado no recorte:

1. `JOAO PESSOA` - R$ 19.837.817.400,96 em 27.454 registros.
2. `CAMPINA GRANDE` - R$ 1.361.144.088,23 em 3.476 registros.
3. `SOUSA` - R$ 1.322.727.188,97 em 865 registros.
4. `POCINHOS` - R$ 845.809.030,37 em 890 registros.
5. `PATOS` - R$ 687.664.805,31 em 657 registros.

Cobertura observada: CNPJ valido em 100,0%, municipio em 99,8%, objeto em 100,0% e modalidade em 100,0%. Ha 0 registros negativos e 129.200 registros marcados como duplicado aparente.

_Fonte local deste bloco: `processada/PB.parquet`; campos e agregacoes usados: campos `municipio`, `cod_municipio`, `objeto`, `modalidade`, `cnpj`, `duplicado_aparente`, `valor_negativo`._

## Fontes extras

### Dados locais

- Arquivo principal desta historia: `processada/PB.parquet`.
- Todas as afirmacoes sobre gasto, volume, anos, concentracao, objetivos e municipios foram derivadas desse parquet.

### Fontes externas verificadas por entidade

- [Consulta oficial de CNPJ (gov.br)](https://www.gov.br/pt-br/servicos/consultar-cadastro-nacional-de-pessoas-juridicas)
- [Comprovante de inscricao e situacao cadastral (Receita)](https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp)
- [Convenios e transferencias federais (gov.br / Transferegov)](https://www.gov.br/planejamento/pt-br/acesso-a-informacao/convenios-e-transparencias)

- `SUPERINTENDENCIA DE OBRAS DO PLANO DE DESENVOLVIMENTO DO ESTADO DA PARAIBA` (09125444000128): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/09125444000128) - status da consulta 429.
- `SECRETARIA DE ESTADO DA INFRAESTRUTURA E DOS RECURSOS HIDRICOS` (02221962000104): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/02221962000104) - status da consulta 429.
- `PREFEITURA MUNICIPAL DE SOUSA` (08999674000153): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/08999674000153) - status da consulta 429.
- `FUNDACAO NAPOLEAO LAUREANO` (09112236000194): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/09112236000194) - status da consulta 429.
- `PREFEITURA MUNICIPAL DE POCINHOS` (08741688000172): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/08741688000172) - status da consulta 429.

### Investigacao complementar

- [SUPERINTENDENCIA DE OBRAS DO PLANO DE DESENVOLVIMENTO DO ESTADO DA PARAIBA - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=09125444000128+SUPERINTENDENCIA+DE+OBRAS+DO+PLANO+DE+DESENVOLVIMENTO+DO+ESTADO+DA+PARAIBA+Paraiba+convenio+contrato+gestao)
- [SECRETARIA DE ESTADO DA INFRAESTRUTURA E DOS RECURSOS HIDRICOS - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=02221962000104+SECRETARIA+DE+ESTADO+DA+INFRAESTRUTURA+E+DOS+RECURSOS+HIDRICOS+Paraiba+convenio+contrato+gestao)
- [PREFEITURA MUNICIPAL DE SOUSA - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=08999674000153+PREFEITURA+MUNICIPAL+DE+SOUSA+Paraiba+convenio+contrato+gestao)
- [FUNDACAO NAPOLEAO LAUREANO - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=09112236000194+FUNDACAO+NAPOLEAO+LAUREANO+Paraiba+convenio+contrato+gestao)
- [PREFEITURA MUNICIPAL DE POCINHOS - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=08741688000172+PREFEITURA+MUNICIPAL+DE+POCINHOS+Paraiba+convenio+contrato+gestao)

## Conclusao

Paraiba deve ser lido como uma UF puxada por volume de dados. Se o objetivo for auditar volume financeiro, os principais focos sao as entidades lideres e os anos de pico. Se o objetivo for comparar com outras UFs, os melhores eixos sao quantidade de registros, ticket medio, concentracao e cobertura dos campos territoriais.
