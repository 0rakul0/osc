# Alagoas (AL)

## Visao geral

Alagoas soma 1.323 registros e R$ 2.416.091.056,98 em valor total. No ranking geral da base, a UF esta em 15o lugar por valor, 21o por quantidade de registros, 6o por ticket medio e 13o por concentracao dos 5 maiores beneficiarios.

O perfil dominante da UF e ticket medio. O ticket medio e de R$ 1.826.221,51, a mediana e de R$ 269.808,00 e os 5 maiores beneficiarios concentram 37,1% do valor total.

_Fonte local deste bloco: `processada/AL.parquet`; campos e agregacoes usados: `valor_total`, `nome_osc`, `cnpj`, `ano`, agregacoes por UF, ranks e shares dos maiores beneficiarios._

## Leitura narrativa

Comparando com o conjunto nacional, AL aparece entre as UFs lideres por valor em `PR, SP, PB, MS, SE`, por volume em `SE, PB, PR, MG, RS`, por ticket medio em `PE, RR, RJ, AM, AC` e por concentracao em `AC, RR, PR, CE, PE`.

Na pratica, isso indica que Alagoas cresce principalmente por ticket medio. A participacao da UF no total nacional desta pasta e de 0,7%.

_Fonte local deste bloco: `processada/AL.parquet`; campos e agregacoes usados: benchmark nacional entre UFs, com comparacao de `valor_num`, `registros`, `ticket_medio` e `top5_share_pct`._

## Principais entidades

1. `12272753000135` - C ENGENHARIA S/N: R$ 244.925.273,84 em 3 registros.
2. `12224895000127` - PREF MUNI DELMIRO GOUVEIA: R$ 202.489.217,21 em 11 registros.
3. `12264222000109` - PREF MUNI SAO MIGUEL DOS CAMPOS: R$ 201.337.698,82 em 8 registros.
4. `09191464000105` - EQUIPAV ENGENHARIA LTDA: R$ 128.647.395,34 em 1 registros.
5. `01543722000155` - S.V.C.-CONSTRUCOES LTDA: R$ 118.831.430,10 em 3 registros.

_Fonte local deste bloco: `processada/AL.parquet`; campos e agregacoes usados: agrupamento por `nome_osc` e `cnpj`, soma de `valor_num` e contagem de registros._

## Gastos e objetivos

Termos mais frequentes nos objetos da UF: `PUBLICADO, 2022, VISANDO, REDE, TRANSPORTE, ALUNOS, PORTARIA, ENSINO, TERMO, 2023, GEITE, CONFORME`.

Registros de maior valor que ajudam a explicar os objetivos do gasto:

1. `PREF MUNI SAO MIGUEL DOS CAMPOS` - R$ 154.188.087,73 (ano 2022): Implantacao de Pavimentacao, Drenagem e Sistema de Esgotamento Sanitario e Rede de Abastecimento de Agua nos Conjuntos Habitacionais Helio Jatoba, I, II E III, no Municipio de Sao Miguel dos Campos/AL.
2. `EQUIPAV ENGENHARIA LTDA` - R$ 128.647.395,34 (ano 2014): OBRAS E SERVICOS DE ESTRADA PARQUE ROTA ECOLOGICA INTERVENCOES QUE COMPREENDEM A RESTAURACAO E IMPLANTACAO DE MELHORIAS RODOVIARIAS DA AL-101 NORTE,UMA EXTENCAO DE 23,56 KM,MELHORIAS E AMPLIACAO DO SI.
3. `C ENGENHARIA S/N` - R$ 96.011.345,80 (ano 2002): 39 MEDICAO REVITALIZACAO DO COMPLEXO ESTUARINO-LAGUNAR MUNDAU/MANGUABA - SISTEMAS DE ESGOTAMENTO SANITARIO, 5 TA. 5. MEDICAO DO CONVENIO N. 1799/2002 MIN. SAUDE POR MEIO DA FUND NACIONAL DE SAUDE. DOE.
4. `C ENGENHARIA S/N` - R$ 96.011.345,80 (ano 2002): 41. MEDICAO DOS SERVICOS REALIZADOS NAS OBRAS DE REVITALIZACAODO COMPLEXO ESTUARINO-LAGUNAR MUNDAU/MANGUABA - SIST ESG. SANITARIO. 6 TA. CONVENIO N. 1971/2005 MIN. DA SAUDE POR MEIO DA FUND. NACIONAL.
5. `PREF MUNI DELMIRO GOUVEIA` - R$ 82.210.115,64 (ano 2022): Implantacao e Recapeamento do Trecho: Entr. AL-220/Mirante do Talhado/Povoado Araca/Povoado Malhadas/Povoado Lameirao/Distrito Lagoinha/Povoado Monte Escuro/Povoado Cruz/Povoado Salgado, localizados.

