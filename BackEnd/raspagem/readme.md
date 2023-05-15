## Como executar o programa

  Para executar o programa, deve-se realizar o download do arquivo **raspagem v2.py**, com o arquivo no computador, enviar ele para uma pasta previamente vazia. Agora, dentro da pasta, deve-se criar um arquivo com extensão **.txt** nomeado de **requirements**, abrindo o arquivo, deve-se editá-lo, copiando e colando o seguinte texto:

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

  Agora, deve-se abrir o [Visual Studio Code](https://code.visualstudio.com/download), nele escolha a pasta onde está o aplicativo. agora, abra o terminal pelo botão na parte superior chamado de **Novo terminal**, dentro do terminal, execute o seguinte comando:
  
```
pip install -r requirements.txt
```

  Com os requerimentos instalados, clique no aplicativo **raspagem v2.py** na parte esquerda do Visual Studio Code e selecione a opção **Executar o Arquivo do Python no Terminal**. Selecionando as opções de desejo, um arquivo será criado com os dados e outro arquivo será criado com um gráfico.

