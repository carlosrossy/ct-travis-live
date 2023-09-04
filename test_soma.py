from soma import funcao_soma

def test_soma_positivos():
    assert funcao_soma(2, 3) == 5

def test_soma_positivos():
    assert funcao_soma(4, 3) == 7

def test_soma_negativos():
    assert funcao_soma(-2, -3) == -5

def test_soma_misto():
    assert funcao_soma(2, -3) == -1

def test_soma_incorreta():
    assert funcao_soma(2, 3) == 10