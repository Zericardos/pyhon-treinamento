# Conteúdo do projeto

## Aquisição de dados

### Teste test_executar_requisicao_retorna_tipo_string

Queremos testar a função *executar_requisicao* da *SUT (System Under Test)*

def test_executar_requisicao_retorna_tipo_string(): **Inicia o teste**
    with patch("programacao_py.dubles_de_testes.colecao.livros.urlopen", duble_de_urlopen): **substitui a função urlopen pela função** *duble_de_urlopen*
        resultado = executar_requisicao("https://buscador?autor=Jk+Rowlings")
    assert type(resultado) == str


