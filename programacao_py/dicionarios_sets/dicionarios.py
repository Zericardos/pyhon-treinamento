#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict, Counter

usuarios = {
    "Amanda": 2,
    "Beatriz": 34,
    "Jose": 25,
    "Jauica": 84
}
# podemos criar dicionário dessa maneira
usuarios_2 = dict(Amanda = 2, Beatriz = 34, Jose = 25, Jauica = 84)

print(usuarios, usuarios_2, sep="\n")

# Entretanto, a primeira forma é mais comum. Dicionários são objetos mutáveis
# Verificação de elementos, fazemos isso nas chaves
print("Beatriz" in usuarios)

# Removemos elementos apontando a sua chave
del usuarios["Amanda"]
print(usuarios)

# Podemos tentar pegar um valor atribuindo uma chave, no caso dessa chave
# ausente, retornamos uma variável de interesse
print(usuarios.get("Amanda", "Não tem a chave 'Amanda'"))
print(usuarios_2.get("Amanda", "Não tem a chave 'Amanda'"))

# acesso as chaves é o modo natural, vide "Beatriz" in usuarios
# mas podemos acessá-las explicitamente com atributo keys
print(usuarios.keys())
# Do mesmo modo, podemos acessar os valores
print(usuarios.values())
# E também uma dupla de cada -> Chave: Valor
print(usuarios.items())

"""Perceba que essas técnicas retornam listas, logo, podemos usar todos os
recursos de lista com essa combinação também. Podemos usar list comprehesion"""
print(["Usuário {}".format(usuario) for usuario in usuarios_2.keys()])

# Podemos usar como um contador de palavras num texto
texto = "Aqui vai um texto que vamos usar várias palavras que podem se " \
        "repetir, entretanto, talvez algumas se repitam mais do que outras," \
        "mas se repetem, repetir repetirão. Podem repetir várias vezes ou " \
        "mesmo nenhuma vez, vamos então contar quantas elas se repetem" \
        "muitas? Poucas? Primeiro vamos tomá-las como todas sendo minúsculas" \
        "para deixar o texto padrão"
texto_padrao = texto.lower()
print(texto_padrao.split())

contagem_palavras = {}
for palavra in texto_padrao.split():
    ate_agora = contagem_palavras.get(palavra, 0)
    ate_agora += 1
    contagem_palavras[palavra] = ate_agora
print(contagem_palavras)

"""Já que primeiramente contagem_palavras não contém valor algum para nenhuma
chave, podemos atribuir valor zero e ir somando. Perceba que podemos reduzir o
código em duas linhas"""
contagem_palavras_2 = {}
for palavra in texto_padrao.split():
    contagem_palavras_2[palavra] = contagem_palavras_2.get(palavra, 0)
    contagem_palavras_2[palavra] += 1
print(contagem_palavras_2)

"""Um outro fato é que deve ser muito comum atribuir um valor padrão para
dicionários. Tão padrão que alguém implementou isso no Python. Fizeram isso
no módulo embutido defaultdict de collections. Ele pega uma factory de valores
padrão, na falta de um valor, ele usa essa factory. Usaremos a factory int
int é também uma função e se não tomar argumento algum, devolve 0, int()=0"""
contagem_palavras_3 = defaultdict(int)
for palavra in texto_padrao.split():
    contagem_palavras_3[palavra] += 1
print(contagem_palavras_3)

"""Por fim, na mesma abordagem, temos a classe embutida, de collections também,
Counter, que retorna um contador de um iterável, justamente o que estamos
fazendo, pois str.split retorna uma lista de strings, logo um iterável"""
print(Counter(texto_padrao.split()))