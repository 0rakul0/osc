# Piaui (PI)

## Visao geral

Piaui soma 160 registros e R$ 113.334.035,87 em valor total. No ranking geral da base, a UF esta em 25o lugar por valor, 23o por quantidade de registros, 13o por ticket medio e 8o por concentracao dos 5 maiores beneficiarios.

O perfil dominante da UF e base mais distribuida. O ticket medio e de R$ 708.337,72, a mediana e de R$ 14.073,86 e os 5 maiores beneficiarios concentram 61,3% do valor total.

_Fonte local deste bloco: `processada/PI.parquet`; campos e agregacoes usados: `valor_total`, `nome_osc`, `cnpj`, `ano`, agregacoes por UF, ranks e shares dos maiores beneficiarios._

## Leitura narrativa

Comparando com o conjunto nacional, PI aparece entre as UFs lideres por valor em `PR, SP, PB, MS, SE`, por volume em `SE, PB, PR, MG, RS`, por ticket medio em `PE, RR, RJ, AM, AC` e por concentracao em `AC, RR, PR, CE, PE`.

Na pratica, isso indica que Piaui cresce principalmente por base mais distribuida. A participacao da UF no total nacional desta pasta e de 0,0%.

_Fonte local deste bloco: `processada/PI.parquet`; campos e agregacoes usados: benchmark nacional entre UFs, com comparacao de `valor_num`, `registros`, `ticket_medio` e `top5_share_pct`._

## Principais entidades

1. `48211585004536` - SOCIEDADE BRASILEIRA CAMINHO DE DAMASCO: R$ 17.320.655,01 em 2 registros.
2. `06058863000104` - ASSOCIACAO FILANTROPICA NOVA ESPERANCA: R$ 15.553.937,45 em 4 registros.
3. `14702257003115` - INSTITUTO SAUDE E CIDADANIA - ISAC: R$ 11.679.936,16 em 1 registros.
4. `60701190000104` - ITAU UNIBANCO S A: R$ 11.071.983,62 em 2 registros.
5. `44660105000142` - AGENCIA DE ATRACAO DE INVESTIMENTOS ESTRATEGICOS DO PIAUI S/A: R$ 10.000.000,00 em 1 registros.

_Fonte local deste bloco: `processada/PI.parquet`; campos e agregacoes usados: agrupamento por `nome_osc` e `cnpj`, soma de `valor_num` e contagem de registros._

## Gastos e objetivos

Termos mais frequentes nos objetos da UF: `PIAUI, SAUDAVEL, GESTAO, EFICIENTE, TRANSPARENTE, NATUREZA, MUNICIPIO, ESPECIAL, ENCARGOS, REALIZACAO, TRANSFORMACAO, DIGITAL`.

Registros de maior valor que ajudam a explicar os objetivos do gasto:

1. `ASSOCIACAO FILANTROPICA NOVA ESPERANCA` - R$ 13.216.524,36 (ano 2025): PIAUI SAUDAVEL.
2. `INSTITUTO SAUDE E CIDADANIA - ISAC` - R$ 11.679.936,16 (ano 2025): PIAUI SAUDAVEL.
3. `AGENCIA DE ATRACAO DE INVESTIMENTOS ESTRATEGICOS DO PIAUI S/A` - R$ 10.000.000,00 (ano 2024): ENCARGOS DE NATUREZA ESPECIAL.
4. `SOCIEDADE BRASILEIRA CAMINHO DE DAMASCO` - R$ 9.405.163,37 (ano 2025): PIAUI SAUDAVEL.
5. `ASSOCIACAO REABILITAR - ASSOC PIAUIENSE DE HA` - R$ 8.393.441,87 (ano 2025): PIAUI SAUDAVEL.

O maior registro individual da UF foi para `ASSOCIACAO FILANTROPICA NOVA ESPERANCA` no valor de R$ 13.216.524,36. O objeto associado foi: PIAUI SAUDAVEL.

_Fonte local deste bloco: `processada/PI.parquet`; campos e agregacoes usados: campos `objeto`, `valor_total`, `ano`; selecao dos maiores registros por `valor_num`._

## Evolucao temporal

Anos de maior volume:

