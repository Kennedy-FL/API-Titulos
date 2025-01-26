import pytest
from main import app

# Fixture para configurar o cliente de teste
@pytest.fixture
def client():
    app.testing = True  # Habilita o modo de teste no Flask
    with app.test_client() as client:
        yield client

# Teste do endpoint '/Titulos' para verificar se todos os títulos são retornados
def test_obter_todos_os_titulos(client):
    response = client.get('/Titulos')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0

# Teste do endpoint '/Titulos/<ano>' para verificar os títulos de um ano específico
def test_obter_titulo_por_ano(client):
    response = client.get('/Titulos/2012')
    assert response.status_code == 200
    titulos = response.json
    assert all(titulo['ano'] == 2012 for titulo in titulos)

# Teste do endpoint '/Titulos/<ano>' para o ano com título inexistente
def test_obter_titulo_por_ano_inexistente(client):
    response = client.get('/Titulos/2025')
    assert response.status_code == 200
    assert len(response.json) == 0
