# Goias (GO)

## Visao geral

Goias soma 1.676 registros e R$ 374.908.527,86 em valor total. No ranking geral da base, a UF esta em 23o lugar por valor, 19o por quantidade de registros, 23o por ticket medio e 9o por concentracao dos 5 maiores beneficiarios.

O perfil dominante da UF e base mais distribuida. O ticket medio e de R$ 223.692,44, a mediana e de R$ 0,00 e os 5 maiores beneficiarios concentram 49,4% do valor total.

_Fonte local deste bloco: `processada/GO.parquet`; campos e agregacoes usados: `valor_total`, `nome_osc`, `cnpj`, `ano`, agregacoes por UF, ranks e shares dos maiores beneficiarios._

## Leitura narrativa

Comparando com o conjunto nacional, GO aparece entre as UFs lideres por valor em `PR, SP, PB, MS, SE`, por volume em `SE, PB, PR, MG, RS`, por ticket medio em `PE, RR, RJ, AM, AC` e por concentracao em `AC, RR, PR, CE, PE`.

Na pratica, isso indica que Goias cresce principalmente por base mais distribuida. A participacao da UF no total nacional desta pasta e de 0,1%.

_Fonte local deste bloco: `processada/GO.parquet`; campos e agregacoes usados: benchmark nacional entre UFs, com comparacao de `valor_num`, `registros`, `ticket_medio` e `top5_share_pct`._

## Principais entidades

1. `01285170000122` - COMPANHIA DE DESENVOLVIMENTO ECONOMICO DE GOIAS: R$ 122.074.582,04 em 14 registros.
2. `01181585000156` - PIRES DO RIO: R$ 19.268.991,80 em 2 registros.
3. `01219807000182` - URUACU: R$ 17.464.808,40 em 4 registros.
4. `01165729000180` - JATAI: R$ 15.203.449,62 em 6 registros.
5. `01169416000109` - LUZIANIA: R$ 11.310.932,62 em 1 registros.

_Fonte local deste bloco: `processada/GO.parquet`; campos e agregacoes usados: agrupamento por `nome_osc` e `cnpj`, soma de `valor_num` e contagem de registros._

## Gastos e objetivos

Termos mais frequentes nos objetos da UF: `UNIDADES, HABITACIONAIS, REFORMA, CONSTRUCAO, ASFALTICA, AQUISICAO, MASSA, FORNECIMENTO, PAVIMENTACAO, PRACA, TIPO, PUBLICO`.

Registros de maior valor que ajudam a explicar os objetivos do gasto:

1. `COMPANHIA DE DESENVOLVIMENTO ECONOMICO DE GOIAS` - R$ 80.236.559,25 (ano 2018): Execucao de Obras de Infraestrutura de Pavimentacao e Obras de Arte na GO 108: Guarani/Terra Ronca.
2. `PIRES DO RIO` - R$ 19.268.991,80 (ano 2018): Recuperacao e Conservacao de Pavimentacao Asfaltica de Pires do Rio.
3. `LUZIANIA` - R$ 11.310.932,62 (ano 2017): PAVIMENTACAO ASFALTICA NOS BAIRROS DE LUZIANIA.
4. `JATAI` - R$ 10.830.051,84 (ano 2017): RECAPEAMENTO COM CBUQ - CONCRETO BETUMINOSO USINADO A QUENTE E LAMA ASFALTICA GROSSA.
5. `COMPANHIA DE DESENVOLVIMENTO ECONOMICO DE GOIAS` - R$ 10.269.734,26 (ano 2018): Reconstrucao e Recapeamento de Vias Urbanas do Municipio de Minacu, neste Estado.

O maior registro individual da UF foi para `COMPANHIA DE DESENVOLVIMENTO ECONOMICO DE GOIAS` no valor de R$ 80.236.559,25. O objeto associado foi: Execucao de Obras de Infraestrutura de Pavimentacao e Obras de Arte na GO 108: Guarani/Terra Ronca.

