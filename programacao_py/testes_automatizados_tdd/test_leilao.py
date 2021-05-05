from unittest import TestCase

from programacao_py.testes_automatizados_tdd.excecoes import LanceInvalido
from programacao_py.testes_automatizados_tdd.leilao import Leilao, Lance, \
    Usuario


class TestLeilao(TestCase):
    """Novas regras do leilão

    * Se o leilão não tiver lances, deve permitir propor um lance

    * Se o último usuário for diferente, deve permitir propor um lance

    * Se o último usuário for o mesmo, não deve permitir propor um lance

    """
    def setUp(self) -> None:
        """Cria o cenário padrão para todos os métodos.

        É carregado antes de qualquer método que for testado"""
        self.jose = Usuario('José', 200.0)
        self.lance_jose = Lance(self.jose, 150.0)

        self.leilao = Leilao('Celular')

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):

        self.leilao.propoe(self.lance_jose)  # um lance feito

        quantidade_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(1, quantidade_de_lances_recebidos)  # checar um lance

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        keith = Usuario('Keith', 1000.0)
        lance_do_keith = Lance(keith, 780.0)

        self.leilao.propoe(self.lance_jose)  # primeiro lance
        self.leilao.propoe(lance_do_keith)  # segundo lance, usuário diferente

        quantidade_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebidos)  # checar dois lances

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        try:
            primeiro_lance = self.leilao.propoe(self.lance_jose)
            novo_lance = Lance(self.jose, 50.0)
            self.leilao.propoe(novo_lance)
            self.fail(msg="Não lançou exceção")
        except LanceInvalido:
            quantidade_de_lances_recebidos = len(self.leilao.lances)

            self.assertEqual(1, quantidade_de_lances_recebidos)

    def nao_deve_permitir_propor_lance_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            keith = Usuario('Keith', 1000.0)
            lance_keith = Lance(keith, 789.0)

            self.leilao.propoe(self.lance_jose)
            self.leilao.propoe(lance_keith)

    def deve_retornar_o_maior_e_o_maior_valor_de_lance_quando_adicionados_em_ordem_crescente(self):
        keith = Usuario('Keith', 1000.0)
        lance_keith = Lance(keith, 789.0)

        self.leilao.propoe(self.lance_jose)
        self.leilao.propoe(lance_keith)

        menor_valor_esperado = 150.0
        maior_valor_esperado = 789.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        keith = Usuario('Keith', 1000.0)
        assiris = Usuario('Assiris', 700.0)

        lance_keith = Lance(keith, 789.0)
        lance_assiris = Lance(assiris, 152.0)

        self.leilao.propoe(self.lance_jose)
        self.leilao.propoe(lance_assiris)
        self.leilao.propoe(lance_keith)

        menor_valor_esperado = 150.0
        maior_valor_esperado = 789.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
