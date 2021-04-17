#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 05:24:49 2021

@author: ricardo
"""


class TaxCalculator(object):
    def performs_calculation(self, budget, tax):

        calculated_tax = tax.calculates_tax(budget)

        print(f"Cálculo do imposto {tax.__str__()}: " + str(calculated_tax))

# to test module only with it is called but not when it is imported


if __name__ == '__main__':

    from budget import Budget
    from budget import Item
    from taxes import ICMS
    from taxes import ISS
    from taxes import ICPP
    from taxes import IKCV

    # Init the class
    orcamento = Budget()
    orcamento.add_item(Item('item - 1', 50))
    orcamento.add_item(Item('item - 2', 450))
    orcamento.add_item(Item('item - 3', 60))
    print(orcamento.value)

    tax_calculator = TaxCalculator()
    tax_calculator.performs_calculation(orcamento, ICMS())
    tax_calculator.performs_calculation(orcamento, ISS())
    tax_calculator.performs_calculation(orcamento, ICPP())
    tax_calculator.performs_calculation(orcamento, IKCV())
