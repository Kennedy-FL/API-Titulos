import pytest
from main import app

# Fixture para configurar o cliente de teste
@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

# Teste do endpoint '/Titulos' para verificar se todos os títulos são retornados
def test_obter_todos_os_titulos(client):
    # Fazendo a requisição GET para '/Titulos'
    response = client.get('/Titulos')
    
    # Verificando se o status code da resposta é 200 (OK)
    assert response.status_code == 200
    
    # Verificando se a resposta é uma lista (ou seja, JSON)
    assert isinstance(response.json, list)

    # Verificando se a resposta contém títulos
    assert len(response.json) > 0

# Teste do endpoint '/Titulos/<ano>' para verificar os títulos de um ano específico
def test_obter_titulo_por_ano(client):
    # Fazendo a requisição GET para '/Titulos/2012'
    response = client.get('/Titulos/2012')
    
    # Verificando se o status code da resposta é 200 (OK)
    assert response.status_code == 200
    
    # Verificando se a resposta contém títulos de 2012
    titulos = response.json
    assert all(titulo['ano'] == 2012 for titulo in titulos)

# Teste do endpoint '/Titulos/<ano>' para o ano com título inexistente
def test_obter_titulo_por_ano_inexistente(client):
    # Fazendo a requisição GET para '/Titulos/2025', que não existe
    response = client.get('/Titulos/2025')
    
    # Verificando se o status code da resposta é 200 (OK)
    assert response.status_code == 200
    
    # Verificando se a resposta está vazia, pois não deve haver títulos para 2025
    assert len(response.json) == 0
