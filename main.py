from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
def home():
  return render_template('home.html')

lista_usuarios = ['Adolfo', 'João', 'José', 'Lucas']

@app.route('/usuarios')
def usuarios():
  return render_template('usuarios.html', lista_usuarios=lista_usuarios)
  
if __name__ == "__main__":
  app.run(debug=True)