# Testa os endpoints de clientes

def test_listar_clientes(client):
    """Testa o endpoint de listagem de clientes"""
    response = client.get("/clientes")
    assert response.status_code == 200
    
    data = response.json()
    assert "clientes" in data
    assert len(data["clientes"]) > 0
    
    # Verifica estrutura dos dados
    cliente = data["clientes"][0]
    assert "id" in cliente
    assert "nome" in cliente
    assert "tempo_restante" in cliente
    assert "tempo_original" in cliente

def test_consultar_cliente_especifico(client):
    """Testa consulta de cliente específico"""
    response = client.get("/clientes/1")
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == 1
    assert "nome" in data
    assert "tempo_restante" in data
    assert "tempo_original" in data

def test_consultar_cliente_inexistente(client):
    """Testa consulta de cliente que não existe"""
    response = client.get("/clientes/999")
    assert response.status_code == 404

def test_reset_tempo_cliente(client):
    """Testa reset de tempo do cliente"""
    novo_tempo = 50
    
    response = client.post(
        f"/clientes/1/reset_tempo",
        params={"novo_tempo": novo_tempo}  
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "resetado" in data["mensagem"].lower()
    assert str(novo_tempo) in data["mensagem"]