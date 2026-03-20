# Amapa (AP)

## Visao geral

Amapa soma 1.553 registros e R$ 2.409.891.576,58 em valor total. No ranking geral da base, a UF esta em 16o lugar por valor, 20o por quantidade de registros, 7o por ticket medio e 11o por concentracao dos 5 maiores beneficiarios.

O perfil dominante da UF e ticket medio. O ticket medio e de R$ 1.551.765,34, a mediana e de R$ 400.000,00 e os 5 maiores beneficiarios concentram 46,7% do valor total.

_Fonte local deste bloco: `processada/AP.parquet`; campos e agregacoes usados: `valor_total`, `nome_osc`, `cnpj`, `ano`, agregacoes por UF, ranks e shares dos maiores beneficiarios._

## Leitura narrativa

Comparando com o conjunto nacional, AP aparece entre as UFs lideres por valor em `PR, SP, PB, MS, SE`, por volume em `SE, PB, PR, MG, RS`, por ticket medio em `PE, RR, RJ, AM, AC` e por concentracao em `AC, RR, PR, CE, PE`.

Na pratica, isso indica que Amapa cresce principalmente por ticket medio. A participacao da UF no total nacional desta pasta e de 0,7%.

_Fonte local deste bloco: `processada/AP.parquet`; campos e agregacoes usados: benchmark nacional entre UFs, com comparacao de `valor_num`, `registros`, `ticket_medio` e `top5_share_pct`._

## Principais entidades

1. `06303192001597` - ASSOCIACAO EDUCADORA SAO FRANCISCO DE ASSIS: R$ 781.365.343,53 em 29 registros.
2. `01560733000143` - ASSOCIACAO DOS MUSICOS E COMPOSIT.DO AP-AMCAP: R$ 97.170.225,29 em 23 registros.
3. `07871719000147` - INSTITUTO DE GESTAO EM DESENVOLVIMENTO SOCIAL E URBANO: R$ 90.422.364,55 em 38 registros.
4. `23066640000108` - PREFEITURA MUNICIPAL DE SANTANA: R$ 80.621.442,91 em 7 registros.
5. `07243422000137` - INSTITUTO PADRE JOAO DA CRUZ: R$ 75.816.795,24 em 4 registros.

_Fonte local deste bloco: `processada/AP.parquet`; campos e agregacoes usados: agrupamento por `nome_osc` e `cnpj`, soma de `valor_num` e contagem de registros._

## Gastos e objetivos

Termos mais frequentes nos objetos da UF: `PRODUTIVO, 2022, ARRANJO, 2024, AMAPA, 2025, FOMENTO, TERMO, PROGRAMA, MANDIOCULTURA, 2023, SAFRA`.

Registros de maior valor que ajudam a explicar os objetivos do gasto:

1. `ASSOCIACAO EDUCADORA SAO FRANCISCO DE ASSIS` - R$ 124.392.074,30 (ano 2023): TERMO DE FOMENTO.
2. `ASSOCIACAO EDUCADORA SAO FRANCISCO DE ASSIS` - R$ 111.052.848,00 (ano 2024): O objeto do presente Termo de Fomento, de acordo com Lei n 13.019, 31 de julho de 2014, tera como finalidade a prestacao de servicos medico-hospitalares, incluindo a gestao de leitos cirurgicos, leitos de terapia intensiva e do centro cirurgico no Hospital de Clinicas Dr. Alberto Lima (HCAL) conforme o Plano de Trabalho..
3. `ASSOCIACAO EDUCADORA SAO FRANCISCO DE ASSIS` - R$ 111.052.848,00 (ano 2024): O objeto do presente Termo de Fomento, de acordo com Lei n 13.019, 31 de julho de 2014, tera como finalidade a prestacao de servicos medico-hospitalares, incluindo a gestao de leitos cirurgicos, leitos de terapia intensiva e do centro cirurgico no Hospital de Clinicas Dr. Alberto Lima (HCAL) conforme o Plano de Trabalho..
4. `ASSOCIACAO EDUCADORA SAO FRANCISCO DE ASSIS` - R$ 69.937.597,75 (ano 2024): TERMO DE FOMENTO No 012/2023  SESA.
5. `ASSOCIACAO EDUCADORA SAO FRANCISCO DE ASSIS` - R$ 69.937.597,75 (ano 2024): TERMO DE FOMENTO No 012/2023  SESA.

O maior registro individual da UF foi para `ASSOCIACAO EDUCADORA SAO FRANCISCO DE ASSIS` no valor de R$ 124.392.074,30. O objeto associado foi: TERMO DE FOMENTO.

_Fonte local deste bloco: `processada/AP.parquet`; campos e agregacoes usados: campos `objeto`, `valor_total`, `ano`; selecao dos maiores registros por `valor_num`._

## Evolucao temporal

Anos de maior volume:

1. `2024` - R$ 1.297.154.317,84 em 911 registros.
2. `2023` - R$ 402.372.274,53 em 116 registros.
3. `2025` - R$ 265.297.832,73 em 155 registros.

