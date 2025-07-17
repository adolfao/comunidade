from flask import render_template, redirect, url_for, flash, request
from comunidade import app, bcrypt
from comunidade.forms import FormLogin, FormCriarConta
from comunidade.models import Usuario
from comunidade.database import database
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/usuarios')
@login_required
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
    usuario = Usuario.query.filter_by(email=form_login.email.data).first()
    if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
      login_user(usuario, remember=form_login.lembrar_dados.data)
      flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
      par_next = request.args.get('next')
      if par_next:
        return redirect(par_next)
      else:
        return redirect(url_for('home'))
    else:
      flash(f'Falha ao fazer login, e-mail ou senha incorretos!', 'alert-danger')
    
  if 'botao_submit_criarconta' in request.form and form_criarconta.validate_on_submit():
    senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
    usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
    database.session.add(usuario)
    database.session.commit()
    flash(f'Conta criada com sucesso no e-mail: {form_criarconta.email.data}', 'alert-success')
    return redirect(url_for('home'))

  return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)

@app.route('/sair')
@login_required
def sair():
  logout_user()
  flash(f'Logout feito com sucesso!', 'alert-success')
  return redirect(url_for('home'))

@app.route('/perfil')
@login_required
def perfil():
  foto_perfil = url_for('static', filename='fotos_perfil/{}' .format(current_user.foto_perfil))
  return render_template('perfil.html', foto_perfil=foto_perfil)

@app.route('/post/criar')
@login_required
def criar_post():
  return render_template('criarpost.html')