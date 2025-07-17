from flask_wtf import FlaskForm #forms padrão
from wtforms import StringField, PasswordField, SubmitField, BooleanField #campo de texto, senha, botão de submit e lembrarlogin
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError #validações: é obrigatório?, satisfaz o tamanho?
from comunidade.models import Usuario                                                  #é email?, é igual a?
from flask_login import current_user

class FormCriarConta(FlaskForm): 
  username = StringField('Nome de usuário', validators=[DataRequired()])
  email = StringField('E-mail', validators=[DataRequired(), Email()])
  senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
  confirmacao_senha = PasswordField('Confirmação de senha', validators=[DataRequired(), EqualTo('senha')])
  botao_submit_criarconta = SubmitField('Criar conta')
  
  def validate_email(self, email):
    usuario = Usuario.query.filter_by(email=email.data).first()
    if usuario:
      raise ValidationError("E-mail já cadastrado")
  
class FormLogin(FlaskForm):
  email = StringField('E-mail', validators=[DataRequired(), Email()])
  senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
  lembrar_dados = BooleanField('Lembrar de mim')
  botao_submit_login = SubmitField('Fazer login')
  
class FormEditarPerfil(FlaskForm):
  username = StringField('Nome de usuário', validators=[DataRequired()])
  email = StringField('E-mail', validators=[DataRequired(), Email()])
  botao_submit_editarperfil = SubmitField('Confirmar edição')
  
  def validate_email(self, email):
    #todo: verificar se o usuario realmente mudou de email
    usuario = Usuario.query.filter_by(email=email.data).first()
    if usuario: 
      raise ValidationError("E-mail já cadastrado")
  
  
#isso diz ao Flask-WTF: “este botão se chamará assim quando for enviado no formulário”
botao_submit_login = SubmitField('Fazer login', render_kw={'name': 'botao_submit_login'})
botao_submit_criarconta = SubmitField('Criar conta', render_kw={'name': 'botao_submit_criarconta'})
botao_submit_editarperfil = SubmitField('Confirmar edição', render_kw={'name': 'botao_submit_editarperfil'})