O maior registro individual da UF foi para `PREF MUNI SAO MIGUEL DOS CAMPOS` no valor de R$ 154.188.087,73. O objeto associado foi: Implantacao de Pavimentacao, Drenagem e Sistema de Esgotamento Sanitario e Rede de Abastecimento de Agua nos Conjuntos Habitacionais Helio Jatoba, I, II E III, no Municipio de Sao Miguel dos Campos/AL.

_Fonte local deste bloco: `processada/AL.parquet`; campos e agregacoes usados: campos `objeto`, `valor_total`, `ano`; selecao dos maiores registros por `valor_num`._

## Evolucao temporal

Anos de maior volume:

1. `2022` - R$ 819.784.519,33 em 300 registros.
2. `2014` - R$ 322.867.261,78 em 44 registros.
3. `2002` - R$ 313.301.058,99 em 9 registros.

Ultimos anos da serie:

- `2019`: R$ 23.343.879,41 em 66 registros, variacao n/d.
- `2020`: R$ 23.170.734,31 em 14 registros, variacao -0,7%.
- `2021`: R$ 128.355.356,18 em 231 registros, variacao 454,0%.
- `2022`: R$ 819.784.519,33 em 300 registros, variacao 538,7%.
- `2023`: R$ 126.236.204,85 em 177 registros, variacao -84,6%.

_Fonte local deste bloco: `processada/AL.parquet`; campos e agregacoes usados: agregacao anual por `ano_num`, soma de `valor_num`, contagem de registros e variacao percentual._

## Territorio e cobertura

A base desta UF nao traz cobertura territorial suficiente para destacar municipios com seguranca.

Cobertura observada: CNPJ valido em 100,0%, municipio em 1,7%, objeto em 100,0% e modalidade em 100,0%. Ha 0 registros negativos e 32 registros marcados como duplicado aparente.

_Fonte local deste bloco: `processada/AL.parquet`; campos e agregacoes usados: campos `municipio`, `cod_municipio`, `objeto`, `modalidade`, `cnpj`, `duplicado_aparente`, `valor_negativo`._

## Fontes extras

### Dados locais

- Arquivo principal desta historia: `processada/AL.parquet`.
- Todas as afirmacoes sobre gasto, volume, anos, concentracao, objetivos e municipios foram derivadas desse parquet.

### Fontes externas verificadas por entidade

- [Consulta oficial de CNPJ (gov.br)](https://www.gov.br/pt-br/servicos/consultar-cadastro-nacional-de-pessoas-juridicas)
- [Comprovante de inscricao e situacao cadastral (Receita)](https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp)
- [Convenios e transferencias federais (gov.br / Transferegov)](https://www.gov.br/planejamento/pt-br/acesso-a-informacao/convenios-e-transparencias)

- `C ENGENHARIA S/N` (12272753000135): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/12272753000135) - situacao ATIVA; municipio/UF MACEIO/AL; porte DEMAIS; atividade principal Construcao de edificios.
- `PREF MUNI DELMIRO GOUVEIA` (12224895000127): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/12224895000127) - situacao ATIVA; municipio/UF DELMIRO GOUVEIA/AL; porte DEMAIS; atividade principal Administracao publica em geral.
- `PREF MUNI SAO MIGUEL DOS CAMPOS` (12264222000109): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/12264222000109) - situacao ATIVA; municipio/UF SAO MIGUEL DOS CAMPOS/AL; porte DEMAIS; atividade principal Administracao publica em geral.
- `EQUIPAV ENGENHARIA LTDA` (09191464000105): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/09191464000105) - situacao ATIVA; municipio/UF SAO PAULO/SP; porte DEMAIS; atividade principal Construcao de rodovias e ferrovias.
- `S.V.C.-CONSTRUCOES LTDA` (01543722000155): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/01543722000155) - situacao ATIVA; municipio/UF SALVADOR/BA; porte DEMAIS; atividade principal Construcao de rodovias e ferrovias.

### Investigacao complementar

- [C ENGENHARIA S/N - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=12272753000135+C+ENGENHARIA+S%2FN+Alagoas+convenio+contrato+gestao)
- [PREF MUNI DELMIRO GOUVEIA - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=12224895000127+PREF+MUNI+DELMIRO+GOUVEIA+Alagoas+convenio+contrato+gestao)
- [PREF MUNI SAO MIGUEL DOS CAMPOS - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=12264222000109+PREF+MUNI+SAO+MIGUEL+DOS+CAMPOS+Alagoas+convenio+contrato+gestao)
- [EQUIPAV ENGENHARIA LTDA - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=09191464000105+EQUIPAV+ENGENHARIA+LTDA+Alagoas+convenio+contrato+gestao)
- [S.V.C.-CONSTRUCOES LTDA - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=01543722000155+S.V.C.-CONSTRUCOES+LTDA+Alagoas+convenio+contrato+gestao)

## Conclusao

Alagoas deve ser lido como uma UF puxada por ticket medio. Se o objetivo for auditar volume financeiro, os principais focos sao as entidades lideres e os anos de pico. Se o objetivo for comparar com outras UFs, os melhores eixos sao quantidade de registros, ticket medio, concentracao e cobertura dos campos territoriais.
