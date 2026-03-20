# Rio Grande do Sul (RS)

## Visao geral

Rio Grande do Sul soma 49.724 registros e R$ 10.184.140.221,37 em valor total. No ranking geral da base, a UF esta em 10o lugar por valor, 5o por quantidade de registros, 24o por ticket medio e 12o por concentracao dos 5 maiores beneficiarios.

O perfil dominante da UF e volume de dados. O ticket medio e de R$ 204.813,37, a mediana e de R$ 13.500,00 e os 5 maiores beneficiarios concentram 38,2% do valor total.

_Fonte local deste bloco: `processada/RS.parquet`; campos e agregacoes usados: `valor_total`, `nome_osc`, `cnpj`, `ano`, agregacoes por UF, ranks e shares dos maiores beneficiarios._

## Leitura narrativa

Comparando com o conjunto nacional, RS aparece entre as UFs lideres por valor em `PR, SP, PB, MS, SE`, por volume em `SE, PB, PR, MG, RS`, por ticket medio em `PE, RR, RJ, AM, AC` e por concentracao em `AC, RR, PR, CE, PE`.

Na pratica, isso indica que Rio Grande do Sul cresce principalmente por volume de dados. A participacao da UF no total nacional desta pasta e de 2,8%.

_Fonte local deste bloco: `processada/RS.parquet`; campos e agregacoes usados: benchmark nacional entre UFs, com comparacao de `valor_num`, `registros`, `ticket_medio` e `top5_share_pct`._

## Principais entidades

1. `89161475000173` - ASSOC RIOGRANDENSE EMPR ASS TEC EXT RURAL: R$ 1.935.262.685,90 em 31 registros.
2. `88648761001843` - FUND UNIVERSIDADE DE CAXIAS DO SUL: R$ 601.917.339,34 em 24 registros.
3. `92898550000864` - FUND UNIVERSITARIA DE CARDIOLOGIA EM REC JUD: R$ 250.448.410,70 em 13 registros.
4. `87958583000146` - ESTADO DO RGS SECRETARIA DA SEGURANCA PUBLICA: R$ 237.240.394,19 em 124 registros.
5. `88648761000103` - FUND UNIVERSIDADE DE CAXIAS DO SUL: R$ 225.923.604,21 em 100 registros.

_Fonte local deste bloco: `processada/RS.parquet`; campos e agregacoes usados: agrupamento por `nome_osc` e `cnpj`, soma de `valor_num` e contagem de registros._

## Gastos e objetivos

Termos mais frequentes nos objetos da UF: `TRANSITO, MUNICIPIO, X0096, SERVICOS, PRESENTE, SOCIAL, FISCALIZACAO, CONVENIO, COMO, CARATER, CONTINUADO, ANIMAL`.

Registros de maior valor que ajudam a explicar os objetivos do gasto:

