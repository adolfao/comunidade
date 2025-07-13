from comunidade.database import database
from datetime import datetime

class Usuario(database.Model): 
  id = database.Column(database.Integer, primary_key=True) #o id é uma coluna de inteiros do meu db e é a chave primária
  username = database.Column(database.String, nullable=False)                     #que seria o que é único nele e será
  senha = database.Column(database.String, nullable=False)                      #usado para identificá-lo
  email = database.Column(database.String, nullable=False, unique=True) #nullable=False -> não pode ser vazio
  foto_perfil = database.Column(database.String, default='default.jpg')#unique=True -> deve ser único      
                                                 #por padrão, a foto do usuário vai ser a default, ele pode mudar dps
  #como um usuario pode ter vários posts e ñ o contrário, essa relação será criada aqui
  posts = database.relationship('Post', backref='autor', lazy=True)#lazy=True significa que quando eu chamar essa função
  #ela vai me retornar todas as informações sobre o autor, não preciso ficar passando cada uma de uma vez    
                                   #backref é como eu vou chamar a função, que no caso seria posts.autor
  informacoes = database.Column(database.String, default='Não informado', nullable=False)
  #como o usuario n consegue entrar falando as informacoes dele, temnos que colocar um default
  #para o nullable n dar problema
            
class Post(database.Model):
  id = database.Column(database.Integer, primary_key=True)
  titulo = database.Column(database.String, nullable=False)
  corpo = database.Column(database.Text, nullable=False) #para textos maiores n se usa string e sim text
  data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow) 
  usuario_id = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False) #mesmo a classe sendo
  #iniciada com a letra maiuscula, aqui deve ser passada com a minuscula
#sobre o datetime, caso vc coloque parentes no utcnow(), ele será caso vc coloque parentes no utcnow(), ele será
#preenchido sempre com o horário de agora, ele seria fixo sem o parentes ele é uma função que sempre roda quando é chamado
