## Como baixar e executar as páginas:

1 passo - Clonar o repositório:

Crie uma pasta e acesse o cmd pela barra de busca
Digite: git clone(Link para clonagem) .


2 passo - Acesso pelo terminal:
Com o repositório clonado, acesse a pasta FrontEnd e novamente acesse o cmd pela barra

Para abrir o visual studio digite: code .
Entre na aba terminal e abra um novo terminal

3 passo - Instalação do requirements.txt:
Digite os seguintes códigos:

Para instalação do ambiente virtual venv: py -3 -m venv venv 

Para permitir a instalação, abra o powershell como administrador e digite: Set-ExecutionPolicy -ExecutionPolicy AllSigned

Aprove o que for perguntado clicando na tecla: A

--> Inicie o ambiente virtual:

.\venv\Script\Activate

--> Instale/atualize o pip:

python -m pip install --upgrade pip

4 passo - Instalação e inicialização do Flask:

Para instalar o flask: pip install -r requirements.txt


E então, caso tudo esteja certo, basta iniciar o programa:

flask run

Será aberto um link local, que ao clicar, você terá acesso ao programa.
