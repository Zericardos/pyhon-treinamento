from unittest.mock import (
    patch,
    mock_open,
    Mock,
    MagicMock,
)
from unittest import skip
import pytest
from programacao_py.dubles_de_testes.colecao.livros import consultar_livro, executar_requisicao


class StubHTTPResponse:
    def read(self):
        return b""  # retorna bytes

    def __enter__(self):  # método necessário para objeto entrar no gerenciador de contexto with
        return self

    def __exit__(self, parametro1, parametro2, parametro3):  # método necessário para objeto entrar no gerenciador
        pass  # de contexto with


# @skip("Deve ser testado quando consultar_livro estiver completo")
@patch("programacao_py.dubles_de_testes.colecao.livros.urlopen", return_value=StubHTTPResponse())
def test_consultar_livro_retorna_formato_resultado_string(stub_urlopen):
    resultado = consultar_livro("Sakurai, Quantum Mechanics")
    assert type(resultado) == str

# @skip
@patch("programacao_py.dubles_de_testes.colecao.livros.urlopen", return_value=StubHTTPResponse())
def test_consultar_livros_chama_preparar_dados_para_requisicao_apenasumavezcomosmesmos_parametros_de_consultar_livros(
stub_urlopen
):
    with patch("programacao_py.dubles_de_testes.colecao.livros.preparar_dados_para_requisicao") as duble:
        consultar_livro("Sakurai, Quantum Mechanics")
        duble.assert_called_once_with("Sakurai, Quantum Mechanics")
    pass

# @skip
@patch("programacao_py.dubles_de_testes.colecao.livros.urlopen", return_value=StubHTTPResponse())
def test_consultar_chama_obter_url_usando_como_parametro_o_retorno_de_preparar_dados_para_requisicao(stub_urlopen):
    with patch("programacao_py.dubles_de_testes.colecao.livros.preparar_dados_para_requisicao") as stub_preparar:
        dados = {"autor": "Sakurai"}
        stub_preparar.return_value = dados  # obter_url ainda não está implementado, por isso usamos o dublê spy
        with patch("programacao_py.dubles_de_testes.colecao.livros.obter_url") as spy_obter_url:
            consultar_livro("Sakurai")
            spy_obter_url.assert_called_once_with("https://buscador", dados)

# @skip
@patch("programacao_py.dubles_de_testes.colecao.livros.urlopen", return_value=StubHTTPResponse())
def test_consultar_livros_chama_executar_requisicao_usando_retorno_obter_url(stub_urlopen):
    with patch("programacao_py.dubles_de_testes.colecao.livros.obter_url") as stub_obter_url:
        stub_obter_url.return_value = "https://buscador"
        with patch("programacao_py.dubles_de_testes.colecao.livros.executar_requisicao") as spy_executar_requisicao:
            consultar_livro("Sakurai")  # executar_requisicao já está implementado, mas o objetivo aqui é verificar
            spy_executar_requisicao.assert_called_once_with("https://buscador")  # se ele recebe os parâmetros devidos


def stub_de_urlopen(url, timeout):
    return StubHTTPResponse()


def test_executar_requisicao_retorna_tipo_string():
    with patch("programacao_py.dubles_de_testes.colecao.livros.urlopen", stub_de_urlopen):
        resultado = executar_requisicao("https://buscador?autor=Jk+Rowlings")
    assert type(resultado) == str


def test_executar_requisicao_retorna_tipo_string_objeto_tipo_mock():
    with patch("programacao_py.dubles_de_testes.colecao.livros.urlopen") as stub_de_url_open:  # patch retorna objeto
        stub_de_url_open.return_value = StubHTTPResponse()
        resultado = executar_requisicao("https://buscador?autor=Jk+Rowlings")  # tipo Magic         Mock que tem
    assert type(resultado) == str  # método return_value

# os dois últimos testes testam a mesma coisa, mas fazem com abordagens diferentes

def test_executar_requisicao_retorna_tipo_string_terceira_abordagem():
    with patch("programacao_py.dubles_de_testes.colecao.livros.urlopen", return_value=StubHTTPResponse()):
        resultado = executar_requisicao("https://buscador?autor=Jk+Rowlings")
    assert type(resultado) == str


