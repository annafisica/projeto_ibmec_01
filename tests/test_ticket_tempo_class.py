# Testa a classe TicketTempo

# CORREÇÃO: Importação correta
from src.api.ticket_tempo import TicketAcesso

def test_ticket_valido_add_acrescimo():
    ticket = TicketAcesso("TICKET_10")
    
    assert ticket.is_valid is True
    assert ticket.get_fator_acrescimo() == 10
    
    tempo_novo = ticket.aplicar_acrescimo(tempo_restante=30)
    assert tempo_novo == 40      # 30 + 10   
    
def test_ticket_invalido_nao_add_tempo():
    ticket = TicketAcesso("TICKET_INVALIDO")
        
    assert ticket.is_valid is False
    assert ticket.get_fator_acrescimo() == 0
    
    tempo_novo = ticket.aplicar_acrescimo(tempo_restante=30)
    assert tempo_novo == 30      # Sem alteração no tempo

def test_ticket_classe_methods():
    """Testa os métodos de classe para adicionar e remover tickets"""
    # Testa adicionar novo ticket
    codigo_novo = "TICKET_TESTE_25"
    TicketAcesso.adicionar_ticket(codigo_novo, 25)
    
    # Verifica se foi adicionado
    assert codigo_novo in TicketAcesso.ticket_acesso
    assert TicketAcesso.ticket_acesso[codigo_novo] == 25
    
    # Testa remover ticket
    resultado = TicketAcesso.remover_ticket(codigo_novo)
    assert resultado is True
    assert codigo_novo not in TicketAcesso.ticket_acesso
    
    # Testa remover ticket inexistente
    resultado = TicketAcesso.remover_ticket("TICKET_INEXISTENTE")
    assert resultado is False