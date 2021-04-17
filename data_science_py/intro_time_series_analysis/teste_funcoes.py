#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 22:48:31 2021

@author: ricardo
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import autocorrelation_plot

time_sales_df = pd.read_csv('data/alucar.csv')
time_sales_df['aumento'] = time_sales_df['vendas'].diff()
time_sales_df['aceleracao'] = time_sales_df['aumento'].diff()

correlations_ylabels = ['Vendas', 'Aumento', 'Aceleração']

dataframe = times_sales_df


figure_number = 0

ax = autocorrelation_plot(time_sales_df['vendas'])
ax.set_title('Correlação das Vendas', loc='left', fontsize=18)
ax = ax


ylabels = ['Correlação de ' + i for i in correlations_ylabels]
plt.figure(num=figure_number, figsize=(16, 12))
ax = plt.subplot(len(ys), 1, 1)
ax.set_title(title, loc='left', fontsize=18)
# ax.set_xlabel(xlabel, fontsize=14)

for i, (y, ylabel) in enumerate(zip(ys, ylabels)):

    ax = plt.subplot(len(ys), 1, i + 1)
    sns.lineplot(x=x, y=y, data=dataframe)
    ax.set_ylabel(ylabel, fontsize=14)

ax.set_xlabel(xlabel, fontsize=14)
ax = ax
