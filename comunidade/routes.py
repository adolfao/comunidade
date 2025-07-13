from flask import render_template, redirect, url_for, flash, request
from comunidade import app
from comunidade.forms import FormLogin, FormCriarConta

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

    
  if 'botao_submit_login' in request.form and form_login.validate_on_submit():
    flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
    return redirect(url_for('home'))

    
  if 'botao_submit_criarconta' in request.form and form_criarconta.validate_on_submit():
    flash(f'Conta criada com sucesso no e-mail: {form_criarconta.email.data}', 'alert-success')
    return redirect(url_for('home'))

  return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)

  