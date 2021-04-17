#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:08:13 2021

@author: ricardo
"""


from abc import ABC, abstractmethod
from contato import Contato
import csv, json, pickle


class ContatoDao(ABC):

    @abstractmethod
    def buscar_todos(self, caminho):
        pass

    @abstractmethod
    def salvar(self, contatos, caminho):
        pass
    
    
class ContatoDaoJSON(ContatoDao):

    @abstractmethod
    def buscar_todos(self, caminho):
        contatos = []
        with open(caminho, mode='r') as arquivo:
            contatos_json = json.load(arquivo)
            for contato in contatos_json:
                        c = Contato(**contato)
                        contatos.append(c)

        return contatos   

    @abstractmethod
    def salvar(self, contatos, caminho):
        with open(caminho, mode='w') as arquivo:
            json.dump(
                contatos, arquivo, default=lambda objeto: objeto.__dict__
                )

class ContatoDaoCSV(ContatoDao):

    @abstractmethod
    def buscar_todos(
            self, caminho, encoding='latin_1'
            ):
        contatos = []
        
        with open(caminho, mode='r') as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                id, nome, email = linha
                contato = Contato(id, nome, email)
                contatos.append(contato)

        return contatos   

    @abstractmethod
    def salvar(self, contatos, caminho):
        with open(caminho, mode='w') as arquivo:
            arquivo_writer = csv.writer(
                arquivo, delimiter=',',
                quotechar='')
            for linha in arquivo_writer:
                id, nome, email = linha
                contato = Contato(id, nome, email)
                arquivo_writer.writerow(contato)
                
                
class ContatoDaoPickle(ContatoDao):

    @abstractmethod
    def buscar_todos(
            self, caminho
            ):
        with open(caminho, mode='rb') as arquivo:
            contatos = pickle.load(arquivo)
        
        return contatos

    @abstractmethod
    def salvar(self, contatos, caminho):
        with open(caminho, mode='wb') as arquivo:
            pickle.dump(contatos, arquivo)