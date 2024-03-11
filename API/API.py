from flask import Flask, jsonify, request
from livros import Livros

app = Flask(__name__)

@app.route('/')
def bem_vindo():
    return "Bem-vindo ao livros! Esta é uma API para consultar livros que estão em uma lista de dicionários."

@app.route('/Livros')
def consultar_all_livros():
    return jsonify(Livros)

@app.route('/Livros/<int:id>', methods=['GET'])
def consultar_id(id):
    for livro in Livros:
        if livro['id'] == id:
            return jsonify(livro)



app.run(port=5000, host='localhost', debug=True)
# http://localhost:5000/Livros
