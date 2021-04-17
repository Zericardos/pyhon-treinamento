#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 23:50:17 2021

Queremos pegar nossa lista de contatos csv e exportá-la para um arquivo
python par que possa ser serializada e transferida para outros meios.
Não é uma boa prática de programação estabelecer todas as funções num mesmo
arquivo, então vamos separar cada pedaço do código para cada sua finalidade
para que qualquer alteração seja feita unicamente em cada código

@author: ricardo
"""


import contato_utilidades

try:
    contatos = contato_utilidades.csv_para_contatos(
        caminho='dados/contatos.csv',
    )
    contatos = contato_utilidades.pickle_para_contatos(
        caminho='dados/contatos.p'
        )
    contatos = contato_utilidades.json_para_contatos(
        caminho='dados/contatos.json'
        )
    contato_utilidades.contatos_para_pickle(
        contatos,
        caminho='dados/contatos.p',
    )
    # o formato pickle geralmente tem extensões .p ou .pickle
    contato_utilidades.contatos_para_json(
        contatos,
        caminho='dados/contatos.json',
    )
    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')
except FileNotFoundError:
    print("Arquivo não encontrado")
except NameError:
    print("Arquivo ainda não definido")
