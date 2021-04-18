#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 17:48:06 2021

@author: ricardo
"""


from operator import attrgetter
from banco import ContaSalario as cs
idades = (13, 28, 64, 52, 34, 42)
print(range(len(idades)))  # lazy class, só abre se for pedido
print(list(range(len(idades))))  # a classe lista desempacota tudo, o mesmo
# acontece com enumerate
print(list(enumerate(idades)))
""" No caso dessas classes lazy, quando usar um iterador como o for, ele
só vai desempacotar um elemento do looping por vez. Logo, um objeto do tipo
lazy entrega para nós a medida que é pedido, na medida do possível.
No caso de poucos elementos, isso pode ser vantajoso. Se for muitos,
talvez seja melhor trabalhar com objetos"""
grupo_estudantes = [
    ('José', 1.77, 31),
    ('Keith', 1.67, 31),
    ('Gui', 1.65, 28)
]

# para unpacking de objetos
for nome, altura, idade in grupo_estudantes:
    print(nome)

# podemos omitir os objetos que não queremos usar
for nome, _, _ in grupo_estudantes:
    print(nome)
"""Geralmente é útil deixar as variáveis explícitas, mesmo que não sejam
usadas porque depois de muito tempo vamos saber do que se trata além de
outro desenvolvedor identificar imediatamente o que significa"""

# ordenar as idades
print(sorted(idades))  # já retorna uma lista

# ordem inversa
print(sorted(idades, reverse=True))

# pegar os elementos em ordem reversa ao original
print(list(reversed(idades)))  # reversed retorna um iterador, precisamos
# desempacotá-lo usando a função list

# objeto list tem método sort e tem a opção reverse.
lista_idades = list(idades)
lista_idades.sort()
lista_idades.sort(reverse=True)


conta_jose = cs(18)
conta_jose.deposita(450)

conta_keith = cs(5)
conta_keith.deposita(650)

conta_gui = cs(12)
conta_gui.deposita(700)

contas = [conta_jose, conta_keith, conta_gui]
"""Para objetos, precisamos deixar bem claro para o Python o que ele quer
comparar. Se formos deixar essas contas em ordem, podemos usar a classe
sorted, mas devemos especificar o que vamos comparar no objeto ContaSalario
como fizemos com o método mágico __eq__.
Vamos usar o atributo key da classe sorted. Podemos usá-las de diferentes
maneiras. Uma delas é usar um método ou função que tomará o seu argumento
o objeto de comparação
"""


def extrai_conta(conta):
    return conta._saldo


for conta in sorted(contas, key=extrai_conta):
    print(conta)

"""Esse procedimento funciona, mas não é uma boa prática extrairmos um
atributo privado. Se ele é privado, queremos que ele não seja exposto.
Podemos também usar o método attrgetter da classe operator"""

for conta in sorted(contas, key=attrgetter('_saldo')):
    print(conta)


"""
Apesar de funcionar como o primeiro, ainda estamos usando um atributo
privado, algo que o criador não gostaria, pois há uma razão para estar
oculto. Não mexendo nesses atributos fora da classe, não estaremos
quebrando o encapsulamento.
Se usarmos a classe sorted diretamente em contas sem mais nada,
verificaremos que o operador < precisa ser definido. Novamente, o Python
precisa saber o que vai comparar. O código, o saldo? etc
Neste caso, devemos definir o operador < entre os objetos ContaSalario.
Queremos ordenar pelo saldo.
Redefinimos o método mágico __lt__ de lesser than"""

for conta in sorted(contas):
    print(conta)  # funciona também com conta_jose < conta_keith

"""Porém, se adotarmos duas contas com saldos iguais, como proceder?
Devemos atribuir uma segunda preferência. Podemos fazer tanto isso pelo
método attrgetter('_saldo', '_codigo') quanto modificar o método mágico
__lt__ e atribuir uma condição no caso de igualdade.
Vamos testar"""

conta_jose = cs(18)
conta_jose.deposita(800)

conta_keith = cs(5)
conta_keith.deposita(800)

conta_gui = cs(12)
conta_gui.deposita(700)

contas = [conta_jose, conta_keith, conta_gui]
# acessando novamente atributos privados fora da classe. Não é uma boa
# prática
for conta in sorted(
        contas, key=attrgetter('_saldo', '_codigo')
):  # atribuiu uma ordem de classificação no caso de igualdade
    print(conta)

# com o método mágico alterado com condição de igualdade
for conta in sorted(contas):
    print(conta)  # funciona também com conta_jose < conta_keith

"""Conseguimos também criar o operador de comparação == e < e por tabela o
> (que é oposto de <). Entretanto, o operador <= não é definido
automaticamente. Para isso devemos criar ele em particular ou usar
a ferramenta total_ordering e usar o decorador em cima da classe que
atribuímos os métodos mágicos __eq__ e __lt__ {ou __gt__}"""

conta_jose < conta_gui
conta_jose < conta_keith
conta_jose == conta_jose
conta_jose <= conta_jose
conta_jose <= conta_keith
