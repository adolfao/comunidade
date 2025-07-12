from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormLogin, FormCriarConta
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os
from database import database, init_db_command
from models import Usuario, Post

app = Flask(__name__) 
load_dotenv(dotenv_path=r"C:\Users\Adolfo\Documents\comunidade\git\.env")

app.config['SECRET_KEY'] =  os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database.init_app(app)
app.cli.add_command(init_db_command)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/usuarios')
def usuarios():
  return render_template('usuarios.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')
  
@app.route('/login', methods=['GET', 'POST'])
def login():
  form_login = FormLogin()
  form_criarconta = FormCriarConta()
  
  #aqui verifica se o botao validou e se foi o botão de login o apertado
  if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
    flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success') #esse format exibe o que o cara preencheu no email
    print("Flash setado!")
    return redirect(url_for('home')) #redireciona para a home
      
  if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
    flash(f'Conta criada com sucesso no e-mail: {form_criarconta.email.data}', 'alert-success')
    return redirect(url_for('home'))
  
  return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)
  
if __name__ == "__main__":
  app.run(debug=True)