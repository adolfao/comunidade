from flask import render_template, redirect, url_for, flash, request
from comunidade import app, bcrypt
from comunidade.forms import FormLogin, FormCriarConta, FormEditarPerfil
from comunidade.models import Usuario
from comunidade.database import database
from flask_login import login_user, logout_user, current_user, login_required
import secrets, os
from PIL import Image

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

def salvar_imagem(imagem):
  codigo = secrets.token_hex(8)
  nome, extensao = os.path.splitext(imagem.filename)
  nome_arquivo = nome + codigo + extensao
  caminho_completo = os.path.join(app.root_path, 'static\\fotos_perfil', nome_arquivo)
  tamanho = (200, 200)
  imagem_reduzida = Image.open(imagem)
  imagem_reduzida.thumbnail(tamanho)
  imagem_reduzida.save(caminho_completo)
  return nome_arquivo

def atualizar_sobremim(form):
  lista_sobremim = []
  for campo in form:
    if 'sobremim_' in campo.name and campo.data:
      lista_sobremim.append(campo.label.text)
  return ';'.join(lista_sobremim)
  

@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
  form_editarperfil = FormEditarPerfil()
  if request.method == 'GET':
    form_editarperfil.username.data = current_user.username
    form_editarperfil.email.data = current_user.email   
  if form_editarperfil.validate_on_submit():
    current_user.email = form_editarperfil.email.data
    current_user.username = form_editarperfil.username.data
    if form_editarperfil.foto_perfil.data:
      nome_imagem = salvar_imagem(form_editarperfil.foto_perfil.data)
      current_user.foto_perfil = nome_imagem
    current_user.sobremim = atualizar_sobremim(form_editarperfil)
    database.session.commit()
    flash(f'Perfil atualizado com sucesso!', 'alert-success')
    return redirect(url_for('perfil'))
  foto_perfil = url_for('static', filename='fotos_perfil/{}' .format(current_user.foto_perfil))
  return render_template('editarperfil.html', foto_perfil=foto_perfil, form_editarperfil=form_editarperfil)  