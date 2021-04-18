#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 20:03:27 2021

@author: ricardo
"""

from functools import total_ordering


@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outra_conta):
        if type(outra_conta) != ContaSalario:
            return False

        return self._codigo == outra_conta._codigo and self._saldo ==\
            outra_conta._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __lt__(self, outra_conta):  # Quando comparamos com sorted e afins

        if self._saldo != outra_conta._saldo:  # O que queremos comparar
            return self._saldo < outra_conta._saldo
        else:
            return self._codigo < outra_conta._codigo

    def __str__(self):
        return f"[>>Codigo {self._codigo}, Saldo {self._saldo}<<]"
