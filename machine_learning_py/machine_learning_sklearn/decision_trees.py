#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:53:10 2021

@author: ricardo
"""

from subprocess import call
from sklearn.dummy import DummyClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from datetime import datetime
import pandas as pd
import numpy as np
import graphviz

"""In colab, use !pip install graphviz
and install on the system, apt-get install graphviz"""

file_address = "https://gist.githubusercontent.com/guilhermesilveira/4d1d4a16ccbf6ea4e0a64a38a24ec884/raw/afd05cb0c796d18f3f5a6537053ded308ba94bf7/car-prices.csv"

car_table = pd.read_csv(file_address)

# save to csv

# car_table.to_csv('car_table.csv', index = False)

# Translate it to portuguese

new_column = {
    'mileage_per_year': 'milhas_por_ano', 'model_year': 'ano_do_modelo',
    'price': 'preco', 'sold': 'vendido'}

car_table.rename(columns=new_column, inplace=True)

# convert vendido column into binary values

vendido_novo = {'no': 0, 'yes': 1}

car_table.vendido = car_table.vendido.map(vendido_novo)

# insert new column km_por_ano with proper values

car_table['km_por_ano'] = car_table.milhas_por_ano * 1.60934

""" Due ano_do_modelo be one hundred greater than difference between actual year and year
of manufactore, we reduced it to the appropriate difference. So, a scaling typing"""

car_table['idade_do_modelo'] = datetime.today().year - car_table.ano_do_modelo

# full translate and take only interested values

tabela_de_carros = car_table[[
    'preco', 'km_por_ano', 'idade_do_modelo', 'vendido']]

# Now teste our DecisionTreeClassifier model with scaling in X

x_feature_names = ['preco', 'km_por_ano', 'idade_do_modelo']

x = tabela_de_carros[x_feature_names]

y = tabela_de_carros['vendido']

SEED = 24

np.random.seed(SEED)

raw_x_train, raw_x_test, y_train, y_test = train_test_split(x, y, train_size=0.75,
                                                            stratify=y)
model = DecisionTreeClassifier(max_depth=2)

model.fit(raw_x_train, y_train)

y_predict = model.predict(raw_x_test)

accuracy = accuracy_score(y_test, y_predict) * 100

print(f'The accuracy was {accuracy:.2f}%')

# Now, we have to test which baseline algorithm will have the best result.
# Then, use it as baseline and our model must be better than that.1

# We use DummyClassifier and its strategies, e.g, stratified, most_frequent,
# prior, uniform

# blind_guess_predict = np.ones(len(y_test))

dummy = DummyClassifier(strategy='most_frequent')

dummy.fit(raw_x_train, y_train)

blind_guess_predict = dummy.predict(raw_x_test)

accuracy_guess = accuracy_score(y_test, blind_guess_predict) * 100

print(f'The accuracy of the baseline algorithm was {accuracy_guess:.2f}%')

# Then make graphs

# Export dot_data

# Not create a file
# Export as dot file

dot_data = export_graphviz(
    model, out_file='dot_data3.dot', feature_names=x_feature_names,
    class_names=["Não", "Sim"], rounded=True, proportion=False, filled=True)

# Convert to png using system command (requires Graphviz)


call(['dot', '-Tpng', 'dot_data3.dot', '-o', 'tree3.png', '-Gdpi=600'])

"""# Display in jupyter notebook
from IPython.display import Image
Image(filename = 'tree.png')

or forget some lines, which?

Visualizing the file, use Okular, we see that some price are negative due to
normalization. But DecisionTree Algorithms don't need to do so."""
