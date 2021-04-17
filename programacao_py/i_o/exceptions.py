#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 18:00:12 2021

@author: ricardo
"""

try:
    arquivo_contatos = open(
        'nao_existe.csv',
        encoding='latin_1',
        mode='w+'
    )
except FileNotFoundError:
    print()
    print("Arquivo não encontrado")
    print()
except NameError:
    print("Arquivo ainda não definido")
# if any exception with open ocurrs, Python will exit try command and
# execute finally
finally:
    arquivo_contatos.close()

arquivo = open(
    'dados/contatos-escrita.csv',
    encoding='latin_1',
    mode='a+'
)

print(type(arquivo.buffer))

texto_em_bytes = bytes('Esse é um texto em bytes', 'latin_1')
# b'Esse é um texto em bytes', 'latin_1' # won't work because é isn't in ASCII
# representation, so we must use built in class bytes()

print(texto_em_bytes)
print(type(texto_em_bytes))

contato = bytes('15,Verônica,veronica@veronica.com.br\n', 'latin_1')
arquivo.buffer.write(contato)

arquivo.close()
