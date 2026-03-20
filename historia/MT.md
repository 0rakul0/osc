# Mato Grosso (MT)

## Visao geral

Mato Grosso soma 18.990 registros e R$ 13.519.491.879,46 em valor total. No ranking geral da base, a UF esta em 8o lugar por valor, 10o por quantidade de registros, 12o por ticket medio e 25o por concentracao dos 5 maiores beneficiarios.

O perfil dominante da UF e base mais distribuida. O ticket medio e de R$ 711.926,90, a mediana e de R$ 110.000,00 e os 5 maiores beneficiarios concentram 10,7% do valor total.

_Fonte local deste bloco: `processada/MT.parquet`; campos e agregacoes usados: `valor_total`, `nome_osc`, `cnpj`, `ano`, agregacoes por UF, ranks e shares dos maiores beneficiarios._

## Leitura narrativa

Comparando com o conjunto nacional, MT aparece entre as UFs lideres por valor em `PR, SP, PB, MS, SE`, por volume em `SE, PB, PR, MG, RS`, por ticket medio em `PE, RR, RJ, AM, AC` e por concentracao em `AC, RR, PR, CE, PE`.

Na pratica, isso indica que Mato Grosso cresce principalmente por base mais distribuida. A participacao da UF no total nacional desta pasta e de 3,7%.

_Fonte local deste bloco: `processada/MT.parquet`; campos e agregacoes usados: benchmark nacional entre UFs, com comparacao de `valor_num`, `registros`, `ticket_medio` e `top5_share_pct`._

## Principais entidades

1. `03347101000121` - PREFEITURA MUNICIPAL DE RONDONOPOLIS: R$ 302.663.126,33 em 164 registros.
2. `05682036000116` - ASSOCIACAO DOS PRODUTORES DA RODOVIA MT - 480: R$ 295.069.704,07 em 5 registros.
3. `03507548000110` - PREFEITURA MUNICIPAL DE VARZEA GRANDE: R$ 290.337.021,38 em 98 registros.
4. `24772246000140` - PREFEITURA MUNICIPAL DE LUCAS DO RIO VERDE: R$ 287.499.243,04 em 94 registros.
5. `33004540000100` - FUNDACAO UNIVERSIDADE FEDERAL DE MATO GROSSO: R$ 269.797.332,67 em 27 registros.

_Fonte local deste bloco: `processada/MT.parquet`; campos e agregacoes usados: agrupamento por `nome_osc` e `cnpj`, soma de `valor_num` e contagem de registros._

## Gastos e objetivos

Termos mais frequentes nos objetos da UF: `MUNICIPIO, SOCIAL, REALIZACAO, RECURSOS, EXTENSAO, AQUISICAO, ENTRE, ESPECIAL, CONSTRUCAO, SERVICOS, PRESENTE, MATO`.

Registros de maior valor que ajudam a explicar os objetivos do gasto:

1. `ASSOCIACAO DOS PRODUTORES DA RODOVIA MT - 480` - R$ 223.104.472,08 (ano 2014): PAVIMENTACAO DA RODOVIA MT 339 - TRECHO: ENTRONCAMENTO RODOVIA 251/364 - ENTRONCAMENTO RODOVIA MT 170 - SUB-TRECHO: ENTRONCAMENTO RODOVIA MT 358 - RODOVIA MT 170 (PANORAMA).
2. `ASSOCIACAO MT 322 - TRECHO MATUPA/MT AO RIO XINGU - PEIXOTO DE AZEVEDO` - R$ 126.667.089,34 (ano 2010): PAVIMENTACAO DA RODOVIA MT - 322, TRECHO: Entroc. BR -163 (MATUPA) - Entroc.MT 130 - SAO JOSE DO XINGU - Entroc. BR 158..
3. `FUNDACAO UNIVERSIDADE FEDERAL DE MATO GROSSO` - R$ 125.549.359,29 (ano 2017): Aperfeicoamento do controle interno e externo do TCE/MPC, por meio de processos de educacao mediada por tecnologias da informacao e da comunicacao e metodos inovadores em gestao publica - Na perspectiva do TCE e MPCMT, o presente convenio tem como objetivo contribuir para a melhoria e aprimoramento de controle institucional interno e externo, por meio de processos de inovacao em educacao mediada por Tecnologias da Informacao e Comunicacao (TICs) e inovacao nos processosde gestao publica, com resultados a serem consolidados em seis metas e acoes, atendendo aos Termos de Referencia e Projetos Basicos do TCE e do MPC/MT. Na perspectiva da UFMT, o convenio pressupoe a realizacao de acoes de Ensi.
4. `ASSOCIACAO CONGREGACAO DE SANTA CATARINA - HOSPITAL SAO LUIZ` - R$ 123.417.768,87 (ano 2012): Integrar a CONVENENTE no Sistema Unico de Saude - SUS e definir a sua insercao na rede regionalizada e hierarquizada de acoes e servicos de saude..
5. `PREFEITURA MUNICIPAL DE QUERENCIA` - R$ 104.496.926,65 (ano 2023): O presente Convenio tem por objeto formalizar entendimentos entre as partes no sentido de unirem esforcos e recursos para Implantacao e Pavimentacao da Rodovia MT-109/110, Trecho: Fim PU Querencia  Entr. MT- 109  Subtrecho: Fim da Pavimentacao  Fazenda Pioneira , numa extensao de 53,60km , no Municipio de Querencia-MT..

