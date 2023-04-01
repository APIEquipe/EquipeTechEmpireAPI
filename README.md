## Equipe
- [Gabriel Henrique](https://github.com/GaSiqueira) / _Scrum Master_
- [Gustavo Castilho](https://github.com/GustavoCastilhoLucena) / _Dev_
- [Juan Santos](https://github.com/JuanSantosVale) / _Dev_
- [Kaue Riki](https://github.com/kaueriki) / _Dev_
- [Lucca Vilela](https://github.com/luccavilela) / _Dev_
- [Miguel Conde](https://github.com/miguelcondesantos) / _Dev_
- [Sarah Antunes](https://github.com/Amentine) / _Dev_
- [Silmara Bittencourt](https://github.com/SBittencourt) / _Product Owner_

## Sobre o Projeto
Projeto desenvolvido por alunos do 1º semestre do curso de Desenvolviento de Software Multiplatafora, da [Fatec São José dos Campos - Prof. Jessen Vidal.](https://fatecsjc-prd.azurewebsites.net/)
Consiste na criação de uma aplicação web que permite a analise de dados sobre a covid longa nas cidades de cobertura da Vanguarda, a fim de entender o impacto desssa condição no sistema de saúde das maiores cidades do Vale do Paraíba.
Back-end do projeto desenvolvido em Python3+ utilizando o microframework flask e o MySQL para gerenciar o banco de dados.

## Visão Geral
O produto é voltado para profissionais da área de saúde, pesquisadores e público em geral interessado em entender o impacto da covid longa no sistema de saúde das maiores cidades do Vale do Paraíba, a aplicação web ajuda os usarios que desejam ter acesso a dados precisos e atualizados sobre a covid longa nas cidades da região, a fim de entender melhor essa condição e seu impacto na saúde pública. Ao contrário de outros sistemas que podem apresentar dados genéricos sobre a covid-19, esse se concentra especificamente na análise de dados da Covid Longa nas cidades de cobertura da Vanguarda, nosso produto elabora informações detalhadas sobre a Covid Longa nas cidades de cobertura da Vanguarda, incluindo dados sobre casos, hospitalizações, sintomas, tratamentos e outros aspectos relevantes para a compreensão da condição e seus efeitos no sistema de saúde da região. Com base nesses dados, o produto deve ajudar os usuários a entender melhor a Covid Longa e desenvolver estratégias para enfrentá-la de forma eficaz.

## MVP
### Sprint 1
_1- Wireframe (protótipo do site)_

![▶ Page 1 - Wireframe - API - Google Chrome 2023-03-30 18-46-34](https://user-images.githubusercontent.com/106455775/228974604-628248d2-cc37-44b4-9167-3d0aa50c0845.gif)

_2- Gráfico da União com Combate à Covid-19 até 2022_

![image](https://user-images.githubusercontent.com/106455775/229213006-5886d729-5bdf-4f14-b640-384a91166805.png)


## Backlogs

### Backlog do Produto
| User Story | Requisito | Funcionalidade | Sprint |
| :--:       | :-----------:|:--------------:     |:--:    |
| **10** | **RNF03** | Levantamento de requisitos. | 1 |
| **07** | **RF07** | Criação do wireframe (protótipo navegável). | 1 |
| **01** | **RF01** | Pesquisa prévia para a criação de gráficos demonstrativos. | 1 |
| **01** | **RF01** | Criação de gráficos feitos a partir da pesquisa feita no item 3. | 1 |
| **10** | **RNF03** | Organização(backlog, burndown, organização da equipe). | 1 |  
| **10** | **RNF03** | Criação do GitHub. | 1 |
| **10** | **RNF03** | Organização do GitHub. | 1 |
| **07** | **RF07** | Criação da tela principal. | 2 |
| **07** | **RF07** | Criação das telas de consulta e de gastos. | 2 |
| **01** | **RF01** | Pesquisa aprofundada a cerca da covid longa. | 2 |
| **01** | **RF01** | Raspagem e tratamento de dados. Código para captura de dados a cerca da covid longa. | 2 |
| **01** | **RF01** | Ferramenta para criação dos gráficos a partir dos dados coletados. | 3 |
| **02** | **RF02** | Gráficos - Filtro para visualizar aumento e queda. | 3 |
| **03** | **RF03** | Gráficos - Filtro para visualizar por tempo. | 3 |
| **04** | **RF04** | Gráficos - Filtro por quantia de utilização | 3 |
| **05** | **RF05** | Gráficos - Filtro por gastos. | 3 |
| **09** | **RNF02** | Criação do banco de dados. | 3 |
| **09** | **RNF02** | Conexão do BD com a ferramenta de criação de gráficos. | 3 |
|  |  | Ajustes necessários. | 4 |
| **10** | **RNF03** | Finalização da documentação e organização final do GitHub. | 4 |

### User Story
 ID | Quem? | Para |
|:--------------:  | :----------:|:---------------------------------------------------------:|
| **01** |   Jornalista   | Gostaria de saber os tipos de consultas, tratamentos, procedimentos e uso de medicamentos entre os anos de 2019 a 2022 para compara-los e obter conteúdo para a sua matéria. |
| **02** |   Jornalista   | Gostaria de relacionar os tipos de consulta, tratamento, procedimentos e use de medicamentos para saber quais tiveram aumento e quais tiveram queda, a fim de obter conteúdo para sua matéria. |
| **03** |   Jornalista   | Gostaria de relacionar essas variação com a covid-19 para obter conteúdo para a sua matéria. |
| **04** |   Jornalista   | Gostaria de comparar os dados das consultas, tratamentos, procedimentos e uso de medicamentos entre 2019 e a partir de 2021 para saber quais foram mais usados em pacientes de covid longa, a fim de obter conteúdo para sua matéria. |
| **05** |   Jornalista   | Gostaria de saber os gastos/investimentos feitos em consultas, tratamentos, procedimentos e uso de medicamentos para dObter conteúdo para sua matéria. | 
| **06** |   Jornalista   | Gostaria de estabelecer uma participação dessas consultas, procedimentos, tratamentos e usos de medicamentos no total utilizado pelo SUS no período pré e pós pandemia para obter conteúdo para sua matéria. |
| **07** |   Jornalista   | Gostaria de uma interface com navegação intuitiva e responsiva para usar a aplicação. |
| **08** |   Jornalista   | Gostaria que os dados estejam armazenados e organizados em um Banco de Dados para serem mais acessíveis. |

### Backlog das Sprints
#### Sprint 1
| Item | Funcionalidade | Planning Poker |
| :--: | :--------------: | :-------------: |
|  01  | Levantamento de requesitos. | 8 |
|  02  | Criação do backlog do produto. | 5 |
|  03  | Wireframe/Protótipo. | 5 |
|  04  | Pesquisa prévia para a criação de gráficos. | 5 |
|  05  | Organização do Github | 5 |
|  06  | Criação do burndown. | 5 |
|  07  | Criação do backlog da sprint. | 3 |
|  08  | Tornar o protótipo navegável. | 3 |
|  09  | Criação de gráficos demonstrativos. | 3 |
|  10  | Criação do Github. | 1 |

## Entregas
<span id="entregas"></span>
O projeto está sendo realizado utilizando-se da metodologia ágil SCRUM, separadas em 4 entregas com sprints de 21 dias de duração cada uma. <br>

| Sprint| Período | Status |
|:-----:|:----------:|:---------:|
| 01 |   13/02/2023 - 02/04/2023 | Pendente :hourglass: | 
| 02 |   03/04/2023 - 23/04/2023 | Pendente :hourglass: |  
| 03 |   24/04/2023 - 14/05/2023 | Pendente :hourglass: | 
| 04 |   15/05/2023 - 04/06/2023 | Pendente :hourglass: |  

