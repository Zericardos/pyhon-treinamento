from unittest import TestCase

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
        self.jose = Usuario('José')
        self.lance_jose = Lance(self.jose, 150.0)

        self.leilao = Leilao('Celular')

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):

        self.leilao.propoe(self.lance_jose)  # um lance feito

        quantidade_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(1, quantidade_de_lances_recebidos)  # checar um lance

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        keith = Usuario('Keith')
        lance_do_keith = Lance(keith, 780.0)

        self.leilao.propoe(self.lance_jose)  # primeiro lance
        self.leilao.propoe(lance_do_keith)  # segundo lance, usuário diferente

        quantidade_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebidos)  # checar dois lances

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        primeiro_lance = self.leilao.propoe(self.lance_jose)
        novo_lance = Lance(self.jose, 100.0)
        self.leilao.propoe(novo_lance)

        quantidade_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(1, quantidade_de_lances_recebidos)  # Não deixar
        # passar dois lances de mesmo usuário. Fiz modificação na classe para o
        # teste passar

    def deve_retornar_o_maior_e_o_maior_valor_de_lance_quando_adicionados_em_ordem_decrescente(self):
        # self.fail()  # se executar essa linha, o programa falha imediatamente
        keith = Usuario('Keith')

        lance_keith = Lance(keith, 789.0)

        self.append(self.lance_jose)
        self.leilao.propoe(lance_keith)



        menor_valor_esperado = 150.0
        maior_valor_esperado = 789.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def deve_retornar_o_maior_e_o_maior_valor_de_lance_quando_adicionados_em_ordem_crescente(self):
        keith = Usuario('Keith')
        lance_keith = Lance(keith, 789.0)

        self.leilao.propoe(self.lance_jose)
        self.leilao.propoe(lance_keith)



        menor_valor_esperado = 150.0
        maior_valor_esperado = 789.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        keith = Usuario('Keith')
        assiris = Usuario('Assiris')

        lance_keith = Lance(keith, 789.0)
        lance_assiris = Lance(assiris, 150.0)

        self.leilao.propoe(self.lance_jose)
        self.leilao.propoe(lance_keith)
        self.leilao.propoe(lance_assiris)

        

        menor_valor_esperado = 150.0
        maior_valor_esperado = 789.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