1. `ASSOC RIOGRANDENSE EMPR ASS TEC EXT RURAL` - R$ 722.806.251,16 (ano 2011): Cooperacao, integracao e complementacao de esforcos entre o Estado e a EMATER/RS, visando promover o desenvolvimento rural, conjulgando melhoria de renda, qualificacao tecnologica e sustentabilidade social e ambiental, atreves da Assistencia Tecnica e Extensao Rural..
2. `ASSOC RIOGRANDENSE EMPR ASS TEC EXT RURAL` - R$ 704.900.000,00 (ano 2015): Cooperacao, integracao e complementacao de esforcos entre o Estado e a EMATER/RS, visando promover o desenvolvimento rural, conjulgando melhoria de renda, qualificacao tecnologica e sustentabilidade social e ambiental, atreves da Assistencia Tecnica e Extensao Rural..
3. `FUND UNIVERSIDADE DE CAXIAS DO SUL` - R$ 376.608.091,80 (ano 2020): Viabilizar o funcionamento do Hospital Geral de Caxias do Sul..
4. `FUND UNIVERSITARIA DE CARDIOLOGIA EM REC JUD` - R$ 231.836.494,61 (ano 2020): A finalidade do presente Convenio e a uniao de esforcos entre os participes para a realizacao de acoes necessarias para a manutencao do atendimento ambulatorial e adequacoes fisicas e estruturais necessarias a implantacao gradativa da parte hospitalar do HOSPITAL REGIONAL DE SANTA MARIA, com sede na Rua Florianopolis, sem numero, Parque Pinheiro Machado, Vila Rossi, no Municipio de Santa Maria/RS, com escopo de dar continuidade a ESTRUTURACAO, OPERACIONALIZACAO, ADMINISTRACAO E FUNCIONAMENTO do HOSPITAL, com vista a ampliacao da assistencia a saude, atraves do atendimento hospitalar, somente a usuarios do SUS, em conformidade com o Plano de Trabalho aprovado e constante no processo administr.
5. `FUND UNIVERSIDADE DE CAXIAS DO SUL` - R$ 180.438.274,00 (ano 2015): O presente Convenio tem por objeto a uniao de esforcos entre os participes, para viabilizar o funcionamento do Hospital Geral de Caxias do Sul, a fim de manter os servicos prestados ao SUS, de acordo com o Plano de Trabalho constante do expediente no 072750-20.00/15.1, independentemente de transcricao..

O maior registro individual da UF foi para `ASSOC RIOGRANDENSE EMPR ASS TEC EXT RURAL` no valor de R$ 722.806.251,16. O objeto associado foi: Cooperacao, integracao e complementacao de esforcos entre o Estado e a EMATER/RS, visando promover o desenvolvimento rural, conjulgando melhoria de renda, qualificacao tecnologica e sustentabilidade social e ambiental, atreves da Assistencia Tecnica e Extensao Rural..

_Fonte local deste bloco: `processada/RS.parquet`; campos e agregacoes usados: campos `objeto`, `valor_total`, `ano`; selecao dos maiores registros por `valor_num`._

## Evolucao temporal

Anos de maior volume:

1. `2015` - R$ 953.062.421,11 em 1.757 registros.
2. `2020` - R$ 883.363.813,88 em 2.302 registros.
3. `2011` - R$ 864.554.363,09 em 1.984 registros.

Ultimos anos da serie:

- `2021`: R$ 785.993.969,59 em 2.557 registros, variacao n/d.
- `2022`: R$ 784.957.029,60 em 3.511 registros, variacao -0,1%.
- `2023`: R$ 665.663.585,50 em 3.163 registros, variacao -15,2%.
- `2024`: R$ 768.685.087,41 em 2.423 registros, variacao 15,5%.
- `2025`: R$ 358.793.118,79 em 1.079 registros, variacao -53,3%.

_Fonte local deste bloco: `processada/RS.parquet`; campos e agregacoes usados: agregacao anual por `ano_num`, soma de `valor_num`, contagem de registros e variacao percentual._

## Territorio e cobertura

Municipios com maior valor acumulado no recorte:

1. `PORTO ALEGRE` - R$ 3.317.002.078,63 em 2.468 registros.
2. `CAXIAS DO SUL` - R$ 905.552.341,13 em 504 registros.
3. `SANTA MARIA` - R$ 339.682.780,12 em 381 registros.
4. `PASSO FUNDO` - R$ 244.294.490,45 em 330 registros.
5. `ALVORADA` - R$ 181.941.784,79 em 117 registros.

Cobertura observada: CNPJ valido em 100,0%, municipio em 100,0%, objeto em 100,0% e modalidade em 100,0%. Ha 0 registros negativos e 71 registros marcados como duplicado aparente.

_Fonte local deste bloco: `processada/RS.parquet`; campos e agregacoes usados: campos `municipio`, `cod_municipio`, `objeto`, `modalidade`, `cnpj`, `duplicado_aparente`, `valor_negativo`._

