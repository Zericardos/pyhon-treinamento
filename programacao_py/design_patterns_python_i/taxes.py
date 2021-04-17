#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 05:24:49 2021

@author: ricardo
"""


from abc import ABCMeta, abstractmethod


class ICMS(object):
    def calculates_tax(self, budget):

        return budget.value * .1

    def __str__(self):
        return 'ICMS'

class ISS(object):
    def calculates_tax(self, budget):

        return budget.value * .06

    def __str__(self):
        return 'ISS'


class Template_de_imposto_condicional(object):
    __metaclass__ = ABCMeta
    # categoriza uma meta classe. Ela será herdada por suas classes filhas
    def calculates_tax(self, budget):
        if self.must_use_tax_maximum(budget):
            return self.tax_maximum(budget)
        else:
            return self.tax_minimum(budget)

    @abstractmethod
    def must_use_tax_maximum(self, budget):
        pass

    @abstractmethod
    def tax_maximum(self, budget):
        pass

    @abstractmethod
    def tax_minimum(self, budget):
        pass


class ICPP(Template_de_imposto_condicional):
    def must_use_tax_maximum(self, budget):
        return budget.value > 500


    def tax_maximum(self, budget):
        return budget.value * 0.07


    def tax_minimum(self, budget):
        return budget.value * 0.05


    def __str__(self):
        return 'ICPP'


class IKCV(Template_de_imposto_condicional):
    def must_use_tax_maximum(self, budget):
        return budget.value > 500 and (
            self.__has_item_greater_than_100_reais(budget))

    def tax_maximum(self, budget):
        return budget.value * 0.1

    def tax_minimum(self, budget):
        return budget.value * 0.06

    def __has_item_greater_than_100_reais(self, budget):
        for item in budget.get_itens():
            if item.value > 100:
                return True
            else:
                return False


    def __str__(self):
        return 'IKCV'