#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:20:06 2021

@author: ricardo
"""


# Download file git clone https://github.com/alura-cursos/...
# reducao-dimensionalidade

from sklearn.preprocessing import StandardScaler
from sklearn.dummy import DummyClassifier
import pandas as pd
from numpy.random import seed
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns

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


# Now lets take a plot to see distribution between malign (M) and benign (B)
# We will use violinplot
# First we will evaluate about exam_1, so

# data_plot = pd.concat([diagnostics_values, exams_values.iloc[:, :10]],
# axis=1)
# #formatting to plot in violinplot
# data_plot = pd.melt(
#     data_plot, id_vars="diagnostico", var_name="exames", value_name="valores"
# )

# but before we plot, we can inspect the data_plot and notice that Y values
# are big and small, so we will standard it with StandardScaler. And do it
# before create data_plot.
# StandardScaler returns an numpy array, so we must create another DataFrame
# before we create data_plot again


standardizer = StandardScaler()
standardizer.fit(exams_values)
standardized_exams_values_array = standardizer.transform(exams_values)
# Constructing a DataFrame again, standardized this time
standardized_exams_values = pd.DataFrame(
    data=standardized_exams_values_array,
    columns=exams_values.keys()
)

plt.close('all')
figure_size = (21, 10)
figure_number = 1


def violin_graph(
        values,
        start,
        end,
        figsize=figure_size,
        nfig=figure_number
):
    # Now create our data_plot
    data_plot = pd.concat(
        [diagnostics_values, values.iloc[:, start:end]],
        axis=1
    )
    # formatting to plot in violinplot
    data_plot = pd.melt(
        data_plot,
        id_vars="diagnostico",
        var_name="exames",
        value_name="valores"
    )
    plt.figure(nfig, figsize)
    sns.violinplot(
        x="exames",
        y="valores",
        hue="diagnostico",
        data=data_plot,
        split=True
    )
    plt.xticks(rotation=90)


# Plotting we notice some relevance exams in this interval. However, exame_4
# shows a constant distribution, that adds no information, so we discard it
# In adition, we create a function to plot the graph everytime we need
violin_graph(standardized_exams_values, 21, 28)