## Fontes extras

### Dados locais

- Arquivo principal desta historia: `processada/RS.parquet`.
- Todas as afirmacoes sobre gasto, volume, anos, concentracao, objetivos e municipios foram derivadas desse parquet.

### Fontes externas verificadas por entidade

- [Consulta oficial de CNPJ (gov.br)](https://www.gov.br/pt-br/servicos/consultar-cadastro-nacional-de-pessoas-juridicas)
- [Comprovante de inscricao e situacao cadastral (Receita)](https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp)
- [Convenios e transferencias federais (gov.br / Transferegov)](https://www.gov.br/planejamento/pt-br/acesso-a-informacao/convenios-e-transparencias)

- `ASSOC RIOGRANDENSE EMPR ASS TEC EXT RURAL` (89161475000173): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/89161475000173) - situacao ATIVA; municipio/UF PORTO ALEGRE/RS; porte DEMAIS; atividade principal Atividades de associacoes de defesa de direitos sociais.
- `FUND UNIVERSIDADE DE CAXIAS DO SUL` (88648761001843): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/88648761001843) - situacao ATIVA; municipio/UF CAXIAS DO SUL/RS; porte DEMAIS; atividade principal Atividades de atendimento hospitalar, exceto pronto-socorro e unidades para atendimento a urgencias.
- `FUND UNIVERSITARIA DE CARDIOLOGIA EM REC JUD` (92898550000864): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/92898550000864) - situacao ATIVA; municipio/UF SANTA MARIA/RS; porte DEMAIS; atividade principal Atividades de atendimento hospitalar, exceto pronto-socorro e unidades para atendimento a urgencias.
- `ESTADO DO RGS SECRETARIA DA SEGURANCA PUBLICA` (87958583000146): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/87958583000146) - situacao ATIVA; municipio/UF PORTO ALEGRE/RS; porte DEMAIS; atividade principal Administracao publica em geral.
- `FUND UNIVERSIDADE DE CAXIAS DO SUL` (88648761000103): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/88648761000103) - situacao ATIVA; municipio/UF CAXIAS DO SUL/RS; porte DEMAIS; atividade principal Educacao superior - graduacao.

### Investigacao complementar

- [ASSOC RIOGRANDENSE EMPR ASS TEC EXT RURAL - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=89161475000173+ASSOC+RIOGRANDENSE+EMPR+ASS+TEC+EXT+RURAL+Rio+Grande+do+Sul+convenio+contrato+gestao)
- [FUND UNIVERSIDADE DE CAXIAS DO SUL - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=88648761001843+FUND+UNIVERSIDADE+DE+CAXIAS+DO+SUL+Rio+Grande+do+Sul+convenio+contrato+gestao)
- [FUND UNIVERSITARIA DE CARDIOLOGIA EM REC JUD - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=92898550000864+FUND+UNIVERSITARIA+DE+CARDIOLOGIA+EM+REC+JUD+Rio+Grande+do+Sul+convenio+contrato+gestao)
- [ESTADO DO RGS SECRETARIA DA SEGURANCA PUBLICA - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=87958583000146+ESTADO+DO+RGS+SECRETARIA+DA+SEGURANCA+PUBLICA+Rio+Grande+do+Sul+convenio+contrato+gestao)
- [FUND UNIVERSIDADE DE CAXIAS DO SUL - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=88648761000103+FUND+UNIVERSIDADE+DE+CAXIAS+DO+SUL+Rio+Grande+do+Sul+convenio+contrato+gestao)

## Conclusao

Rio Grande do Sul deve ser lido como uma UF puxada por volume de dados. Se o objetivo for auditar volume financeiro, os principais focos sao as entidades lideres e os anos de pico. Se o objetivo for comparar com outras UFs, os melhores eixos sao quantidade de registros, ticket medio, concentracao e cobertura dos campos territoriais.
