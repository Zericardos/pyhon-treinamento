#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise VII

# ## Criando Agrupamentos

# In[2]:


import pandas as pd


# In[3]:


dados = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')


# In[4]:


dados.head(10)

dados['Valor'].mean()

# #### https://pandas.pydata.org/pandas-docs/stable/api.html#api-dataframe-stats

bairros = dados.Bairro.unique()

type(bairros)

bairros[:8]

bairros_2 = ['Copacabana', 'Jardim Botânico', 'Centro', 'Higienópolis',
       'Cachambi', 'Barra da Tijuca']


selecao = dados['Bairro'].isin(bairros_2)
dados = dados[selecao]
dados

dados['Bairro'].drop_duplicates() 

# ### Criando grupos

grupo_bairro = dados.groupby('Bairro')


# #### Getting more information


for bairro, dados in grupo_bairro:
    print(bairro, type(dados), dados)


# In[23]:





# In[ ]:




