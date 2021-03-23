#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 05:24:49 2021

@author: ricardo
"""


class ICMS(object):
    def calculates_tax(budget):

        return budget.value * .1


class ISS(object):
    def calculates_tax(budget):

        return budget.value * .06
