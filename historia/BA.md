# Bahia (BA)

## Visao geral

Bahia soma 23.939 registros e R$ 7.855.301.612,25 em valor total. No ranking geral da base, a UF esta em 11o lugar por valor, 9o por quantidade de registros, 20o por ticket medio e 26o por concentracao dos 5 maiores beneficiarios.

O perfil dominante da UF e base mais distribuida. O ticket medio e de R$ 328.138,25, a mediana e de R$ 72.432,71 e os 5 maiores beneficiarios concentram 8,6% do valor total.

_Fonte local deste bloco: `processada/BA.parquet`; campos e agregacoes usados: `valor_total`, `nome_osc`, `cnpj`, `ano`, agregacoes por UF, ranks e shares dos maiores beneficiarios._

## Leitura narrativa

Comparando com o conjunto nacional, BA aparece entre as UFs lideres por valor em `PR, SP, PB, MS, SE`, por volume em `SE, PB, PR, MG, RS`, por ticket medio em `PE, RR, RJ, AM, AC` e por concentracao em `AC, RR, PR, CE, PE`.

Na pratica, isso indica que Bahia cresce principalmente por base mais distribuida. A participacao da UF no total nacional desta pasta e de 2,1%.

_Fonte local deste bloco: `processada/BA.parquet`; campos e agregacoes usados: benchmark nacional entre UFs, com comparacao de `valor_num`, `registros`, `ticket_medio` e `top5_share_pct`._

## Principais entidades

1. `10490525000106` - Instituto De Desenvolvimento Social Pela Musica - Idsm: R$ 193.115.317,50 em 8 registros.
2. `03037070000102` - Fundacao Luiz Eduardo Magalhaes: R$ 157.113.049,87 em 7 registros.
3. `40554834000163` - Instituto De Def.dos Direitos Humanos Doutor Jesus: R$ 144.292.018,76 em 8 registros.
4. `11020634000122` - Fundacao Estatal Saude Da Familia: R$ 99.196.782,27 em 1 registros.
5. `17955769000166` - Associacao  Amigos Do Teatro Castro Alves: R$ 82.093.989,48 em 5 registros.

_Fonte local deste bloco: `processada/BA.parquet`; campos e agregacoes usados: agrupamento por `nome_osc` e `cnpj`, soma de `valor_num` e contagem de registros._

## Gastos e objetivos

Termos mais frequentes nos objetos da UF: `2014, PLANO, COFINANCIAMENTO, ENTRE, CONV, ACAO, CELEBRADO, SEDES, MUNICIPIO, FMAS, TERMO, BAHIA`.

Registros de maior valor que ajudam a explicar os objetivos do gasto:

