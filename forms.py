from flask_wtf import FlaskForm #forms padrão
from wtforms import StringField, PasswordField, SubmitField, BooleanField #campo de texto, senha, botão de submit e lembrarlogin
from wtforms.validators import DataRequired, Length, Email, EqualTo #validações: é obrigatório?, satisfaz o tamanho?
                                                                    #é email?, é igual a?

class FormCriarConta(FlaskForm): 
  username = StringField('Nome de usuário', validators=[DataRequired()])
  email = StringField('E-mail', validators=[DataRequired(), Email()])
  senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
  confirmacao_senha = PasswordField('Confirmação de senha', validators=[DataRequired(), EqualTo('senha')])
  botao_submit_criarconta = SubmitField('Criar conta')
  
class FormLogin(FlaskForm):
  email = StringField('E-mail', validators=[DataRequired(), Email()])
  senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
  lembrar_dados = BooleanField('Lembrar de mim')
  botao_submit_login = SubmitField('Fazer login')