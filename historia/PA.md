# Para (PA)

## Visao geral

Para soma 29.407 registros e R$ 5.960.040.896,02 em valor total. No ranking geral da base, a UF esta em 12o lugar por valor, 8o por quantidade de registros, 25o por ticket medio e 19o por concentracao dos 5 maiores beneficiarios.

O perfil dominante da UF e base mais distribuida. O ticket medio e de R$ 202.674,22, a mediana e de R$ 19.242,05 e os 5 maiores beneficiarios concentram 31,0% do valor total.

_Fonte local deste bloco: `processada/PA.parquet`; campos e agregacoes usados: `valor_total`, `nome_osc`, `cnpj`, `ano`, agregacoes por UF, ranks e shares dos maiores beneficiarios._

## Leitura narrativa

Comparando com o conjunto nacional, PA aparece entre as UFs lideres por valor em `PR, SP, PB, MS, SE`, por volume em `SE, PB, PR, MG, RS`, por ticket medio em `PE, RR, RJ, AM, AC` e por concentracao em `AC, RR, PR, CE, PE`.

Na pratica, isso indica que Para cresce principalmente por base mais distribuida. A participacao da UF no total nacional desta pasta e de 1,6%.

_Fonte local deste bloco: `processada/PA.parquet`; campos e agregacoes usados: benchmark nacional entre UFs, com comparacao de `valor_num`, `registros`, `ticket_medio` e `top5_share_pct`._

## Principais entidades

1. `04567897000190` - TRIBUNAL DE JUSTICA DO ESTADO DO PARA: R$ 1.005.324.224,60 em 9.390 registros.
2. `05320403000131` - HOSPITAL SANTO ANTONIO MARIA ZACARIA: R$ 430.665.150,24 em 1.041 registros.
3. `05055009000113` - PREFEITURA MUNICIPAL DE BELEM: R$ 144.454.049,72 em 844 registros.
4. `04873592000107` - PREFEITURA MUNICIPAL DE BRAGANCA: R$ 140.014.362,32 em 153 registros.
5. `05196530000170` - PREFEITURA MUNICIPAL DE TOME ACU: R$ 127.107.641,34 em 213 registros.

_Fonte local deste bloco: `processada/PA.parquet`; campos e agregacoes usados: agrupamento por `nome_osc` e `cnpj`, soma de `valor_num` e contagem de registros._

## Gastos e objetivos

Termos mais frequentes nos objetos da UF: `BELEM, SOCIAL, VULNERABILIDADE, CAPACITACAO, SITUACAO, OFICIO, AUTORIZADO, 2005, 0116, DIREITOS, AMBIENTE, MUSICA`.

Registros de maior valor que ajudam a explicar os objetivos do gasto:

1. `ASSOCIACAO DE LIGAS ESPORTIVAS DE CARAJAS` - R$ 2.450.000,00 (ano 2022): Implementacao e Desenvolvimento do Projeto ALCA - FOMENTO AO ESPORTE AMADOR no Municipio de Maraba/PA.
2. `INSTITUTO MARIA NEVES` - R$ 2.125.000,00 (ano 2025): Implementacao e Desenvolvimento do Projeto CRESCENDO JUNTOS, no Municipio de Belem/PA.
3. `INSTITUTO MARIA NEVES` - R$ 2.000.000,00 (ano 2025): Implementacao e Desenvolvimento do Projeto CRESCENDO JUNTOS, no Municipio de Belem/PA.
4. `ASSOCIACAO DE LIGAS ESPORTIVAS DE CARAJAS` - R$ 1.599.897,55 (ano 2025): Implementacao e Desenvolvimento do Projeto ALCA - FOMENTO AO ESPORTE AMADOR no Municipio de Maraba/PA.
5. `ASSOCIACAO CULTURAL AMAZONIA INDEPENDENTE` - R$ 1.500.000,00 (ano 2021): Realizar a nona edicao do Festival Se Rasgum..

O maior registro individual da UF foi para `TRIBUNAL DE JUSTICA DO ESTADO DO PARA` no valor de R$ 60.068.002,81. O objeto associado foi: .

_Fonte local deste bloco: `processada/PA.parquet`; campos e agregacoes usados: campos `objeto`, `valor_total`, `ano`; selecao dos maiores registros por `valor_num`._

## Evolucao temporal

Anos de maior volume:

1. `2025` - R$ 1.248.630.946,37 em 5.085 registros.
2. `2024` - R$ 1.006.207.094,95 em 4.075 registros.
3. `2023` - R$ 996.793.918,29 em 4.102 registros.

