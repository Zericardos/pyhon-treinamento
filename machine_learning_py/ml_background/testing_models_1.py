#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 09:13:50 2021

@author: ricardo
"""


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from itertools import compress


def split_sets(X_DataFrame, Y_DataFrame, train_size=.8):

    # separate in three sets for training and predict
    x_train, x_test_validation, y_train, y_test_validation = train_test_split(
        X_DataFrame, Y_DataFrame, train_size=train_size, stratify=y_df)

    x_test, x_validation, y_test, y_validation = train_test_split(
        x_test_validation, y_test_validation, train_size=.5, stratify=y_test_validation)

    return x_train, x_test, x_validation, y_train, y_test, y_validation


def predict_result_test(
        x_train, x_test, y_train, y_test, model, print_score=True):

    # train and test our model
    model.fit(x_train, y_train)
    y_predict_test = model.predict(x_test)

    accuracy_test = accuracy_score(y_test, y_predict_test) * 100
    if print_score:
        print(f'\nThe accuracy of {model} was {accuracy_test:.2f}%')

    return model, accuracy_test


busca_tabela = pd.read_csv('busca.csv')

# set seed to fix control random choices
SEED = 8
np.random.seed(SEED)

# make features, result DataFrames
X = busca_tabela[['home', 'busca', 'logado']]
Y = busca_tabela['comprou']

# improve type feature with dummies
x_dummies_df = pd.get_dummies(X)
y_df = Y.copy()

x_train, x_test, x_validation, y_train, y_test, y_validation = split_sets(x_dummies_df,
                                                                          y_df)

# test our models
# begin with multinomialNB
multinomialnb_model, multinomialnb_result = predict_result_test(
    x_train,
    x_test, y_train, y_test,
    MultinomialNB())

# To our base algorithm, we have five options, but I'll use four and take those
# which give best results
strategies = ["stratified", "most_frequent", "prior", "uniform"]
test_aux = []
model_aux = []
accuracy_aux = []
aux_index = np.arange(len(strategies))

for i, j in enumerate(strategies):
    test_aux.append((predict_result_test(
        x_train, x_test, y_train, y_test,
        DummyClassifier(
            strategy=j))))
    model_aux.append(test_aux[i][0])
    accuracy_aux.append(test_aux[i][1])

maximum_accuracy_index = accuracy_aux == max(accuracy_aux)
models = list(compress(model_aux, maximum_accuracy_index))

adaboost_model, adaboost_result = predict_result_test(
    x_train, x_test, y_train, y_test,
    AdaBoostClassifier())

# Which are winner?
if adaboost_result >= multinomialnb_result:
    vencedor = adaboost_model
else:
    vencedor = multinomialnb_model


def final_test(x_validation, y_validation, model):

    y_final_predict = model.predict(x_validation)
    accuracy_test = accuracy_score(y_validation, y_final_predict) * 100

    print(f'\nThe final accuracy of {model} was {accuracy_test:.2f}%')


models.append(vencedor)

for model in models:
    final_test(x_validation, y_validation, model)
    final_test(x_validation, y_validation, model)
for model in models:
    final_test(x_validation, y_validation, model)