1. `2025` - R$ 86.085.921,99 em 56 registros.
2. `2024` - R$ 16.006.244,67 em 25 registros.
3. `2023` - R$ 11.241.262,75 em 55 registros.

Ultimos anos da serie:

- `2022`: R$ 606,46 em 11 registros, variacao n/d.
- `2023`: R$ 11.241.262,75 em 55 registros, variacao 1853486,8%.
- `2024`: R$ 16.006.244,67 em 25 registros, variacao 42,4%.
- `2025`: R$ 86.085.921,99 em 56 registros, variacao 437,8%.
- `2026`: R$ 0,00 em 13 registros, variacao -100,0%.

_Fonte local deste bloco: `processada/PI.parquet`; campos e agregacoes usados: agregacao anual por `ano_num`, soma de `valor_num`, contagem de registros e variacao percentual._

## Territorio e cobertura

A base desta UF nao traz cobertura territorial suficiente para destacar municipios com seguranca.

Cobertura observada: CNPJ valido em 100,0%, municipio em 26,9%, objeto em 99,4% e modalidade em 81,9%. Ha 0 registros negativos e 23 registros marcados como duplicado aparente.

_Fonte local deste bloco: `processada/PI.parquet`; campos e agregacoes usados: campos `municipio`, `cod_municipio`, `objeto`, `modalidade`, `cnpj`, `duplicado_aparente`, `valor_negativo`._

## Fontes extras

### Dados locais

- Arquivo principal desta historia: `processada/PI.parquet`.
- Todas as afirmacoes sobre gasto, volume, anos, concentracao, objetivos e municipios foram derivadas desse parquet.

### Fontes externas verificadas por entidade

- [Consulta oficial de CNPJ (gov.br)](https://www.gov.br/pt-br/servicos/consultar-cadastro-nacional-de-pessoas-juridicas)
- [Comprovante de inscricao e situacao cadastral (Receita)](https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp)
- [Convenios e transferencias federais (gov.br / Transferegov)](https://www.gov.br/planejamento/pt-br/acesso-a-informacao/convenios-e-transparencias)

- `SOCIEDADE BRASILEIRA CAMINHO DE DAMASCO` (48211585004536): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/48211585004536) - status da consulta 429.
- `ASSOCIACAO FILANTROPICA NOVA ESPERANCA` (06058863000104): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/06058863000104) - status da consulta 429.
- `INSTITUTO SAUDE E CIDADANIA - ISAC` (14702257003115): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/14702257003115) - status da consulta 429.
- `ITAU UNIBANCO S A` (60701190000104): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/60701190000104) - status da consulta 429.
- `AGENCIA DE ATRACAO DE INVESTIMENTOS ESTRATEGICOS DO PIAUI S/A` (44660105000142): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/44660105000142) - status da consulta 429.

### Investigacao complementar

- [SOCIEDADE BRASILEIRA CAMINHO DE DAMASCO - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=48211585004536+SOCIEDADE+BRASILEIRA+CAMINHO+DE+DAMASCO+Piaui+convenio+contrato+gestao)
- [ASSOCIACAO FILANTROPICA NOVA ESPERANCA - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=06058863000104+ASSOCIACAO+FILANTROPICA+NOVA+ESPERANCA+Piaui+convenio+contrato+gestao)
- [INSTITUTO SAUDE E CIDADANIA - ISAC - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=14702257003115+INSTITUTO+SAUDE+E+CIDADANIA+-+ISAC+Piaui+convenio+contrato+gestao)
- [ITAU UNIBANCO S A - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=60701190000104+ITAU+UNIBANCO+S+A+Piaui+convenio+contrato+gestao)
- [AGENCIA DE ATRACAO DE INVESTIMENTOS ESTRATEGICOS DO PIAUI S/A - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=44660105000142+AGENCIA+DE+ATRACAO+DE+INVESTIMENTOS+ESTRATEGICOS+DO+PIAUI+S%2FA+Piaui+convenio+contrato+gestao)

## Conclusao

Piaui deve ser lido como uma UF puxada por base mais distribuida. Se o objetivo for auditar volume financeiro, os principais focos sao as entidades lideres e os anos de pico. Se o objetivo for comparar com outras UFs, os melhores eixos sao quantidade de registros, ticket medio, concentracao e cobertura dos campos territoriais.
