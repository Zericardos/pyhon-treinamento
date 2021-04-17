#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 17:34:39 2021

@author: ricardo
"""


import pandas as pd
from plot_timeseries import PlotDf
from plot_timeseries import MultiplePlots as mp

time_sales_df = pd.read_csv('data/alucar.csv')

# Verify null values
time_sales_df.isna().sum()
print('Quantidade de dados nulos', time_sales_df.isna().sum().sum())

# verify data type
print('Tipo de dados', time_sales_df.dtypes)

# Is important to transform object (mes) to datetime type
time_sales_df.mes = pd.to_datetime(time_sales_df.mes)
# increased sales
time_sales_df['aumento'] = time_sales_df['vendas'].diff()
# acceleration of sales
time_sales_df['aceleracao'] = time_sales_df['aumento'].diff()

data_plot = PlotDf(
    time_sales_df
)

data_plot.line('mes',
               'vendas',
               'Vendas Alucar de 2017 e 2018',
               'Tempo (meses)',
               'Vendas (R$)',
               0
               )

data_plot.line(
    x_tag='mes',
    y_tag='aumento',
    title='Aumento das Vendas Alucar de 2017 e 2018',
    xlabel='Tempo (meses)',
    ylabel='Aumento',
    figure_number=1
)

data_plot.line(
    'mes',
    'aceleracao',
    'Aceleração das Vendas Alucar de 2017 e 2018',
    'Tempo (meses)',
    'Aceleração',
    2
)

# To compare them in one figure
ys = ['vendas', 'aumento', 'aceleracao']
ylabels = ['Vendas (R$)', 'Aumento', 'Aceleração']
xlabel = 'Tempo (meses)'

data_plots = mp.lines(
    x='mes',
    ys=ys,
    dataframe=time_sales_df,
    title="Análise de Vendas da Alucar de 2017 e 2018",
    xlabel='Tempo (meses)',
    ylabels=ylabels,
    figure_number=3
)


# now lets make a correlation plot
data_plot.correlation(
    to_correlate='vendas',
    title='Correlação das Vendas',
    figure_number=4,
)

data_plot.correlation(
    to_correlate='aumento',
    title='Correlação do Aumento',
    figure_number=5,
)

data_plot.correlation(
    to_correlate='aceleracao',
    title='Correlação da Aceleração',
    figure_number=6,
)
