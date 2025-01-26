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
    if titulos_encontrados:
        return jsonify(titulos_encontrados) 
        
app.run(port=5000,host='localhost',debug=True)