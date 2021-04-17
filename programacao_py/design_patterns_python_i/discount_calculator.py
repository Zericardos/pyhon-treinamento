#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 07:32:10 2021

@author: ricardo
"""


class DiscountCalculator:
    def calcs(budget):
        """ É feita uma cadeia de descontos em que um desconto chama o próximo
        e assim por diante até o fim da cadeia, em que não há desconto. Assim
        são feitos descontos sucessivos.
        Esse Design Patterns chama-se Chain of Responsability"""
        discount = Discount5MoreItens(
            Discount500MoreReais(NoDiscount)
        ).calcs(budget)
        return discount


# tester
if __name__ == '__main__':

    from budget import Budget
    from budget import Item
    from discount import Discount5MoreItens
    from discount import Discount500MoreReais
    from discount import NoDiscount
    # Init the class
    budget = Budget()
    budget.add_item(Item('item - 1', 50))
    budget.add_item(Item('item - 2', 450))
    budget.add_item(Item('item - 3', 60))
    print(budget.value)
    calculated_discount = DiscountCalculator.calcs(budget)
    print(calculated_discount)
