#!/usr/bin/env python3
# -*- coding: utf-8 -*-


usuarios_data_science = [15, 23, 43, 56]  # códigos dos usuarios
usuarios_machine_learning = [13, 23, 42, 56]

"""Queremos enviar um e-mail para os usuários que fizeram este curso, então
criaremos uma lista com ambos os usuários"""

assistiram = usuarios_data_science.copy()  # faz uma cópia rasa
# cópia rasa não cria um novo objeto, mas utiliza a mesma referência
assistiram.extend(usuarios_machine_learning)
print(assistiram)

"""Entretanto, percebemos que em ambas as listas, há usuários comuns entre
si. Isso gera um problema no disparo de e-mail. O Python oferece um módulo
que pega somente elementos únicos de objetos iteráveis, o set.

set não possui indexador, então não podemos acessar os elementos por 
set(iterável)[índice]"""

assistiram = set(assistiram)  # transforma em set, pega somente os únicos obj
# podemos fazer a união de conjuntos com o unificador pipe |
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 42, 56}
assistiram_set =  usuarios_data_science | usuarios_machine_learning
print("Data Science", usuarios_data_science)
print("Machine Learning", usuarios_machine_learning)
print("Assistiram um ou outro", assistiram, assistiram_set, sep='\n')

""" Para pegar elemntos em comum a dois sets usamos o operador &"""
assistiram_ambos =  usuarios_data_science & usuarios_machine_learning
print("Assistiram ambos", assistiram_ambos)
"""Agora supomos que queiramos enviar e-mails somente para usuários que
estudaram Data Science, mas não Machine Learning. Novamente, podemos usar
outra operação com conjuntos -"""
somente_data_science = usuarios_data_science - usuarios_machine_learning
print("Somente Data Science", somente_data_science)

# Ou exclusivo ^
somente_um_ou_outro = usuarios_data_science ^ usuarios_machine_learning
print("Somente um ou outro", somente_um_ou_outro)

"""Um conjunto é um objeto mutável. Podemos adicionar elementos ao objeto
set por meio do método add(elemento)"""
print("Data Science", usuarios_data_science)
usuarios_data_science.add(173)
print("Data Science adicionado usuário 173", usuarios_data_science)
# Se quisermos compor um conjunto imutável, usamos frozenset em vez de set
print("Conjunto imutável", frozenset({3,1,33,11}))
texto = "No caso de um texto, se quisermos pegar todas as palavras, sem" \
        "repetição, podemos primeiro separar as palavras com o método split" \
        "do objeto string. Depois usamos o set neste resultado"
print(texto)
print("Palavras únicas do texto", set(texto.split()))