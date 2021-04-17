#
# Exemplo de como criar classes
#
class minhaClasse():
    """Put inherited melhods, from another class, between brackets
    The constructor, for pathern, in the beggining of the class is
    __init__(self). This indicates that all methods in my class will
    receive the object self, but the python will pass along every 
    object being instatiaded"""

    def __init__(self):
        self.meuAtributo = "Passou pelo construtor!"

    def meuMetodo(self):
        print("Passou pelo meuMetodo")
    
    def meuMetodo2(self, valor):
        """
        The methods can receive other parameters as valor

        Parameters
        ----------
        valor : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.outroAtributo = valor
        print(self.outroAtributo)

        