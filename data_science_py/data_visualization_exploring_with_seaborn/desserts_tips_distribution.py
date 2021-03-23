#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 15:19:01 2021

@author: ricardo
"""

from scipy.stats import ranksums
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = pd.read_csv('tips.csv')

renomear = {
    'total_bill': 'valor_da_conta',
    'tip': 'gorjeta',
    'dessert': 'sobremesa',
    'day': 'dia_da_semana',
    'time': 'hora_do_dia',
    'size': 'total_de_pessoas'
}

gorjetas = tips.rename(columns=renomear)

sim_nao = {
    'No': 'Não',
    'Yes': 'Sim'
}

gorjetas.sobremesa = gorjetas.sobremesa.map(sim_nao)

dias = {
    'Sun': 'Domingo',
    'Sat': 'Sábado',
    'Thur': 'Quinta',
    'Fri': 'Sexta'
}

gorjetas.dia_da_semana = gorjetas.dia_da_semana.map(dias)

hora = {
    'Dinner': 'Jantar',
    'Lunch': 'Almoço'
}

gorjetas.hora_do_dia = gorjetas.hora_do_dia.map(hora)

# Valor da conta e da gorjeta

figsize = (21, 10)
plt.close('all')
figure_number = 1
plt.figure(figure_number, figsize)
graphico_valor_gorjeta = sns.scatterplot(x='valor_da_conta', y='gorjeta',
                                         data=gorjetas)
graphico_valor_gorjeta.set_title('Gráfico valor da gorjeta')
graphico_valor_gorjeta.figure.suptitle('scatterlot')
# Visualmente, a gorjeta aumenta com o valor da conta
print(f"Temos um total de {gorjetas.shape[0]} registros. \n")
print(f"E um total {gorjetas.count()} de registros não nulos ")

# Criando o campo porcentagem
gorjetas['porcentagem'] = round(100 * (gorjetas['gorjeta'] / gorjetas
                                       ['valor_da_conta']), 2)

figure_number += 1
plt.figure(figure_number, figsize)
graphico_valor_gorjeta_proporcional = sns.scatterplot(x='valor_da_conta',
                                                        y='porcentagem',
                                                        data=gorjetas)
graphico_valor_gorjeta_proporcional.set_title(
    'Gráfico valor da gorjeta proporcional')
graphico_valor_gorjeta_proporcional.figure.suptitle('scatterlot')
# Visualmente, a gorjeta não aumenta proporcionalmente com o valor da conta

# Gráfico de linha, poucos valores tornam a densidade baixa
figure_number += 1
plt.figure(figure_number, figsize)
grafico_valorgorjeta_porcentagem_linha = sns.relplot(x='valor_da_conta',
                                                     y='porcentagem',
                                                     kind='line',
                                                     data=gorjetas)
grafico_valorgorjeta_porcentagem_linha.set_titles(
    'Gráfico Valor Gorjeta x Porcentagem')
grafico_valorgorjeta_porcentagem_linha.fig.suptitle('relplot, kind=line')
# draw a scatterplot of two variables, x and y, and then fit the regression
# model y ~ x and plot the resulting regression line and a 95% confidence
# interval for that regression

figure_number += 1
plt.figure(figure_number, figsize)
grafico_valor_gorjeta_porcentagem_regressao = sns.lmplot(x='valor_da_conta',
                                                         y='porcentagem',
                                                         data=gorjetas)
grafico_valor_gorjeta_porcentagem_regressao.set_titles('Gráfico Valor  \
                                                         Gorjeta x Porcentagem\
                                                              - Regressão')
grafico_valor_gorjeta_porcentagem_regressao.fig.suptitle('lmplot')
# Segunda análise

# Quantas pessoas pediram sobremesa
print(gorjetas[gorjetas.sobremesa == 'Sim'].describe().round(2))

# Quantas pessoas não pediram sobremesa
print(gorjetas[gorjetas.sobremesa == 'Não'].describe().round(2))

# Ordering a dessert changes the tip value?

figure_number += 1
plt.figure(figure_number, figsize)
grafico_valorgorjetas_gorjetas_vertical = sns.catplot(x='sobremesa',
                                                      y='gorjeta',
                                                      data=gorjetas)
grafico_valorgorjetas_gorjetas_vertical.set_titles(
    'Gráfico Valor Gorjeta x Gorjetas - Vertical')
grafico_valorgorjetas_gorjetas_vertical.fig.suptitle('catplot')


# Avaliate distribution
figure_number += 1
plt.figure(figure_number, figsize)
graphico_valorgorjeta_gorjeta_distribuicao = sns.relplot(
    x='valor_da_conta',
    y='gorjeta',
    hue='sobremesa',
    data=gorjetas)
graphico_valorgorjeta_gorjeta_distribuicao.set_titles(
    'Gráfico Valor Gorjeta x Gorjetas - Distribuição')
graphico_valorgorjeta_gorjeta_distribuicao.fig.suptitle(
    'relplot, hue=sobremesa')

# Two plots
figure_number += 1
plt.figure(figure_number, figsize)
grafico_valorgorjeta_gorjeta_two = sns.relplot(
    x='valor_da_conta', y='gorjeta',
    col='sobremesa',
    hue='sobremesa', data=gorjetas)
grafico_valorgorjeta_gorjeta_two.set_titles(
    'Segundo Gráfico Valor Gorjeta x Gorjetas')
grafico_valorgorjeta_gorjeta_two.fig.suptitle(
    'relplot, hue=sobremesa')

# Two plots, same color
figure_number += 1
plt.figure(figure_number, figsize)
grafico_valorgorjetas_gorjetas_two_same_color = sns.relplot(
    x='valor_da_conta',
    y='gorjeta',
    col='sobremesa',
    data=gorjetas)
grafico_valorgorjetas_gorjetas_two_same_color.set_titles(
    "Segundo Gráfico: Valor Gorjeta x Gorjetas")
grafico_valorgorjetas_gorjetas_two_same_color.fig.suptitle(
    'relplot, col=sobremesa')

# Avaliate distribution in regression model
figure_number += 1
plt.figure(figure_number, figsize)
grafico_valorgorjeta_regressao = sns.lmplot(
    x='valor_da_conta', y='gorjeta',
    col='sobremesa', hue='sobremesa',
    data=gorjetas)
grafico_valorgorjeta_regressao.set_titles(
    "Gráfico Valor Gorjeta x Gorjetas - Regressão")
grafico_valorgorjeta_regressao.fig.suptitle(
    'lmplot, hue=sobremesa, col=sobremesa')

# Avaliate distribution in regression model
figure_number += 1
plt.figure(figure_number, figsize)
graphico_valorgorjeta_porcentagem_regressao = sns.lmplot(
    x='valor_da_conta',
    y='porcentagem',
    col='sobremesa',
    hue='sobremesa',
    data=gorjetas)

graphico_valorgorjeta_porcentagem_regressao.set_titles(
    "Gráfico Valor Porcentagem x Gorjetas - Regressão")
graphico_valorgorjeta_porcentagem_regressao.fig.suptitle(
    'lmplot, hue=sobremesa, col=sobremesa')
print("Visualmente, existe uma diferença no valor da gorjeta daqueles que  pediram sobremesa e não pediram sobremesa. Entretanto, essa diferença é muito sutil, vamos fazer um cálculo estatístico a respeito")

print("\n\nTeste de Hipótese")

print("\nHipótese Nula:\n A distribuição da taxa da gorjeta é a mesma nos dois grupos")

print("\nHipótese Não Nula:\n A distribuição da taxa da gorjeta não é a mesma nos dois grupos")

plt.close('all')

# first lets take the percentage of everyone who ordered dessert

porcentagem_gorjetas = gorjetas.query("sobremesa == 'Sim'").porcentagem
porcentagem_nao_gorjetas = gorjetas.query("sobremesa == 'Não'").porcentagem

# Statistics parameter
r = ranksums(porcentagem_gorjetas, porcentagem_nao_gorjetas)
