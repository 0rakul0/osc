# Ceara (CE)

## Visao geral

Ceara soma 5.823 registros e R$ 1.526.046.673,75 em valor total. No ranking geral da base, a UF esta em 19o lugar por valor, 11o por quantidade de registros, 22o por ticket medio e 4o por concentracao dos 5 maiores beneficiarios.

O perfil dominante da UF e concentracao. O ticket medio e de R$ 262.072,24, a mediana e de R$ 87.500,00 e os 5 maiores beneficiarios concentram 82,4% do valor total.

_Fonte local deste bloco: `processada/CE.parquet`; campos e agregacoes usados: `valor_total`, `nome_osc`, `cnpj`, `ano`, agregacoes por UF, ranks e shares dos maiores beneficiarios._

## Leitura narrativa

Comparando com o conjunto nacional, CE aparece entre as UFs lideres por valor em `PR, SP, PB, MS, SE`, por volume em `SE, PB, PR, MG, RS`, por ticket medio em `PE, RR, RJ, AM, AC` e por concentracao em `AC, RR, PR, CE, PE`.

Na pratica, isso indica que Ceara cresce principalmente por concentracao. A participacao da UF no total nacional desta pasta e de 0,4%.

_Fonte local deste bloco: `processada/CE.parquet`; campos e agregacoes usados: benchmark nacional entre UFs, com comparacao de `valor_num`, `registros`, `ticket_medio` e `top5_share_pct`._

## Principais entidades

1. `03021597000149` - INSTITUTO CENTRO DE ENSINO TECNOLOGICO: R$ 630.217.412,76 em 1.531 registros.
2. `02455125000131` - INSTITUTO  DRAGAO DO MAR: R$ 211.178.369,87 em 566 registros.
3. `04867567000110` - INSTITUTO AGROPOLOS DO CEARA: R$ 181.608.594,56 em 1.091 registros.
4. `02533538000197` - INSTITUTO DE DESENVOLVIMENTO DO TRABALHO - IDT: R$ 138.469.484,00 em 326 registros.
5. `04867567000110` - INSTITUTO AGROPOLOS DO CEARA: R$ 95.977.356,02 em 635 registros.

_Fonte local deste bloco: `processada/CE.parquet`; campos e agregacoes usados: agrupamento por `nome_osc` e `cnpj`, soma de `valor_num` e contagem de registros._

## Gastos e objetivos

Termos mais frequentes nos objetos da UF: `CONTRATO, MEIO, EXECUTADO, GESTAO, PROFISSIONAL, SOCIAL, MANUTENCAO, CAPACITACAO, ACOES, NIVEL, ATENDIMENTO, ADOLESCENTES`.

Registros de maior valor que ajudam a explicar os objetivos do gasto:

1. `INSTITUTO CENTRO DE ENSINO TECNOLOGICO` - R$ 38.819.957,18 (ano 2022): Contratacao e Capacitacao de Professores para Escolas de Ensino Medio Integrado a Educacao Profissional Executado por meio de Contrato de Gestao..
2. `INSTITUTO CENTRO DE ENSINO TECNOLOGICO` - R$ 14.051.738,66 (ano 2025): Contratacao e Capacitacao de Professores para Escolas de Ensino Medio Integrado a Educacao Profissional Executado por meio de Contrato de Gestao..
3. `INSTITUTO CENTRO DE ENSINO TECNOLOGICO` - R$ 14.051.738,66 (ano 2025): Contratacao e Capacitacao de Professores para Escolas de Ensino Medio Integrado a Educacao Profissional Executado por meio de Contrato de Gestao..
4. `INSTITUTO CENTRO DE ENSINO TECNOLOGICO` - R$ 13.956.828,31 (ano 2022): Contratacao e Capacitacao de Professores para Escolas de Ensino Medio Integrado a Educacao Profissional Executado por meio de Contrato de Gestao..
5. `INSTITUTO CENTRO DE ENSINO TECNOLOGICO` - R$ 13.686.213,56 (ano 2024): Contratacao e Capacitacao de Professores para Escolas de Ensino Medio Integrado a Educacao Profissional Executado por meio de Contrato de Gestao..

O maior registro individual da UF foi para `INSTITUTO CENTRO DE ENSINO TECNOLOGICO` no valor de R$ 38.819.957,18. O objeto associado foi: Contratacao e Capacitacao de Professores para Escolas de Ensino Medio Integrado a Educacao Profissional Executado por meio de Contrato de Gestao..

_Fonte local deste bloco: `processada/CE.parquet`; campos e agregacoes usados: campos `objeto`, `valor_total`, `ano`; selecao dos maiores registros por `valor_num`._

## Evolucao temporal

Anos de maior volume:

1. `2022` - R$ 213.685.357,90 em 506 registros.
2. `2025` - R$ 202.936.906,34 em 479 registros.
3. `2021` - R$ 155.298.326,30 em 717 registros.

Ultimos anos da serie:

