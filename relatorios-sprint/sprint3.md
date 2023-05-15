# Sprint 3

Nesta Sprint o foco foi na raspagem de dados. Houve também atualização no número de informações sobre a covid longa e a criação do banco de dados.

## Backlog da Sprint
| Item | Funcionalidade | Planning Poker |
| :--: | :--------------: | :-------------: |
|  01  | Pesquisa aprofundada acerca dos dados. | 8 |
|  02  | Criação do código para captura dos dados | 8 |
|  03  | Raspagem de dados. | 8 |
|  04  | Tratamento dos dados coletados na raspagem. | 8 |
|  05  | Criação do banco de dados. | 8 |
|  06  | Estudo a respeito de banco de dados. | 5 |
|  07  | Criação do modelo lógico do banco de dados. | 5 |
|  08  | Testes para confirmar o funcionamento. | 5 |
|  09  | Estudo a cerca de criação de gráficos por código. | 3 |
|  10  | Criação do backlog da sprint. | 3 |
|  11  | Organização do Github da Sprint. | 3 |

## Benefícios
* Permite a elaboração de matérias sobre a covid longa com mais facilidade, segmentando rapidamente os dados desejados;
* Agrega à produtividade dos jornalistas porque o processo não exige que os profissionais escrevam códigos ou scripts;
* O cliente poderá ter uma visão ampla da ferramenta e sugerir possíveis ajustes de navegação nos ambientes desenvolvidos.

## Funcionalidades desenvolvidas
![video raspagem (1)](https://github.com/APIEquipe/EquipeTechEmpireAPI/assets/112987836/fde190fa-cad3-45e9-a94a-ca002e7c63fb)

## Como executar o programa

  Para executar o programa, deve-se realizar o download do arquivo **raspagem v2.py** em *EquipeTechEmpireAPI/BackEnd/raspagem/*, com o arquivo no computador, enviar ele para uma pasta previamente vazia. Agora, dentro da pasta, deve-se criar um arquivo com extensão **.txt** nomeado de **requirements**, abrindo o arquivo, deve-se editá-lo, copiando e colando o seguinte texto:

```
altgraph==0.17.3
beautifulsoup4==4.12.2
blinker==1.6.2
bs4==0.0.1
certifi==2023.5.7
charset-normalizer==3.1.0
click==8.1.3
colorama==0.4.6
contourpy==1.0.7
cycler==0.11.0
et-xmlfile==1.1.0
Flask==2.3.2
fonttools==4.39.4
idna==3.4
itsdangerous==2.1.2
Jinja2==3.1.2
kiwisolver==1.4.4
markdown-it-py==2.2.0
MarkupSafe==2.1.2
matplotlib==3.7.1
mdurl==0.1.2
numpy==1.24.3
openpyxl==3.1.2
packaging==23.1
pandas==2.0.1
pefile==2023.2.7
Pillow==9.5.0
Pygments==2.15.1
pyinstaller==5.10.1
pyinstaller-hooks-contrib==2023.3
pyparsing==3.0.9
python-dateutil==2.8.2
pytz==2023.3
pywin32-ctypes==0.2.0
requests==2.30.0
rich==13.3.5
six==1.16.0
soupsieve==2.4.1
tzdata==2023.3
urllib3==2.0.2
Werkzeug==2.3.4
```

  Agora, deve-se abrir o [Visual Studio Code](https://code.visualstudio.com/download), nele escolha a pasta onde está o aplicativo. Em seguida, abra o terminal pelo botão na parte superior chamado de **Novo terminal**. Dentro do terminal, execute o seguinte comando:
  
```
pip install -r requirements.txt
```

  Com os requerimentos instalados, clique com o botão direito no aplicativo **raspagem v2.py** na parte esquerda do Visual Studio Code e selecione a opção **Executar o Arquivo do Python no Terminal**. Selecionando as opções de desejo, um arquivo será criado com os dados e outro arquivo será criado com um gráfico.