Ultimos anos da serie:

- `2022`: R$ 931.321.231,93 em 3.279 registros, variacao n/d.
- `2023`: R$ 996.793.918,29 em 4.102 registros, variacao 7,0%.
- `2024`: R$ 1.006.207.094,95 em 4.075 registros, variacao 0,9%.
- `2025`: R$ 1.248.630.946,37 em 5.085 registros, variacao 24,1%.
- `2026`: R$ 50.081.418,54 em 515 registros, variacao -96,0%.

_Fonte local deste bloco: `processada/PA.parquet`; campos e agregacoes usados: agregacao anual por `ano_num`, soma de `valor_num`, contagem de registros e variacao percentual._

## Territorio e cobertura

Municipios com maior valor acumulado no recorte:

1. `BELEM` - R$ 1.279.107.304,58 em 10.967 registros.
2. `BRAGANCA` - R$ 571.924.586,51 em 1.314 registros.
3. `TOME-ACU` - R$ 127.107.641,34 em 213 registros.
4. `ANANINDEUA` - R$ 124.141.228,69 em 560 registros.
5. `ABAETETUBA` - R$ 120.163.069,57 em 143 registros.

Cobertura observada: CNPJ valido em 100,0%, municipio em 98,5%, objeto em 1,0% e modalidade em 2,7%. Ha 0 registros negativos e 8.452 registros marcados como duplicado aparente.

_Fonte local deste bloco: `processada/PA.parquet`; campos e agregacoes usados: campos `municipio`, `cod_municipio`, `objeto`, `modalidade`, `cnpj`, `duplicado_aparente`, `valor_negativo`._

## Fontes extras

### Dados locais

- Arquivo principal desta historia: `processada/PA.parquet`.
- Todas as afirmacoes sobre gasto, volume, anos, concentracao, objetivos e municipios foram derivadas desse parquet.

### Fontes externas verificadas por entidade

- [Consulta oficial de CNPJ (gov.br)](https://www.gov.br/pt-br/servicos/consultar-cadastro-nacional-de-pessoas-juridicas)
- [Comprovante de inscricao e situacao cadastral (Receita)](https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp)
- [Convenios e transferencias federais (gov.br / Transferegov)](https://www.gov.br/planejamento/pt-br/acesso-a-informacao/convenios-e-transparencias)

- `TRIBUNAL DE JUSTICA DO ESTADO DO PARA` (04567897000190): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/04567897000190) - status da consulta 429.
- `HOSPITAL SANTO ANTONIO MARIA ZACARIA` (05320403000131): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/05320403000131) - status da consulta 429.
- `PREFEITURA MUNICIPAL DE BELEM` (05055009000113): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/05055009000113) - status da consulta 429.
- `PREFEITURA MUNICIPAL DE BRAGANCA` (04873592000107): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/04873592000107) - status da consulta 429.
- `PREFEITURA MUNICIPAL DE TOME ACU` (05196530000170): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/05196530000170) - status da consulta 429.

### Investigacao complementar

- [TRIBUNAL DE JUSTICA DO ESTADO DO PARA - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=04567897000190+TRIBUNAL+DE+JUSTICA+DO+ESTADO+DO+PARA+Para+convenio+contrato+gestao)
- [HOSPITAL SANTO ANTONIO MARIA ZACARIA - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=05320403000131+HOSPITAL+SANTO+ANTONIO+MARIA+ZACARIA+Para+convenio+contrato+gestao)
- [PREFEITURA MUNICIPAL DE BELEM - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=05055009000113+PREFEITURA+MUNICIPAL+DE+BELEM+Para+convenio+contrato+gestao)
- [PREFEITURA MUNICIPAL DE BRAGANCA - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=04873592000107+PREFEITURA+MUNICIPAL+DE+BRAGANCA+Para+convenio+contrato+gestao)
- [PREFEITURA MUNICIPAL DE TOME ACU - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=05196530000170+PREFEITURA+MUNICIPAL+DE+TOME+ACU+Para+convenio+contrato+gestao)

## Conclusao

Para deve ser lido como uma UF puxada por base mais distribuida. Se o objetivo for auditar volume financeiro, os principais focos sao as entidades lideres e os anos de pico. Se o objetivo for comparar com outras UFs, os melhores eixos sao quantidade de registros, ticket medio, concentracao e cobertura dos campos territoriais.
