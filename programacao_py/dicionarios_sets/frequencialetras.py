#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import Counter

"""Vamos usar os textos do módulo dicionario.py e sets.py"""

texto1 = """
Perceba que essas técnicas retornam listas, logo, podemos usar todos os
recursos de lista com essa combinação também. Podemos usar list comprehesion.
Já que primeiramente contagem_palavras não contém valor algum para nenhuma
chave, podemos atribuir valor zero e ir somando. Perceba que podemos reduzir o
código em duas linhas.
Um outro fato é que deve ser muito comum atribuir um valor padrão para
dicionários. Tão padrão que alguém implementou isso no Python. Fizeram isso
no módulo embutido defaultdict de collections. Ele pega uma factory de valores
padrão, na falta de um valor, ele usa essa factory. Usaremos a factory int
int é também uma função e se não tomar argumento algum, devolve 0, int()=0.
Por fim, na mesma abordagem, temos a classe embutida, de collections também,
Counter, que retorna um contador de um iterável, justamente o que estamos
fazendo, pois str.split retorna uma lista de strings, logo um iterável
"""
texto1 = texto1.lower()  # Para termos uma abordagem estatística

texto2 = """
Queremos enviar um e-mail para os usuários que fizeram este curso, então
criaremos uma lista com ambos os usuários.
Entretanto, percebemos que em ambas as listas, há usuários comuns entre
si. Isso gera um problema no disparo de e-mail. O Python oferece um módulo
que pega somente elementos únicos de objetos iteráveis, o set.

set não possui indexador, então não podemos acessar os elementos por 
set(iterável)[índice].
Agora supomos que queiramos enviar e-mails somente para usuários que
estudaram Data Science, mas não Machine Learning. Novamente, podemos usar
outra operação com conjuntos -
Um conjunto é um objeto mutável. Podemos adicionar elementos ao objeto
set por meio do método add(elemento)
"No caso de um texto, se quisermos pegar todas as palavras, sem" \
        "repetição, podemos primeiro separar as palavras com o método split" \
        "do objeto string. Depois usamos o set neste resultado"
"""
texto2 = texto2.lower()
for caractere, frequencia in Counter(texto1).most_common(10):
    frequencia_porcentagem = frequencia / sum(Counter(texto1).values())
    print(f"Caractere {caractere} ==> {frequencia_porcentagem:.2f}")

# logo podemos criar uma função

def conta_os_dez_primeiras_letras_mais_frequentes(texto):
    for caractere, frequencia in Counter(texto).most_common(10):
        frequencia_porcentagem = frequencia / sum(Counter(texto).values())
        print(f"Caractere {caractere} ==> {frequencia_porcentagem*100:.2f}%")

conta_os_dez_primeiras_letras_mais_frequentes(texto2)