O maior registro individual da UF foi para `ASSOCIACAO DOS PRODUTORES DA RODOVIA MT - 480` no valor de R$ 223.104.472,08. O objeto associado foi: PAVIMENTACAO DA RODOVIA MT 339 - TRECHO: ENTRONCAMENTO RODOVIA 251/364 - ENTRONCAMENTO RODOVIA MT 170 - SUB-TRECHO: ENTRONCAMENTO RODOVIA MT 358 - RODOVIA MT 170 (PANORAMA).

_Fonte local deste bloco: `processada/MT.parquet`; campos e agregacoes usados: campos `objeto`, `valor_total`, `ano`; selecao dos maiores registros por `valor_num`._

## Evolucao temporal

Anos de maior volume:

1. `2022` - R$ 2.642.436.473,69 em 1.663 registros.
2. `2024` - R$ 1.615.533.076,92 em 1.311 registros.
3. `2023` - R$ 1.562.588.514,28 em 1.309 registros.

Ultimos anos da serie:

- `2021`: R$ 1.065.287.158,65 em 882 registros, variacao n/d.
- `2022`: R$ 2.642.436.473,69 em 1.663 registros, variacao 148,0%.
- `2023`: R$ 1.562.588.514,28 em 1.309 registros, variacao -40,9%.
- `2024`: R$ 1.615.533.076,92 em 1.311 registros, variacao 3,4%.
- `2025`: R$ 755.507.200,77 em 948 registros, variacao -53,2%.

_Fonte local deste bloco: `processada/MT.parquet`; campos e agregacoes usados: agregacao anual por `ano_num`, soma de `valor_num`, contagem de registros e variacao percentual._

## Territorio e cobertura

A base desta UF nao traz cobertura territorial suficiente para destacar municipios com seguranca.

Cobertura observada: CNPJ valido em 100,0%, municipio em 0,0%, objeto em 100,0% e modalidade em 100,0%. Ha 0 registros negativos e 22 registros marcados como duplicado aparente.

_Fonte local deste bloco: `processada/MT.parquet`; campos e agregacoes usados: campos `municipio`, `cod_municipio`, `objeto`, `modalidade`, `cnpj`, `duplicado_aparente`, `valor_negativo`._

## Fontes extras

### Dados locais

- Arquivo principal desta historia: `processada/MT.parquet`.
- Todas as afirmacoes sobre gasto, volume, anos, concentracao, objetivos e municipios foram derivadas desse parquet.

### Fontes externas verificadas por entidade

- [Consulta oficial de CNPJ (gov.br)](https://www.gov.br/pt-br/servicos/consultar-cadastro-nacional-de-pessoas-juridicas)
- [Comprovante de inscricao e situacao cadastral (Receita)](https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp)
- [Convenios e transferencias federais (gov.br / Transferegov)](https://www.gov.br/planejamento/pt-br/acesso-a-informacao/convenios-e-transparencias)

- `PREFEITURA MUNICIPAL DE RONDONOPOLIS` (03347101000121): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/03347101000121) - status da consulta 429.
- `ASSOCIACAO DOS PRODUTORES DA RODOVIA MT - 480` (05682036000116): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/05682036000116) - status da consulta 429.
- `PREFEITURA MUNICIPAL DE VARZEA GRANDE` (03507548000110): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/03507548000110) - status da consulta 429.
- `PREFEITURA MUNICIPAL DE LUCAS DO RIO VERDE` (24772246000140): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/24772246000140) - status da consulta 429.
- `FUNDACAO UNIVERSIDADE FEDERAL DE MATO GROSSO` (33004540000100): [fonte externa verificada](https://brasilapi.com.br/api/cnpj/v1/33004540000100) - status da consulta 429.

### Investigacao complementar

- [PREFEITURA MUNICIPAL DE RONDONOPOLIS - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=03347101000121+PREFEITURA+MUNICIPAL+DE+RONDONOPOLIS+Mato+Grosso+convenio+contrato+gestao)
- [ASSOCIACAO DOS PRODUTORES DA RODOVIA MT - 480 - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=05682036000116+ASSOCIACAO+DOS+PRODUTORES+DA+RODOVIA+MT+-+480+Mato+Grosso+convenio+contrato+gestao)
- [PREFEITURA MUNICIPAL DE VARZEA GRANDE - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=03507548000110+PREFEITURA+MUNICIPAL+DE+VARZEA+GRANDE+Mato+Grosso+convenio+contrato+gestao)
- [PREFEITURA MUNICIPAL DE LUCAS DO RIO VERDE - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=24772246000140+PREFEITURA+MUNICIPAL+DE+LUCAS+DO+RIO+VERDE+Mato+Grosso+convenio+contrato+gestao)
- [FUNDACAO UNIVERSIDADE FEDERAL DE MATO GROSSO - busca complementar por CNPJ/nome/UF](https://www.google.com/search?q=33004540000100+FUNDACAO+UNIVERSIDADE+FEDERAL+DE+MATO+GROSSO+Mato+Grosso+convenio+contrato+gestao)

## Conclusao

Mato Grosso deve ser lido como uma UF puxada por base mais distribuida. Se o objetivo for auditar volume financeiro, os principais focos sao as entidades lideres e os anos de pico. Se o objetivo for comparar com outras UFs, os melhores eixos sao quantidade de registros, ticket medio, concentracao e cobertura dos campos territoriais.
