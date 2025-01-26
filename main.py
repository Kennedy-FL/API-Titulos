from flask import Flask, jsonify
from bd import Titulos

app = Flask(__name__)

# Consultar todos
@app.route('/Titulos',methods=['GET'])
def obter_titulos():
    return jsonify(Titulos)

# Consultar por ano
@app.route('/Titulos/<int:ano>',methods=['GET'])
def obter_titulo_por_ano(ano):
    titulos_encontrados = [titulo for titulo in Titulos if titulo.get('ano') == ano]
    # titulo for titulo in Titulos → Para cada item na lista Titulos, pegue o titulo.
    # if titulo.get('ano') == ano → Só adiciona à nova lista se o ano for igual ao buscado.
    if titulos_encontrados:
        return jsonify(titulos_encontrados) 
    else:
        return jsonify([])  # Retorna uma lista vazia quando não encontrar nenhum título    
# app.run(port=5000,host='localhost',debug=True)