#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:29:52 2021

@author: ricardo
"""


import pandas as pd
from plot_timeseries import PlotDf, MultiplePlots as mp

cafelura = pd.read_csv('data/cafelura.csv')
print('cafelura DataFrame', cafelura.head())
print(cafelura.dtypes)
cafelura.mes = pd.to_datetime(cafelura.mes)
print(cafelura.dtypes)
print(
    'Campos da tabela Chocolura: ',
    [i for i in cafelura.keys()])
print('Quantidade de dados nulos: ', cafelura.isna().sum().sum())

# plotar o gráfico par avaliar sua distribuição
data_plot = PlotDf(cafelura)
data_plot.line(
    'mes',
    'vendas',
    'Análise de distribuição das vendas da Chocolura de 2017 e 2018',
    'Tempo (meses)',
    'Vendas (R$)',
)
# o gráfico apresenta uma tendência de aumento, mas há algumas quedas
# no crescimento, podemos avaliar melhor se o normalizarmos.
# vamos fazer isso pelo número de finais de semana (fds)
quantidade_de_dias_de_fds = pd.read_csv('data/dias_final_de_semana.csv')
# normalizaãço
cafelura['vendas_normalizadas'] = (
    cafelura['vendas'] / quantidade_de_dias_de_fds['quantidade_de_dias'].values
)
# vamos plotar numa só figuráa o gráfico normal e normalizado

mp.lines(
    x='mes',
    ys=['vendas', 'vendas_normalizadas'],
    dataframe=cafelura,
    title="Vendas Cafelura 2017 e 2018",
    xlabel='Tempo (meses)',
    ylabels=['Vendas (R$)', 'Vendas (R$)'],
    figure_number=1)
# percebemos há um aumento contínuo nas vendas de 2017 a 2018

# vamos comparar os resultados estatísticos usando outros métodos
