import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Teste para a rota de obter todos os títulos
def test_obter_todos_os_titulos(client):
    response = client.get('/Titulos')
    assert response.status_code == 200  # Verifica se a resposta foi bem-sucedida
    assert isinstance(response.json, list)  # Verifica se a resposta é uma lista

# Teste para a rota de obter títulos por ano existente
def test_obter_titulos_por_ano_existente(client):
    response = client.get('/Titulos/2012')
    assert response.status_code == 200
    assert len(response.json) > 0  # Verifica se há títulos retornados

# Teste para a rota de ano inexistente
def test_obter_titulos_por_ano_inexistente(client):
    response = client.get('/Titulos/1999')
    assert response.status_code == 404  # Deve retornar erro para ano não encontrado
    assert response.json['erro'] == 'Nenhum título encontrado para esse ano'
