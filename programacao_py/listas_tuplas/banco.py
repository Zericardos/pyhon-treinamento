#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 20:03:27 2021

@author: ricardo
"""


class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outra_conta):
        if type(outra_conta) != ContaSalario:
            return False

        return self._codigo == outra_conta.codigo and self._saldo ==\
            outra_conta.saldo
