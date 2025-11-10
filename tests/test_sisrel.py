import re
from datetime import datetime, timedelta

import pytest

from sisrel import Venda, calcular_media, filtrar_por_produto, gerar_vendas


def test_calcular_media_funciona():
    vendas = [
        Venda("Camiseta", 100.0, datetime(2024, 1, 10)),
        Venda("Calça", 300.0, datetime(2024, 1, 11)),
    ]
    assert calcular_media(vendas) == pytest.approx(200.0)


def test_calcular_media_lista_vazia_erro():
    with pytest.raises(ValueError):
        calcular_media([])


def test_filtrar_por_produto():
    vendas = [
        Venda("Tênis", 150.0, datetime(2024, 1, 10)),
        Venda("Camiseta", 80.0, datetime(2024, 1, 10)),
        Venda("Tênis", 200.0, datetime(2024, 1, 11)),
    ]
    apenas_tenis = filtrar_por_produto(vendas, "Tênis")
    assert len(apenas_tenis) == 2
    assert all(v.produto == "Tênis" for v in apenas_tenis)


def test_gerar_vendas_basico():
    qtd = 12
    vendas = gerar_vendas(qtd)
    assert len(vendas) == qtd
    now = datetime.now()
    for v in vendas:
        assert v.produto in ['Camiseta', 'Calça', 'Tênis', 'Boné']
        assert 50 <= v.valor <= 500
        # datas entre 1 e 30 dias atrás
        assert now - timedelta(days=31) < v.data <= now - timedelta(days=0)


def test_venda_str_format():
    v = Venda("Boné", 123.456, datetime(2024, 5, 9))
    s = str(v)
    # "Boné - R$123.46 em 09/05/2024"
    assert "Boné" in s
    assert "R$123.46" in s
    assert re.search(r"\b09/05/2024\b", s)