Ultimos anos da serie:

- `2022`: R$ 218.673.314,42 em 255 registros, variacao n/d.
- `2023`: R$ 402.372.274,53 em 116 registros, variacao 84,0%.
- `2024`: R$ 1.297.154.317,84 em 911 registros, variacao 222,4%.
- `2025`: R$ 265.297.832,73 em 155 registros, variacao -79,5%.
- `2026`: R$ 1.527.300,00 em 1 registros, variacao -99,4%.

_Fonte local deste bloco: `processada/AP.parquet`; campos e agregacoes usados: agregacao anual por `ano_num`, soma de `valor_num`, contagem de registros e variacao percentual._

## Territorio e cobertura

A base desta UF nao traz cobertura territorial suficiente para destacar municipios com seguranca.

Cobertura observada: CNPJ valido em 100,0%, municipio em 0,0%, objeto em 99,5% e modalidade em 98,5%. Ha 0 registros negativos e 76 registros marcados como duplicado aparente.

_Fonte local deste bloco: `processada/AP.parquet`; campos e agregacoes usados: campos `municipio`, `cod_municipio`, `objeto`, `modalidade`, `cnpj`, `duplicado_aparente`, `valor_negativo`._

## Fontes extras

### Dados locais

- Arquivo principal desta historia: `processada/AP.parquet`.
- Todas as afirmacoes sobre gasto, volume, anos, concentracao, objetivos e municipios foram derivadas desse parquet.

### Fontes externas verificadas por entidade

- [Consulta oficial de CNPJ (gov.br)](https://www.gov.br/pt-br/servicos/consultar-cadastro-nacional-de-pessoas-juridicas)
- [Comprovante de inscricao e situacao cadastral (Receita)](https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp)
- [Convenios e transferencias federais (gov.br / Transferegov)](https://www.gov.br/planejamento/pt-br/acesso-a-informacao/convenios-e-transparencias)

- `ASSOCIACAO EDUCADORA SAO FRANCISCO DE ASSIS` (06303192001597): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/06303192001597) - situacao ATIVA; municipio/UF MACAPA/AP; porte DEMAIS; atividade principal Atividade medica ambulatorial com recursos para realizacao de procedimentos cirurgicos.
- `ASSOCIACAO DOS MUSICOS E COMPOSIT.DO AP-AMCAP` (01560733000143): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/01560733000143) - situacao ATIVA; municipio/UF MACAPA/AP; porte DEMAIS; atividade principal Atividades de associacoes de defesa de direitos sociais.
- `INSTITUTO DE GESTAO EM DESENVOLVIMENTO SOCIAL E URBANO` (07871719000147): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/07871719000147) - situacao ATIVA; municipio/UF MACAPA/AP; porte DEMAIS; atividade principal Outras atividades profissionais, cientificas e tecnicas nao especificadas anteriormente.
- `PREFEITURA MUNICIPAL DE SANTANA` (23066640000108): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/23066640000108) - situacao ATIVA; municipio/UF SANTANA/AP; porte DEMAIS; atividade principal Administracao publica em geral.
- `INSTITUTO PADRE JOAO DA CRUZ` (07243422000137): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/07243422000137) - situacao ATIVA; municipio/UF SANTANA/AP; porte DEMAIS; atividade principal Atividades de profissionais da area de saude nao especificadas anteriormente.

### Investigacao complementar

- [ASSOCIACAO EDUCADORA SAO FRANCISCO DE ASSIS - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=06303192001597+ASSOCIACAO+EDUCADORA+SAO+FRANCISCO+DE+ASSIS+Amapa+convenio+contrato+gestao)
- [ASSOCIACAO DOS MUSICOS E COMPOSIT.DO AP-AMCAP - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=01560733000143+ASSOCIACAO+DOS+MUSICOS+E+COMPOSIT.DO+AP-AMCAP+Amapa+convenio+contrato+gestao)
- [INSTITUTO DE GESTAO EM DESENVOLVIMENTO SOCIAL E URBANO - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=07871719000147+INSTITUTO+DE+GESTAO+EM+DESENVOLVIMENTO+SOCIAL+E+URBANO+Amapa+convenio+contrato+gestao)
- [PREFEITURA MUNICIPAL DE SANTANA - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=23066640000108+PREFEITURA+MUNICIPAL+DE+SANTANA+Amapa+convenio+contrato+gestao)
- [INSTITUTO PADRE JOAO DA CRUZ - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=07243422000137+INSTITUTO+PADRE+JOAO+DA+CRUZ+Amapa+convenio+contrato+gestao)

## Conclusao

Amapa deve ser lido como uma UF puxada por ticket medio. Se o objetivo for auditar volume financeiro, os principais focos sao as entidades lideres e os anos de pico. Se o objetivo for comparar com outras UFs, os melhores eixos sao quantidade de registros, ticket medio, concentracao e cobertura dos campos territoriais.
