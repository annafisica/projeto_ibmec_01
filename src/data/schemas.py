"""
Schemas Pydantic para validação de dados
"""
from pydantic import BaseModel, Field
from typing import List

# Modelo de Clientes
class ClientesInput(BaseModel):
    """
    Schema para representar os dados de entrada de um cliente
    """    
    nome: str = Field(..., min_length=1, max_length=256, description="Nome do cliente")
    tempo: int = Field(..., ge=1, le=1000, description="Tempo de acesso remanescente do cliente")


class ClienteOutput(BaseModel):
    """
    Schema para representar os dados de saída de um cliente
    """
    id: int
    nome: str 
    tempo: int 

class TicketInput(BaseModel):
    ticket: str = Field(..., min_length=1, max_length=50, description="Código do ticket de acesso")


class TicketCreateInput(BaseModel):
    """
    Schema para entrada de dados para criação de um novo ticket de acesso.
    """
    codigo: str = Field(..., 
                      min_length=3, 
                      max_length=50, 
                      description="Código único do novo ticket (ex: TICKET_40)")
    valor: int = Field(..., 
                       ge=1, 
                       le=600, 
                       description="Valor em minutos que o ticket adiciona")

    class Config:
        json_schema_extra  = {
            "example": {
                "codigo": "TICKET_CUSTOM_25",
                "valor": 25
            }
        }