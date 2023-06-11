# Instruções para instalar e executar os arquivos

## 1- Clonar o repositório

Crie uma pasta de qualquer nome, acesse ela, pesquise por "cmd" na barra de pesquisa e digite o seguinte código: 

```
git clone <link do repositório>
```

## 2- Acesso pelo terminal

Com o repositório clonado, ainda na linha de comando, acesse a pasta FrontEnd com o seguinte código:

```
cd EquipeTechEmpireAPI/FrontEnd/
```

Agora, abra o Visual Studio Code com o seguinte código:

```
code .
```

Na parte superior do aplicativo, entre na opção "terminal" e abra um novo terminal.

## 3- Instalação do requirements.txt

Com o terminal ainda aberto, digite os seguintes códigos:

Para instalação do ambiente virtual venv:

```
py -3 -m venv venv 
```

Ao executar o comando, ocorrerá um erro de permissão. Para permitir a instalação, abra o powershell como administrador e digite: 

```
Set-ExecutionPolicy -ExecutionPolicy AllSigned
```

Aprove o que for perguntado clicando na tecla: A

Volte para o terminal do Visual Studio Code. Nele, inicie o ambiente virtual com o seguinte comando:

```
.\venv\Script\Activate
```

Em seguida, deve ser instalado e atualizado o "pip" como seguinte comando:

```
python -m pip install --upgrade pip
````

## 4- Instalação e inicialização do Flask:

Ainda no terminal, instale o flask utilzando o seguinte comando:

```
pip install -r requirements.txt
```

Após seguir todas as instruções, para ter acesso ao website execute o seguinte comando:

```
flask run
```

Agora, aparecerá um link em formato de protocolo IP, onde, segurando o botão Control, deve-se clicar com o botão esquerdo do mouse.
Para navegar pelas abas do website pode-se clicar nos links em formato de nome na parte superior da tela.
