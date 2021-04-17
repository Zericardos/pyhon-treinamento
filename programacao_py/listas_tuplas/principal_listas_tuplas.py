#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 17:48:06 2021

@author: ricardo
"""


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
