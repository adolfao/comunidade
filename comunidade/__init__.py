from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os
from comunidade.database import database, init_db_command
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__) 
load_dotenv(dotenv_path=r"C:\Users\Adolfo\Documents\comunidade\git\.env")

app.config['SECRET_KEY'] =  os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database.init_app(app)
app.cli.add_command(init_db_command)
bcrypt = Bcrypt(app) 
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Você precisa fazer login para acessar essa página'
login_manager.login_message_category = 'alert-info'

from comunidade import routes #precisa do app pra rodar