1. `Fundacao Estatal Saude Da Familia` - R$ 99.196.782,27 (ano 2023): Projeto Estadual de incentivo a Primeira Experiencia Profissional  Ocupacao Formal  Projeto Primeiro Emprego a Estudantes e egressos dos cursos tecnicos de nivel medioda Rede Estadual de Educacao Profissional e egressos do ensino medio e fundamental publico estadual qualificados por programas governamentais executados pelo Estado da Bahia e sem experiencia formal de trabalho na habilitacao cursada.
2. `Fundacao Luiz Eduardo Magalhaes` - R$ 87.824.370,68 (ano 2023): Projeto Estadual de incentivo a Primeira Experiencia Profissional  Ocupacao Formal  Projeto Primeiro Emprego a Estudantes e egressos dos cursos tecnicos de nivel medioda Rede Estadual de Educacao Profissional e egressos do ensino medio e fundamental publico estadual qualificados por programas governamentais executados pelo Estado da Bahia e sem experiencia formal de trabalho na habilitacao cursada.
3. `Instituto De Def.dos Direitos Humanos Doutor Jesus` - R$ 86.707.513,62 (ano 2023): TERMO DE FOMENTO No 005/2022 - CONSTITUI OBJETO DO PRESENTE TERMO DE FOMENTO, A EXECUCAO DO "PROJETO ARARAT VI" QUE VISA O ACOLHIMENTO DE ATE 1.000 (UM MIL) PESSOAS, DE AMBOS OS SEXOS, EM SITUACAO DE VULNERABILIDADE PESSOAL E SOCIAL, USUARIOS DE ALCOOL, CRACK E OUTRAS DROGAS, EM AMBIENTE FAVORAVEL, ORGANIZADO, PROMOVENDO A REINSERCAO SOCIAL, OCUPACIONAL, FAMILIAR E COMUNITARIA, CONFORME DETALHADO NO PLANO DE TRABALHO..
4. `Instituto De Desenvolvimento Social Pela Musica - Idsm` - R$ 62.412.965,87 (ano 2019): CONTRATO DE GESTAO No 029/2019 - CONSTITUI OBJETO DO PRESENTE CONTRATO A GESTAO DE NUCLEOS ESTADUAIS DE ORQUESTRAS JUVENIS E INFANTIS DA BAHIA-NEOJIBA,DE ACORDO COM AS ESPECIFICACOES E OBRIGACOES CONSTANTES DO EDITAL DE SELECAO,COM AS CONDICOES PREVISTAS NESTE CONTRATO E NA PROPOSTA DE TRABALHO APRESENTADA PELA CONTRATADA..
5. `Instituto De Desenvolvimento Social Pela Musica - Idsm` - R$ 61.072.531,07 (ano 2023): CONTRATO DE GESTAO No 029/2019 - CONSTITUI OBJETO DO PRESENTE CONTRATO A GESTAO DE NUCLEOS ESTADUAIS DE ORQUESTRAS JUVENIS E INFANTIS DA BAHIA-NEOJIBA,DE ACORDO COM AS ESPECIFICACOES E OBRIGACOES CONSTANTES DO EDITAL DE SELECAO,COM AS CONDICOES PREVISTAS NESTE CONTRATO E NA PROPOSTA DE TRABALHO APRESENTADA PELA CONTRATADA..

O maior registro individual da UF foi para `Fundacao Estatal Saude Da Familia` no valor de R$ 99.196.782,27. O objeto associado foi: Projeto Estadual de incentivo a Primeira Experiencia Profissional  Ocupacao Formal  Projeto Primeiro Emprego a Estudantes e egressos dos cursos tecnicos de nivel medioda Rede Estadual de Educacao Profissional e egressos do ensino medio e fundamental publico estadual qualificados por programas governamentais executados pelo Estado da Bahia e sem experiencia formal de trabalho na habilitacao cursada.

_Fonte local deste bloco: `processada/BA.parquet`; campos e agregacoes usados: campos `objeto`, `valor_total`, `ano`; selecao dos maiores registros por `valor_num`._

## Evolucao temporal

Anos de maior volume:

1. `2022` - R$ 1.951.170.851,54 em 2.274 registros.
2. `2023` - R$ 1.133.899.592,39 em 3.013 registros.
3. `2024` - R$ 948.941.455,52 em 2.040 registros.

Ultimos anos da serie:

- `2021`: R$ 409.840.938,61 em 818 registros, variacao n/d.
- `2022`: R$ 1.951.170.851,54 em 2.274 registros, variacao 376,1%.
- `2023`: R$ 1.133.899.592,39 em 3.013 registros, variacao -41,9%.
- `2024`: R$ 948.941.455,52 em 2.040 registros, variacao -16,3%.
- `2025`: R$ 402.497.306,08 em 1.827 registros, variacao -57,6%.

_Fonte local deste bloco: `processada/BA.parquet`; campos e agregacoes usados: agregacao anual por `ano_num`, soma de `valor_num`, contagem de registros e variacao percentual._

## Territorio e cobertura

Municipios com maior valor acumulado no recorte:

1. `SALVADOR` - R$ 1.673.063.140,72 em 3.168 registros.
2. `NAO INFORMADO` - R$ 421.701.452,00 em 1.157 registros.
3. `FEIRA DE SANTANA` - R$ 155.471.117,21 em 334 registros.
4. `CANDEIAS` - R$ 152.335.462,90 em 45 registros.
5. `BRASILIA` - R$ 144.810.982,26 em 55 registros.

