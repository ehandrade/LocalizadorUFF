import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')

@app.route('/Entrar')
def entrar_page():
    return render_template('Entrar.html')

@app.route('/index')
def index_page():
    return render_template('index.html')

@app.route('/Localizacao')
def localizacao_page():
    return render_template('Localizacao.html')

@app.route('/Cadastro')
def cadastro_page():
    return render_template('Cadastro.html')

@app.route('/QuemSomos')
def quem_page():
    return render_template('QuemSomos.html')

@app.route('/teste')
def teste_page():
    return render_template('teste.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port= port)
