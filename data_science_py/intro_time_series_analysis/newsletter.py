#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 21:55:31 2021

@author: ricardo
"""


from plot_timeseries import MultiplePlots as mp
import pandas as pd
# Alucar - Analisando assinantes da newsletter
assinantes = pd.read_csv('data/newsletter_alucar.csv')
# Investigar um pouco
assinantes.head()
assinantes.dtypes
assinantes.shape
assinantes.isna().sum()
assinantes.isna().sum().sum()
# Mudar o tipo do mes, de object para datetime
assinantes.mes = pd.to_datetime(assinantes.mes)
# implementar a "derivada discreta" para inferir aumento/decréscimo
assinantes['aumento'] = assinantes['assinantes'].diff()
assinantes['aceleracao'] = assinantes['aumento'].diff()
# vamos plotar usando a classe que criamos quando trabalhamos com Alucar
mp.lines(
    x=assinantes.mes,
    ys=['assinantes', 'aumento', 'aceleracao'],
    dataframe=assinantes,
    title='Análise do número de assinantes',
    xlabel='Tempo (meses)',
    ylabels=[
        'Número de assinantes',
        'Aumento',
        'Aceleração'
    ],
    figure_number=0
)
# Pode-se fazer inferência de pico de crescimento, aceleração e afins
# não há sazonalidade
