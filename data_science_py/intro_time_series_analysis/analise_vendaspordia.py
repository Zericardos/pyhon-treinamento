#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 08:32:25 2021

@author: ricardo
"""


import pandas as pd
from plot_timeseries import MultiplePlots as mp, PlotDf


vendas_por_dia = pd.read_csv('data/vendas_por_dia.csv')
vendas_por_dia.dia = pd.to_datetime(vendas_por_dia.dia)
print('Campos da tabela Chocolura: ', vendas_por_dia.keys())
print ('Quantidade de dados nulos: ', vendas_por_dia.isna().sum().sum())

vendas_por_dia['aumento'] = vendas_por_dia['vendas'].diff()
vendas_por_dia['aceleracao'] = vendas_por_dia['aumento'].diff()

# campos do DataFrame
ys = ['vendas', 'aumento', 'aceleracao']
ylabels = ['Vendas (R$)', 'Aumento', 'Aceleração']
xlabel = 'Tempo (dias)'

data_plots = mp.lines(
    x='dia',
    ys=ys,
    dataframe=vendas_por_dia,
    title="Análise de Vendas de Outubro e Novembro - Chocolura",
    xlabel=xlabel,
    ylabels=ylabels,
    figure_number=0
)

# vamos analisar a sazonalidade, mas primeiro vamos redefinir os dias para os
# dias da semana


vendas_por_dia['dias_da_semana'] = vendas_por_dia['dia'].dt.day_name()
# vamos traduzir esses campos
print(vendas_por_dia['dias_da_semana'].unique())
# criar o dicionário para traduzir
traducao_dias = {
    'Monday': 'segunda',
    'Tuesday': 'terca',
    'Wednesday': 'quarta',
    'Thursday': 'quinta',
    'Friday': 'sexta',
    'Saturday': 'sabado',
    'Sunday': 'domingo'
    }
# realizar a traducao
vendas_por_dia['dias_da_semana'] = vendas_por_dia['dias_da_semana'].map(
    traducao_dias
    )

# agrupar os dias para avaliarmos as medias

vendas_agrupadas = vendas_por_dia.groupby(
    ['dias_da_semana']
    )[ys]
print(vendas_agrupadas.mean().round(2))

data_plots = mp.lines(
    x='dias_da_semana',
    ys=ys,
    dataframe=vendas_por_dia,
    title="Análise de Vendas de Outubro e Novembro - Chocolura",
    xlabel='Dias da Semana',
    ylabels=ylabels,
    figure_number=1
)

# então fazemos uma correlação
vendas_diarias_plots = PlotDf(vendas_por_dia)
vendas_diarias_plots.correlation(
    'vendas',
    'Correlação das Vendas Diárias',
    figure_number=2
    )
vendas_diarias_plots.correlation(
    'aumento',
    'Correlação do Aumento das Vendas Diárias',
    figure_number=3
    )
vendas_diarias_plots.correlation(
    'aceleracao',
    'Correlação da Aceleração das Vendas Diárias',
    figure_number=4
    )
"""Os três últimos gráficos mostram que há forte correlação entre as vendas
diárias, o seu aumento e a aceleração, algo bem esperado já que um é baseado
no outro. O gráfico dos dias mostra que há uma queda significativa nas vendas no começo da semana, voltando aumentar logo em seguida"""
