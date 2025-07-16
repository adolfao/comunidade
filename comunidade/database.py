# arquivo criado so pra fazer uma triangulação entre models e main
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
import click

database = SQLAlchemy()

# comando customizado para recriar o banco
@click.command('init-db') 
@with_appcontext
def init_db_command():
    # apaga e recria o banco de dados.
    from comunidade.models import Usuario, Post 
    database.drop_all()
    database.create_all()
    print("Banco de dados recriado com sucesso!")
    #para rodar, ative o env pelo terminal do vscode: .\.venv\Scripts\Activate
		# e depois rode o comando: flask init-db
		#para ativar o env tem que estar na pasta do projeto