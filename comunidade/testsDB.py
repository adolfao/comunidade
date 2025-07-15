#arquivo criado para testar o database com comandos
from comunidade.database import database
from comunidade.models import Usuario
from comunidade import app

#para rodar: python -m comunidade.testsDB (na raiz)

with app.app_context():
  Usuario.query.all()
  print(Usuario)
  for usuario in Usuario.query.all():
    print(usuario.id, usuario.username, usuario.email, usuario.senha)