# projeto_ibmec_01
Projeto para Avaliação da Disciplina de Engenharia de Software, Prof. Luis Fernando Lufe Mello Barreto - MBA/IBMEC
Estudantes: Vitor Zago, Anna Lara, Giselle Dias, 

Trata-se de uma aplicação **FastAPI** para gerenciar o **tempo de acesso dos clientes**, permitindo consultar tempo restante, aplicar acréscimo através de tickets e reinicializar o tempo de uso.

---

## EndPoint 1 – `/clientes`

Retorna **todos os clientes cadastrados**, incluindo:

- Tempo restante atualizado  
- Tempo original configurado  
- Cálculo automático baseado no tempo decorrido desde o início da API

### **Método**
`GET /clientes`

### **Retorno esperado**
```json
{
  "clientes": [
    {
      "id": 1,
      "nome": "Gisele",
      "tempo_restante": 30.0,
      "tempo_original": 30
    }
  ]
}
```

## EndPoint 2 – `/clientes/{cliente_id}`

Retorna informações detalhadas de um único cliente:

- Tempo restante
- Tempo original
- Momento de inicialização da API

### **Método**
`GET /clientes/{cliente_id}`

### **Exemplo de Retorno**
```json
{
  "id": 1,
  "nome": "Gisele",
  "tempo_restante": 27.5,
  "tempo_original": 30,
  "api_iniciada_em": "2025-11-22T14:30:00.000Z"
}
```

## POST – /clientes/{cliente_id}/calcular_tempo

Aplica um acréscimo de tempo baseado em um ticket verificado pela classe TicketAcesso.

Corpo da requisição0
{
  "ticket": "ABC123"
}

### ***Exemplo de Retorno***
```json
{
  "id": 1,
  "nome": "Gisele",
  "tempo_restante_anterior": 12.5,
  "acrescimo_aplicado": 15,
  "novo_tempo_restante": 27.5,
  "novo_tempo_total": 42.5,
  "tempo_decorrido": 17.0
}
```

## POST – /clientes/{cliente_id}/reset_tempo

Endpoint utilizado para testes, permitindo redefinir o tempo total de um cliente.

Exemplo
```json
{
  "novo_tempo": 60
}
```

## → Outros Endpoints
✓ / – Home
Retorna mensagem de boas-vindas.

✓ /health
Retorna informações da API:
Status
Tempo de operação
Versão
Horário de inicialização

## ★ Funcionamento Interno

A API registra o horário de início no evento startup.
Cada cliente possui um tempo inicial configurado.
A função calcular_tempo_restante() recalcula o tempo restante usando:
Tempo inicial
Tempo decorrido desde o start
Tickets válidos podem adicionar minutos ao tempo restante.
* O “banco de dados” é limitado e carregado em memória, para fins de demonstração.

## ⇒ Como Executar o Projeto
1. Instale as dependências
pip install fastapi uvicorn pydantic (ou instale a partir do arquivo requirements.txt)

2. Execute o servidor
uvicorn src.api.main:app

3. Acesse a documentação
http://127.0.0.1:8000/docs