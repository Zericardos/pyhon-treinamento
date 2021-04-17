#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 08:37:47 2021

@author: ricardo
"""

# We have a cumulative discount


class Discount5MoreItens:
    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def calcs(self, budget):

        if budget.total_itens > 5:
            return budget.value * 0.1
        else:
            return self.__next_discount.calcs(budget)


class Discount500MoreReais:
    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def calcs(self, budget):
        if budget.value > 500:
            return budget.value * 0.07
        else:
            return self.__next_discount.calcs(budget)


class NoDiscount:
    def calcs(self, budget):
        return 0
