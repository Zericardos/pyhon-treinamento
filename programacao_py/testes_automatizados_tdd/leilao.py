"""Vamos fazer um programa de leilão, entõa definiremos algumas classes"""
import sys


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if valor <= self.__carteira:
            lance = Lance(self, valor)
            leilao.propoe(lance)
            self.__carteira -= valor
        else:
            raise ValueError(f"Valor proposto maior que o disponível na carteira: {self.__carteira}")

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