class TicketAcesso:
    """
    Classe para gerenciar tickets de tempo de acesso.
    """
    
    # Dicionário estático de tickets de acesso válidos
    ticket_acesso = {"TICKET_10": 10, "TICKET_5": 5, "TICKET_2": 2}

    @classmethod
    def adicionar_ticket(cls, codigo: str, valor: int) -> None:
        """
        Adiciona um novo ticket ao dicionário estático da classe.
        """
        cls.ticket_acesso[codigo] = valor

    @classmethod
    def remover_ticket(cls, codigo: str) -> bool:
        """
        Remove um ticket do dicionário estático da classe.
        Retorna True se o ticket foi removido, False se não foi encontrado.
        """
        if codigo in cls.ticket_acesso:
            del cls.ticket_acesso[codigo]
            return True
        return False

    def __init__(self, codigo: str):
        self.codigo = codigo
        self.is_valid = codigo in self.__class__.ticket_acesso
        self.fator_acrescimo = self.__class__.ticket_acesso.get(codigo, 0)

    def aplicar_acrescimo(self, tempo_restante: float) -> float:
        """
        Retorna o tempo restante de acesso acrescido do bonus do ticket.
        """
        return tempo_restante + self.fator_acrescimo

    def get_fator_acrescimo(self) -> int:
        """
        Retorna o valor do fator de acrescimo do ticket.
        """
        return self.fator_acrescimo