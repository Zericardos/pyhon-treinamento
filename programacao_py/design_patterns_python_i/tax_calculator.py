class TaxCalculator(object):
    def performs_calculation(self, budget, tax):

        calculated_tax = tax.calculates_tax(budget)

        print(calculated_tax)

# to test module only with it is called but not when it is imported


if __name__ == '__main__':

    from budget import Budget
    from taxes import ICMS
    from taxes import ISS

    orcamento = Budget(500)
    print(orcamento.value)

    tax_calculator = TaxCalculator()
    tax_calculator.performs_calculation(orcamento, ICMS)
    tax_calculator.performs_calculation(orcamento, ISS)
