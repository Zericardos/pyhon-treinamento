import logging
from urllib.error import HTTPError
from urllib.request import urlopen


def consultar_livro(autor: str = ""):
    dados = preparar_dados_para_requisicao(autor)
    url = obter_url("https://buscador", dados)
    retorno = executar_requisicao(url)
    return retorno


def preparar_dados_para_requisicao(livro):
    pass


def obter_url(url, dados):
    pass


def executar_requisicao(url):
    try:
        with urlopen(url, timeout=10) as resposta:
            resultado = resposta.read().decode("utf-8")  # read() retorna objeto tipo bytes então codificamos para utf-8
    except HTTPError as excecao:
        logging.exception(f"Ao acessar {url}: {excecao}")
    else:
        return resultado
