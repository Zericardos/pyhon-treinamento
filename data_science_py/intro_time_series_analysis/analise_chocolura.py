#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 07:51:24 2021

@author: ricardo
"""


from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd
from plot_timeseries import MultiplePlots as mp
from matplotlib import pyplot as plt

chocolura = pd.read_csv('data/chocolura.csv')
chocolura.mes = pd.to_datetime(chocolura.mes)
print('Campos da tabela Chocolura: ', chocolura.keys())
print('Quantidade de dados nulos: ', chocolura.isna().sum().sum())

chocolura['aumento'] = chocolura['vendas'].diff()
chocolura['aceleracao'] = chocolura['aumento'].diff()

# campos do DataFrame
ys = ['vendas', 'aumento', 'aceleracao']
ylabels = ['Vendas (R$)', 'Aumento', 'Aceleração']
xlabel = 'Tempo (meses)'

data_plots = mp.lines(
    x='mes',
    ys=ys,
    dataframe=chocolura,
    title="Análise de Vendas da Chocolura de 2017 e 2018",
    xlabel='Tempo (meses)',
    ylabels=ylabels,
    figure_number=0
)
""" o valor do parâmetro period retorna a análise em unidades de frequência.
Quanto maior period, perde-se informações a respeito de tendência, ruído e
observações, por exemplo.
Armazenamos a lista em todas as variáveis. Agora, criaremos um DataFrame com todos esses valores. Visualizaremos ele logo depois.
"""
resultado = seasonal_decompose(chocolura['vendas'], period=1)
plt.figure(num=1, figsize=(16, 12))
ax = resultado.plot()

observacao = resultado.observed
tendencia = resultado.trend
sazonalidade = resultado.seasonal
ruido = resultado.resid

data = ({
    'observacao': observacao,
    'tendencia': tendencia,
    'sazonalidade': sazonalidade,
    'ruido': ruido
})
resultado = pd.DataFrame(data)
print(resultado.head)
"""Então, teremos o valor do ruído dessa nossa observação. Mas deixaremos
mesmo como a sazonalidade, pois criamos uma função para plotar apenas 3
gráficos.

O Statsmodels, portanto, é um exemplo de como podemos utilizar uma função para
visualizar todas as informações que desejamos. Vimos também que a frequência é
muito importante para que os resultados sejam visualizados corretamente.

A documentação da frequência poderá ser acessada quando, no trecho do código
em que ela aparece "freq=3,...", digitarmos uma vírgula e apertarmos "Enter".
Esse documento dirá que essa será uma int opcional. No entanto, a partir da
versão do Pandas que estamos utilizando no curso, o Colab não permitirá que
ela seja opcional. Precisaremos passá-la para ter um entendimento mais claro,
já que estamos trabalhando com Series. """