Cobertura observada: CNPJ valido em 100,0%, municipio em 100,0%, objeto em 100,0% e modalidade em 0,0%. Ha 0 registros negativos e 1.025 registros marcados como duplicado aparente.

_Fonte local deste bloco: `processada/BA.parquet`; campos e agregacoes usados: campos `municipio`, `cod_municipio`, `objeto`, `modalidade`, `cnpj`, `duplicado_aparente`, `valor_negativo`._

## Fontes extras

### Dados locais

- Arquivo principal desta historia: `processada/BA.parquet`.
- Todas as afirmacoes sobre gasto, volume, anos, concentracao, objetivos e municipios foram derivadas desse parquet.

### Fontes externas verificadas por entidade

- [Consulta oficial de CNPJ (gov.br)](https://www.gov.br/pt-br/servicos/consultar-cadastro-nacional-de-pessoas-juridicas)
- [Comprovante de inscricao e situacao cadastral (Receita)](https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp)
- [Convenios e transferencias federais (gov.br / Transferegov)](https://www.gov.br/planejamento/pt-br/acesso-a-informacao/convenios-e-transparencias)

- `Instituto De Desenvolvimento Social Pela Musica - Idsm` (10490525000106): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/10490525000106) - situacao ATIVA; municipio/UF SALVADOR/BA; porte DEMAIS; atividade principal Atividades de organizacoes associativas ligadas a cultura e a arte.
- `Fundacao Luiz Eduardo Magalhaes` (03037070000102): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/03037070000102) - situacao ATIVA; municipio/UF SALVADOR/BA; porte DEMAIS; atividade principal Outras atividades de ensino nao especificadas anteriormente.
- `Instituto De Def.dos Direitos Humanos Doutor Jesus` (40554834000163): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/40554834000163) - situacao ATIVA; municipio/UF CANDEIAS/BA; porte DEMAIS; atividade principal Atividades de associacoes de defesa de direitos sociais.
- `Fundacao Estatal Saude Da Familia` (11020634000122): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/11020634000122) - situacao ATIVA; municipio/UF SALVADOR/BA; porte DEMAIS; atividade principal Regulacao das atividades de saude, educacao, servicos culturais e outros servicos sociais.
- `Associacao  Amigos Do Teatro Castro Alves` (17955769000166): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/17955769000166) - situacao ATIVA; municipio/UF SALVADOR/BA; porte DEMAIS; atividade principal Artes cenicas, espetaculos e atividades complementares nao especificadas anteriormente.

### Investigacao complementar

- [Instituto De Desenvolvimento Social Pela Musica - Idsm - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=10490525000106+Instituto+De+Desenvolvimento+Social+Pela+Musica+-+Idsm+Bahia+convenio+contrato+gestao)
- [Fundacao Luiz Eduardo Magalhaes - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=03037070000102+Fundacao+Luiz+Eduardo+Magalhaes+Bahia+convenio+contrato+gestao)
- [Instituto De Def.dos Direitos Humanos Doutor Jesus - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=40554834000163+Instituto+De+Def.dos+Direitos+Humanos+Doutor+Jesus+Bahia+convenio+contrato+gestao)
- [Fundacao Estatal Saude Da Familia - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=11020634000122+Fundacao+Estatal+Saude+Da+Familia+Bahia+convenio+contrato+gestao)
- [Associacao  Amigos Do Teatro Castro Alves - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=17955769000166+Associacao++Amigos+Do+Teatro+Castro+Alves+Bahia+convenio+contrato+gestao)

## Conclusao

Bahia deve ser lido como uma UF puxada por base mais distribuida. Se o objetivo for auditar volume financeiro, os principais focos sao as entidades lideres e os anos de pico. Se o objetivo for comparar com outras UFs, os melhores eixos sao quantidade de registros, ticket medio, concentracao e cobertura dos campos territoriais.
