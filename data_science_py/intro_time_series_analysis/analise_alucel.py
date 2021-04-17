#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 18:20:27 2021

@author: ricardo
"""


from plot_timeseries import PlotDf
import pandas as pd
from plot_timeseries import MultiplePlots as mp

alucel = pd.read_csv('data/alucel.csv')
alucel.dia = pd.to_datetime(alucel.dia)
print('Campos da tabela alucel: ', alucel.keys())
print('Quantidade de dados nulos: ', alucel.isna().sum().sum())

alucel['aumento'] = alucel['vendas'].diff()
alucel['aceleracao'] = alucel['aumento'].diff()

# campos do DataFrame
ys = ['vendas', 'aumento', 'aceleracao']
ylabels = ['Vendas (R$)', 'Aumento', 'Aceleração']
xlabel = 'Tempo (dias)'

data_plots = mp.lines(
    x='dia',
    ys=ys,
    dataframe=alucel,
    title="Análise de Vendas da Alucel de Outubro e Novembro de 2018",
    xlabel='Tempo (dias)',
    ylabels=ylabels,
    figure_number=0
)
"""Percebemos que há muito ruído, o que dificulta encontrar alguma
eventual sazonaliade, vamos aplicar a técnica 'Média Móvel' para tratar
desse caso. Usamos a média de 7 dias com a função rolling(7).mean"""
alucel['media_movel'] = alucel['vendas'].rolling(7).mean()
# vamos plotar para avaliar essa técnica

data_plot = PlotDf(alucel)
data_plot.line(
    x_tag='dia',
    y_tag='media_movel',
    title="Análise de vendas com média móvel de 7 dias",
    xlabel='Tempo (dias)',
    ylabel="Média Móvel",
    figure_number=1
)
# fazendo agora uma média móvel de 21 dias para compararmos
alucel['media_movel21'] = alucel['vendas'].rolling(21).mean()
ymovels = ['vendas', 'media_movel', 'media_movel21']
ylabels = [
    'Vendas (R$)',
    'Média Móvel 7 dias',
    'Média Móvel 21 dias'
]

data_plots = mp.lines(
    x='dia',
    ys=ymovels,
    dataframe=alucel,
    title="Comparando as Vendas com Médias Móveis da Alucel",
    xlabel='Tempo (dias)',
    ylabels=ylabels,
    figure_number=2
)
# Percebemos que quanto maior o período de dias da média móvel, a curva
# se normaliza, mas perdemos informações. Isso deve ser usado com cuidado
# e o número de dias varia de caso para caso
