"""Vamos fazer um programa de leilão, entõa definiremos algumas classes"""
import sys


class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.maior_lance = sys.float_info.min  # Para garantir o maior lance
        self.menor_lance = sys.float_info.max  # Para garantir o menor lance
        self.__lances = []

    def propoe(self, lance: Lance):
        if not self.__lances or self.__lances[-1].usuario != lance.usuario \
                and self.__lances[-1].valor < lance.valor:
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise ValueError("Erro ao propor lance")
    @property
    def lances(self):
        return self.__lances[:]  # Cópia rasa para não alterar a nossa lista de
    # lances

"""
class Avaliador:
    ""Avalia  os lances e atualiza com o valor dado

    ""
    def __init__(self):
        ""Inicia o Avaliador""
        self.maior_lance = sys.float_info.min  # Para garantir o maior lance
        self.menor_lance = sys.float_info.max  # Para garantir o menor lance


    def avalia(self, leilao: Leilao):
        ""Faz a avaliação""
        for lance in leilao.lances:
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
"""