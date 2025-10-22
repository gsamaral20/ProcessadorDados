import pytest
import datetime
from src.contrato import Vendas

def test_vendas_com_dados_validos():

    dados_validos = {
        "email": "comprador@example.com",
        "data": datetime.now(),
        "valor": 100.50,
        "produto": "Produto X",
        "quantidade": 3,
        "categoria": "categoria3"

    }

    venda = Vendas(**dados_validos)


