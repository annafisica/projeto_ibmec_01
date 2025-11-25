# Testa a api de tickets
# Garante que um ticket válido (ex: TICKET_5) aumente o tempo restante do cliente exatamente pelo fator do ticket.

import pytest

def test_ticket_valido_api(client):
    """Testa aplicação de ticket válido via API"""
    client_id = 1
    
    # Primeiro obtém o estado atual do cliente
    response_cliente = client.get(f"/clientes/{client_id}")
    tempo_anterior = response_cliente.json()["tempo_restante"]
    
    # Aplica o ticket
    response = client.post(
        f"/clientes/{client_id}/calcular_tempo", 
        json={"ticket": "TICKET_5"},
    )
    
    assert response.status_code == 200
    data = response.json()
    
    assert "tempo_restante_anterior" in data
    assert "novo_tempo_restante" in data
    assert "acrescimo_aplicado" in data
    assert data["acrescimo_aplicado"] == 5
    assert data["novo_tempo_restante"] == pytest.approx(
        data["tempo_restante_anterior"] + 5,
        rel=1e-2,
    )

def test_ticket_invalido_api(client):
    """Testa tentativa de usar ticket inválido via API"""
    client_id = 1
    
    response = client.post(
        f"/clientes/{client_id}/calcular_tempo", 
        json={"ticket": "TICKET_INVALIDO"},
    )
    
    assert response.status_code == 400
    data = response.json()
    assert "Ticket inválido" in data["detail"]

def test_criar_e_deletar_ticket_api(client):
    """Testa criação e deleção de tickets customizados via API"""
    # Cria novo ticket
    ticket_data = {
        "codigo": "TICKET_TESTE_15",
        "valor": 15
    }
    
    response = client.post("/tickets", json=ticket_data)
    assert response.status_code == 200
    data = response.json()
    assert "sucesso" in data["mensagem"].lower()
    assert ticket_data["codigo"] in data["tickets_disponiveis"]
    
    # Tenta criar ticket duplicado
    response = client.post("/tickets", json=ticket_data)
    assert response.status_code == 400
    
    # Deleta o ticket
    response = client.delete(f"/tickets/{ticket_data['codigo']}")
    assert response.status_code == 200
    data = response.json()
    assert "removido" in data["mensagem"].lower()
    assert ticket_data["codigo"] not in data["tickets_disponiveis_atualizados"]
    
    # Tenta deletar ticket inexistente
    response = client.delete("/tickets/TICKET_INEXISTENTE")
    assert response.status_code == 404