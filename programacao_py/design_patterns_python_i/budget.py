#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 05:24:49 2021

@author: ricardo
"""


class Budget(object):
    def __init__(self):
        """
        Inits Budget

        Returns
        -------
        None.

        """
        self.__itens = []

    # a budget can't variable, must be have a fixed value, so we use property decorator
    @property
    def value(self):
        total = 0.0
        for item in self.__itens:
            total += item.value

        return total

    def get_itens(self):

        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def add_item(self, item):
        self.__itens.append(item)


class Item(object):
    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    @property
    def value(self):
        return self.__value

    @property
    def name(self):
        return self.__name
