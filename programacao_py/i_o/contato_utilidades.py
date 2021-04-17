#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 23:52:44 2021

Este código é responsável por realizar a leitura arquivos e a escrita deles
já convertidos.
@author: ricardo
"""


import csv
import pickle
import json
from contato import Contato


def csv_para_contatos(caminho, encoding='latin_1'):
    contatos = []

    with open(caminho, encoding=encoding) as arquivo:
        # O módulo csv entende a separação de cada linha e separador por
        # vírgula
        leitor = csv.reader(arquivo)
        # cada linha na iteração é uma lista em que cada elemento da lista é
        # um atributo do documento csv
        for linha in leitor:
            # id = linha[0]
            # nome = linha[1]
            # email = linha[2]
            # podemos usar o desempacotamento, um código mais enxuto
            # como a linha só tem três atributos, podemos desempacotá-lo
            # com três variáveis, que é equivalente ao código comentado
            id, nome, email = linha
            contato = Contato(id, nome, email)
            contatos.append(contato)

    return contatos


def contatos_para_pickle(contatos, caminho):
    # primeiro abrir o arquivo no modo escrita e binário, pois o módulo pickle
    # só salva neste formato
    with open(caminho, mode='wb') as arquivo:
        pickle.dump(contatos, arquivo)
        
        
def pickle_para_contatos(caminho):
    # vai fazer a operação inversa, note que o modo de abertura deve ser
    # também em modo binário: bytes
    with open(caminho, mode='rb') as arquivo:
        contatos = pickle.load(arquivo)
        
    return contatos


def contatos_para_json(contatos, caminho):
    with open(caminho, mode='w') as arquivo:
        # O python não sabe como exportar o arquivo contato pelo método dump
        # temos que especificar uma forma de fazer isso. Especificamos pela
        # função criada no argumento default. Então, default recebe um objeto
        # callable e receberá o primeiro argumento de dump
        json.dump(contatos, arquivo, default=_contato_para_json)
        # o sinal _ na frent da função indica aos programadores que ela deve
        # ser de uso interno, i.e, somente usada dentro deste módulo
        # entretanto, poderíamos usar uma função anônima lambda, ficaria assim
        # json.dump(contatos, arquivo, default=lambda contato: 
        # contato.__dict__)
def _contato_para_json(contatos):
    return contatos.__dict__
# o dunder method __dict__ pega todos os atributos e seus valores do objeto
# aplicado e retorna um dicionário com chaves e valores respectivamente. Isso
# implica que cada item da lista será um dicionário com esses atributos


def json_para_contatos(caminho):
    contatos = []
    # salvamos os contatos em formato de lista, então vamos continuar fazendo
    # dessa maneira
    # com vamos apenas ler, usamos o modo padrão da classe open
    with open(caminho) as arquivo:
        # carregamento de arquivo
        contatos_json = json.load(arquivo)
        # criamos um looping para cada contato, pois os contatos estão salvos em
        # uma lista de dicionários, então vamos desempácotá-los
        print(contatos_json)
        for contato in contatos_json:
            # c = Contato(
            #     contato['id'],
            #     contato['nome'],
            #     contato['email']
            #     )
            # note que nossa classe Contato tems os nomes dos atributos
            # coincidentes com os nomes das chaves do dicionário contato
            # assim, podemos usar o desempacotamento ** da forma
            c = Contato(**contato)
            contatos.append(c)
    
    return contatos
# todas essas funções poderiam ser agrupadas como métodos e elas tem em comum
# a finalidade de ler e salvar os arquivos em diferentes formatos, logo, é
# interessante agrupá-las em classes