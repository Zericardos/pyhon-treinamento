#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:20:06 2021

@author: ricardo
"""


# Download file git clone https://github.com/alura-cursos/...
# reducao-dimensionalidade

from sklearn.dummy import DummyClassifier
import pandas as pd
from numpy.random import seed
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

results_diagnostics = pd.read_csv('exames.csv')

# First we must analyse our data
# results_diagnostics.head()
# results_diagnostics.isnull.any()
# We see that last column has NaN values, so how many?
# results_diagnostics.isnull.sum() -> 419
# We have 569 values, but 419 with NaN in exame_33. This represents
# 74%, a lot. So we'll drop this column

results_diagnostics.drop(columns='exame_33', inplace=True)

# So this way we can train our algorithm

exams_values = results_diagnostics.drop(
    columns=['id', 'diagnostico'])

diagnostics_values = results_diagnostics.diagnostico

# seed value to reproduce the test
SEED = 1223
seed(SEED)
test_size = .3

train_x, test_x, train_y, test_y = train_test_split(
    exams_values, diagnostics_values, test_size=test_size,
    stratify=diagnostics_values)


# Our base classifier, dummy
dummy_classifier = DummyClassifier(strategy='most_frequent')
dummy_classifier.fit(train_x, train_y)

# Our real classifier, RandomForest
classifier = RandomForestClassifier(n_estimators=100)
classifier.fit(train_x, train_y)
print(
    f"\nOur classifier accuracy score is {classifier.score(test_x, test_y) * 100:.2f}%")
print(
    f"\nOur classifier accuracy score is {dummy_classifier.score(test_x, test_y) * 100:.2f}%")
