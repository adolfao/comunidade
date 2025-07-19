#arquivo criado para testar o database com comandos
from comunidade.database import database
from comunidade.models import Usuario
from comunidade import app

#para rodar: python -m comunidade.testsDB (na raiz)

with app.app_context():
    usuarios = Usuario.query.all()
    print("Lista de usuários:")
    for usuario in usuarios:
        print(f"Email: {usuario.email} | Sobre mim: {usuario.sobremim}")