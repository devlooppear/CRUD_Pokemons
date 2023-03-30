# Pokemon_Finder

- Este é um site desenvolvido com Flask que permite pesquisar informações de Pokémons, tais como nome, descrição, HP, tipo, região e imagem. Para armazenamento dos dados, foi utilizado o banco de dados PostgreSQL.

## Input

- O arquivo de execussão é o `run.py`.

## Output

- O output é a aplicação web aberta pelo browser.

## Requisitos

- Python 3
- PostgreSQL
- Pacotes Python: Flask
- SQLAlchemy
- Psycopg2

## Instalação

- Clone este repositório em sua máquina local:
`bash`
- git clone https://github.com/seu-usuario/pokemon-finder.git
- Crie um ambiente virtual:
python -m venv myenv
Ative o ambiente virtual:
source myenv/bin/activate
Instale as dependências do projeto:
pip install -r requirements.txt
- Crie o banco de dados e execute as migrações:
- createdb pokemon_db
- flask db upgrade
- Execute a aplicação:
Acesse http://localhost:5000 em seu navegador, clicando CTRL + Click com o botão direito em http://localhost:5000 .
## Utilização
Na página inicial, é possível pesquisar por um Pokémon pelo seu nome. Ao clicar no botão "Buscar", o site irá retornar o nome, descrição, HP, tipo, região e imagem.

## Tecnologias utilizadas
- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Psycopg2

## Conclusão
- Este projeto tem como objetivo demonstrar como criar uma aplicação web simples utilizando Flask e banco de dados PostgreSQL. É possível adaptar o código para criar uma aplicação mais complexa e robusta, com mais funcionalidades e recursos.