from programacao_py.testes_automatizados_tdd.leilao import Usuario, Leilao
import pytest


@pytest.fixture
def jose():
     return Usuario('Jose', 100.0)

@pytest.fixture
def leilao():
    return Leilao('Celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(jose,leilao):
    jose.propoe_lance(leilao, 50.0)

    assert jose.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(jose,leilao):
    jose.propoe_lance(leilao, 1.0)

    assert jose.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_que_o_valor_da_carteira(jose,leilao):

    jose.propoe_lance(leilao, 100.0)

    assert jose.carteira == 0

def test_nao_deve_permitir_propor_lance_quando_o_valor_eh_maior_que_o_valor_da_carteira(jose,leilao):
    with pytest.raises(ValueError):
        jose.propoe_lance(leilao, 200.0)
