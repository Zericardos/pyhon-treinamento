#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 05:24:49 2021

@author: ricardo
"""


from abc import ABCMeta, abstractmethod


class Imposto(object):
    """
    Serve para composição de impostos.

    Mas não será herdada por todos os impostos porque a classe
    Template_de_imposto_condicional já faz isso com os impostos IKCV e ICPP.
    Já que ela fornece o esqueleto para IKCV, ICPP, podemos atribuir a soma
    do próximo imposto naquela parte Template_de_imposto_condicional
    """

    __metaclass__ = ABCMeta

    def __init__(self, outro_imposto=None):
        self.__outro_imposto = outro_imposto

    def calculo_do_outro_imposto(self, orcamento):
        if self.__outro_imposto is None:
            return 0
        else:
            return self.__outro_imposto.calcula(orcamento)

    @abstractmethod
    def calcula(self, orcamento):
        pass

    def __str__(self):
        if self.__outro_imposto is None:
            return ''
        else:
            return f" com {self.__outro_imposto.__str__()}"


class Template_de_imposto_condicional(Imposto):
    __metaclass__ = ABCMeta
    # categoriza uma meta classe. Ela será herdada por suas classes filhas

    def calcula(self, orcamento):
        if self.must_use_tax_maximum(orcamento):
            return self.tax_maximum(orcamento) +\
                self.calculo_do_outro_imposto(orcamento)
        else:
            return self.tax_minimum(orcamento) +\
                self.calculo_do_outro_imposto(orcamento)

    @abstractmethod
    def must_use_tax_maximum(self, orcamento):
        pass

    @abstractmethod
    def tax_maximum(self, orcamento):
        pass

    @abstractmethod
    def tax_minimum(self, orcamento):
        pass


class ICMS(Imposto):
    def calcula(self, orcamento):

        return orcamento.value * .1 + self.calculo_do_outro_imposto(orcamento)

    def __str__(self):
        return 'ICMS' + str(Imposto.__str__(self))


class ISS(Imposto):
    def calcula(self, orcamento):

        return orcamento.value * .06 + self.calculo_do_outro_imposto(orcamento)

    def __str__(self):
        return 'ISS' + str(Imposto.__str__(self))


class ICPP(Template_de_imposto_condicional):
    def must_use_tax_maximum(self, orcamento):
        return orcamento.value > 500

    def tax_maximum(self, orcamento):
        return orcamento.value * 0.07

    def tax_minimum(self, orcamento):
        return orcamento.value * 0.05

    def __str__(self):
        return 'ICPP' + str(Imposto.__str__(self))


class IKCV(Template_de_imposto_condicional):
    def must_use_tax_maximum(self, orcamento):
        return orcamento.value > 500 and (
            self.__has_item_greater_than_100_reais(orcamento))

    def tax_maximum(self, orcamento):
        return orcamento.value * 0.1

    def tax_minimum(self, orcamento):
        return orcamento.value * 0.06

    def __has_item_greater_than_100_reais(self, orcamento):
        for item in orcamento.get_itens():
            if item.value > 100:
                return True
            else:
                return False

    def __str__(self):
        return 'IKCV' + str(Imposto.__str__(self))
