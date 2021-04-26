from unittest import TestCase

from programacao_py.testes_automatizados_tdd.dominio import Leilao, Lance, \
    Usuario


class TestAvaliador(TestCase):

    def setUp(self) -> None:
        """Cria o cenário padrão para todos os métodos.
        É carregado antes de qualquer método que for testado"""
        self.jose = Usuario('José')
        self.lance_jose = Lance(self.jose, 150.0)

        self.leilao = Leilao('Celular')

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