@patch("programacao_py.dubles_de_testes.colecao.livros.urlopen", return_value=StubHTTPResponse())
def test_executar_requisicao_retorna_tipo_string_quarta_abordagem(duble_de_url_open):
    resultado = executar_requisicao("https://buscador?autor=Jk+Rowlings")
    assert type(resultado) == str


from urllib.error import HTTPError


@patch("programacao_py.dubles_de_testes.colecao.livros.urlopen")  # quando criamos o decorador, obrigatoriamente devemos
def test_executar_requisicao_retorna_tipo_string_quinta_abordagem(duble_de_url_open):  # colocar a variável
    duble_de_url_open.return_value = StubHTTPResponse()
    resultado = executar_requisicao("https://buscador?autor=Jk+Rowlings")
    assert type(resultado) == str


class Dummy:  # é um dublê que serve para substituir parâmetros obrigatórios que não são relevantes para o teste. Não
    pass  # fazem parte do teste


def duble_de_urlopen_que_levanta_excecao_http_error(url, timeout):  # a função deve receber os mesmos parâmetros que a
    fp = mock_open  # a função que substitui; mock_open simula um gerenciador de contexto e exige atributo close
    fp.close = Dummy  # precisamos desse gerenciador de contexto porque urlopen inicia um, por isso usamos o método
    raise HTTPError(Dummy(), Dummy(), "mensagem de erro", Dummy(), fp)  # close. Podemos substituir o objeto Dummy por
# Mock() sem problemas

@skip
def test_executar_requisicao_levanta_excecao_do_tipo_http_error():  # objetivo aqui é verificar se levanta a exceção
    with patch("programacao_py.dubles_de_testes.colecao.livros.urlopen",  # problemas na internet podem ocorrer por
               duble_de_urlopen_que_levanta_excecao_http_error):  # motivos
        with pytest.raises(HTTPError) as excecao:
            executar_requisicao("http")
        assert "mensagem de erro" in str(excecao.value)

@skip
@patch("programacao_py.dubles_de_testes.colecao.livros.urlopen")
def test_executar_requisicao_levanta_excecao_do_tipo_http_error_segunda_abordagem(duble_de_urlopen):
    fp = mock_open
    fp.close = Dummy
    duble_de_urlopen.side_effect = HTTPError(Dummy(), Dummy(), "mensagem de erro", Dummy(), fp)  # side_effect não
    with pytest.raises(HTTPError) as excecao:  # retorna um valor ao dublê como return_value, mas uma exceção
        executar_requisicao("http")
        assert "mensagem de erro" in str(excecao.value)


def test_executar_requisicao_loga_mensagem_de_erro_de_http_error(caplog):  # como queremos levantar o resultado da
    with patch("programacao_py.dubles_de_testes.colecao.livros.urlopen",  # excecao, devemos defini-la na funcao que
               duble_de_urlopen_que_levanta_excecao_http_error):  # leva ela, no caso, executar_requisicao
        resultado = executar_requisicao("http")  # caplog é uma fixture do pytest
        mensagem_de_erro = "mensagem de erro"
        assert len(caplog.records) == 1  # verifica se só há uma mensagem, é um iterável
        for registro in caplog.records:
            assert mensagem_de_erro in registro.message
"""O teste anterior infere tratar as exceções que envolvem o dublê. Para isso a função executar_requisicao foi
modificada. Com isso, os dois testes anteriores deixaram de funcionar"""


@patch("programacao_py.dubles_de_testes.colecao.livros.urlopen")
def test_executar_requisicao_loga_mensagem_de_erro_de_http_error_segunda_abordagem_mock(duble_de_url_open, caplog):
    fp = mock_open
    fp.close = Dummy
    duble_de_url_open.side_effect = HTTPError(Dummy(), Dummy(), "mensagem de erro", Dummy(), fp)
    executar_requisicao("http//")
    assert len(caplog.records) == 1
    for registro in caplog.records:
        assert "mensagem de erro" in registro.message
