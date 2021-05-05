"""Vamos fazer um programa de leilão, entõa definiremos algumas classes"""
from programacao_py.testes_automatizados_tdd.excecoes import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if not self._valor_eh_valido(valor):
            raise LanceInvalido(f"Valor proposto maior que o disponível na carteira: {self.__carteira}")
        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -= valor

    def _valor_eh_valido(self, valor):
        return valor <= self.__carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.maior_lance = .0
        self.menor_lance = 0.0
        self.__lances = []

    def propoe(self, lance: Lance):
        if self._lance_eh_valido(lance):
            if self._nao_tem_lance():
                self.menor_lance = lance.valor
            self.__lances.append(lance)
            self.maior_lance = lance.valor

    @property
    def lances(self):
        return self.__lances[:]  # Cópia rasa para não alterar a nossa lista de

    def _nao_tem_lance(self):
        return not self.__lances

    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        else:
            raise LanceInvalido("O mesmo usuário não pode dar dois lances seguidos")

    def _lance_maior_que_o_anterior(self, lance):
        if self.__lances[-1].valor < lance.valor:
            return True
        else:
            raise LanceInvalido("O lance proposto não deve ser menor que o anterior")

    def _lance_eh_valido(self, lance):
        return self._nao_tem_lance() or self._usuarios_diferentes(lance) and self._lance_maior_que_o_anterior(lance)
