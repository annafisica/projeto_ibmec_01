# src/tests/conftest.py - definição de fixtures para o pytest

import sys
from pathlib import Path
from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

# Adicionar a pasta src/ ao sys.path para conseguir importar módulos da aplicação
SRC_DIR = Path(__file__).resolve().parents[1]

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
    

from src.api.main import app


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    """
    Fixture para fornecer um cliente de teste FastAPI.
    Isso permite que os testes façam requisições à aplicação sem precisar rodar um servidor real.
    O TestClient dispara os eventos de inicialização (startup) e desligamento (shutdown) automaticamente para cada teste que o utiliza.
    """
    with TestClient(app) as c:
        yield c