- `2021`: R$ 155.298.326,30 em 717 registros, variacao n/d.
- `2022`: R$ 213.685.357,90 em 506 registros, variacao 37,6%.
- `2023`: R$ 79.604.734,87 em 302 registros, variacao -62,7%.
- `2024`: R$ 105.450.285,18 em 445 registros, variacao 32,5%.
- `2025`: R$ 202.936.906,34 em 479 registros, variacao 92,4%.

_Fonte local deste bloco: `processada/CE.parquet`; campos e agregacoes usados: agregacao anual por `ano_num`, soma de `valor_num`, contagem de registros e variacao percentual._

## Territorio e cobertura

Municipios com maior valor acumulado no recorte:

1. `FORTALEZA` - R$ 1.483.612.933,07 em 5.539 registros.
2. `CRATO` - R$ 11.004.048,78 em 15 registros.
3. `JUAZEIRO DO NORTE` - R$ 7.205.404,76 em 39 registros.
4. `MARACANAU` - R$ 6.463.418,22 em 66 registros.
5. `CAUCAIA` - R$ 4.481.381,20 em 22 registros.

Cobertura observada: CNPJ valido em 100,0%, municipio em 100,0%, objeto em 100,0% e modalidade em 77,5%. Ha 0 registros negativos e 2.349 registros marcados como duplicado aparente.

_Fonte local deste bloco: `processada/CE.parquet`; campos e agregacoes usados: campos `municipio`, `cod_municipio`, `objeto`, `modalidade`, `cnpj`, `duplicado_aparente`, `valor_negativo`._

## Fontes extras

### Dados locais

- Arquivo principal desta historia: `processada/CE.parquet`.
- Todas as afirmacoes sobre gasto, volume, anos, concentracao, objetivos e municipios foram derivadas desse parquet.

### Fontes externas verificadas por entidade

- [Consulta oficial de CNPJ (gov.br)](https://www.gov.br/pt-br/servicos/consultar-cadastro-nacional-de-pessoas-juridicas)
- [Comprovante de inscricao e situacao cadastral (Receita)](https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp)
- [Convenios e transferencias federais (gov.br / Transferegov)](https://www.gov.br/planejamento/pt-br/acesso-a-informacao/convenios-e-transparencias)

- `INSTITUTO CENTRO DE ENSINO TECNOLOGICO` (03021597000149): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/03021597000149) - situacao ATIVA; municipio/UF FORTALEZA/CE; porte DEMAIS; atividade principal Educacao profissional de nivel tecnologico.
- `INSTITUTO  DRAGAO DO MAR` (02455125000131): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/02455125000131) - situacao ATIVA; municipio/UF FORTALEZA/CE; porte DEMAIS; atividade principal Atividades de associacoes de defesa de direitos sociais.
- `INSTITUTO AGROPOLOS DO CEARA` (04867567000110): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/04867567000110) - situacao ATIVA; municipio/UF FORTALEZA/CE; porte DEMAIS; atividade principal Atividades associativas nao especificadas anteriormente.
- `INSTITUTO DE DESENVOLVIMENTO DO TRABALHO - IDT` (02533538000197): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/02533538000197) - situacao ATIVA; municipio/UF FORTALEZA/CE; porte DEMAIS; atividade principal Atividades de intermediacao e agenciamento de servicos e negocios em geral, exceto imobiliarios.
- `INSTITUTO AGROPOLOS DO CEARA` (04867567000110): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/04867567000110) - situacao ATIVA; municipio/UF FORTALEZA/CE; porte DEMAIS; atividade principal Atividades associativas nao especificadas anteriormente.

### Investigacao complementar

- [INSTITUTO CENTRO DE ENSINO TECNOLOGICO - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=03021597000149+INSTITUTO+CENTRO+DE+ENSINO+TECNOLOGICO+Ceara+convenio+contrato+gestao)
- [INSTITUTO  DRAGAO DO MAR - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=02455125000131+INSTITUTO++DRAGAO+DO+MAR+Ceara+convenio+contrato+gestao)
- [INSTITUTO AGROPOLOS DO CEARA - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=04867567000110+INSTITUTO+AGROPOLOS+DO+CEARA+Ceara+convenio+contrato+gestao)
- [INSTITUTO DE DESENVOLVIMENTO DO TRABALHO - IDT - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=02533538000197+INSTITUTO+DE+DESENVOLVIMENTO+DO+TRABALHO+-+IDT+Ceara+convenio+contrato+gestao)
- [INSTITUTO AGROPOLOS DO CEARA - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=04867567000110+INSTITUTO+AGROPOLOS+DO+CEARA+Ceara+convenio+contrato+gestao)

## Conclusao

Ceara deve ser lido como uma UF puxada por concentracao. Se o objetivo for auditar volume financeiro, os principais focos sao as entidades lideres e os anos de pico. Se o objetivo for comparar com outras UFs, os melhores eixos sao quantidade de registros, ticket medio, concentracao e cobertura dos campos territoriais.
