from flask import Flask, render_template, url_for
from forms import FormLogin, FormCriarConta
from dotenv import load_dotenv
import os

app = Flask(__name__) 
load_dotenv(dotenv_path=r"C:\Users\Adolfo\Documents\comunidade\README\.env")

app.config['SECRET_KEY'] =  os.getenv("SECRET_KEY")

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/usuarios')
def usuarios():
  return render_template('usuarios.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')
  
@app.route('/login')
def login():
  form_login = FormLogin()
  form_criarconta = FormCriarConta()
  return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)
  
if __name__ == "__main__":
  app.run(debug=True)