_Fonte local deste bloco: `processada/GO.parquet`; campos e agregacoes usados: campos `objeto`, `valor_total`, `ano`; selecao dos maiores registros por `valor_num`._

## Evolucao temporal

Anos de maior volume:

1. `2018` - R$ 211.516.000,82 em 233 registros.
2. `2017` - R$ 163.392.527,04 em 93 registros.
3. `2010` - R$ 0,00 em 1 registros.

Ultimos anos da serie:

- `2014`: R$ 0,00 em 646 registros, variacao n/d.
- `2015`: R$ 0,00 em 83 registros, variacao n/d.
- `2016`: R$ 0,00 em 184 registros, variacao n/d.
- `2017`: R$ 163.392.527,04 em 93 registros, variacao inf%.
- `2018`: R$ 211.516.000,82 em 233 registros, variacao 29,5%.

_Fonte local deste bloco: `processada/GO.parquet`; campos e agregacoes usados: agregacao anual por `ano_num`, soma de `valor_num`, contagem de registros e variacao percentual._

## Territorio e cobertura

A base desta UF nao traz cobertura territorial suficiente para destacar municipios com seguranca.

Cobertura observada: CNPJ valido em 100,0%, municipio em 0,0%, objeto em 99,9% e modalidade em 100,0%. Ha 0 registros negativos e 209 registros marcados como duplicado aparente.

_Fonte local deste bloco: `processada/GO.parquet`; campos e agregacoes usados: campos `municipio`, `cod_municipio`, `objeto`, `modalidade`, `cnpj`, `duplicado_aparente`, `valor_negativo`._

## Fontes extras

### Dados locais

- Arquivo principal desta historia: `processada/GO.parquet`.
- Todas as afirmacoes sobre gasto, volume, anos, concentracao, objetivos e municipios foram derivadas desse parquet.

### Fontes externas verificadas por entidade

- [Consulta oficial de CNPJ (gov.br)](https://www.gov.br/pt-br/servicos/consultar-cadastro-nacional-de-pessoas-juridicas)
- [Comprovante de inscricao e situacao cadastral (Receita)](https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp)
- [Convenios e transferencias federais (gov.br / Transferegov)](https://www.gov.br/planejamento/pt-br/acesso-a-informacao/convenios-e-transparencias)

- `COMPANHIA DE DESENVOLVIMENTO ECONOMICO DE GOIAS` (01285170000122): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/01285170000122) - status da consulta 429.
- `PIRES DO RIO` (01181585000156): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/01181585000156) - status da consulta 429.
- `URUACU` (01219807000182): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/01219807000182) - status da consulta 429.
- `JATAI` (01165729000180): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/01165729000180) - status da consulta 429.
- `LUZIANIA` (01169416000109): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/01169416000109) - status da consulta 429.

### Investigacao complementar

- [COMPANHIA DE DESENVOLVIMENTO ECONOMICO DE GOIAS - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=01285170000122+COMPANHIA+DE+DESENVOLVIMENTO+ECONOMICO+DE+GOIAS+Goias+convenio+contrato+gestao)
- [PIRES DO RIO - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=01181585000156+PIRES+DO+RIO+Goias+convenio+contrato+gestao)
- [URUACU - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=01219807000182+URUACU+Goias+convenio+contrato+gestao)
- [JATAI - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=01165729000180+JATAI+Goias+convenio+contrato+gestao)
- [LUZIANIA - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=01169416000109+LUZIANIA+Goias+convenio+contrato+gestao)

## Conclusao

Goias deve ser lido como uma UF puxada por base mais distribuida. Se o objetivo for auditar volume financeiro, os principais focos sao as entidades lideres e os anos de pico. Se o objetivo for comparar com outras UFs, os melhores eixos sao quantidade de registros, ticket medio, concentracao e cobertura dos campos territoriais.
