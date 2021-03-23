#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 13:04:20 2021

@author: ricardo
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

file_address = 'https://gist.githubusercontent.com/guilhermesilveira/1b7d5475863c15f484ac495bd70975cf/raw/16aff7a0aee67e7c100a2a48b676a2d2d142f646/projects.csv'

budget_table = pd.read_csv(file_address)

budget_table.rename(columns={'unfinished': 'finished'}, inplace=True)

value_changes = {0: 1, 1: 0}

budget_table['finished'] = budget_table.finished.map(value_changes)

x = budget_table[['expected_hours', 'price']]

y = budget_table['finished']

SEED = 2447

np.random.seed(SEED)

raw_x_train, raw_x_test, y_train, y_test = train_test_split(
    x, y, train_size=0.75,
    stratify=y)

# Scaling our features

scaler = StandardScaler()

scaler.fit(raw_x_train)

# Transforming will return an array of arrays, not DataFrame

x_train = scaler.transform(raw_x_train)

x_test = scaler.transform(raw_x_test)

# So we modify our data to plot

model = SVC()

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

accuracy = accuracy_score(y_test, y_predict) * 100

print(f'The accuracy was {accuracy:.2f}%')

blind_guess_predict = np.ones(len(y_test))
accuracy_guess = accuracy_score(y_test, blind_guess_predict) * 100

print(f'The accuracy of the baseline algorithm was {accuracy_guess:.2f}%')
plt.close('all')

# We modified here

data_x = x_test[:, 0]

data_y = x_test[:, 1]

plt.figure(1)
# hue acepts array too, so data must be x array and hue y array
ax1 = sns.scatterplot(x=data_x, y=data_y, hue=y_test, data=x_test)
ax1.set_title('Hours Distribution')

# But a quantitative analysis is not enough, we must see the distribution
# points in all possible values to assess the behavior of our algorithm. Lets
# see them, possible only in two dimensions

# According to graph

x_min = data_x.min()
x_max = data_x.max()
y_min = data_y.min()
y_max = data_y.max()

print(x_min, x_max, y_min, y_max)

# Lets create a 100x100 grid in those limits. The more pixels I put, more
# readable it will be for me. However, 100 pixel are enough for good reading

pixels = 100

x_pixels_axis = np.arange(x_min, x_max, (x_max - x_min) / pixels)

y_pixels_axis = np.arange(y_min, y_max, (y_max - y_min) / pixels)

# Let's join the formed axes in a grid
# Meshgrid return x_axis, y_axis pixels times repeated.We still don't want that
xx, yy = np.meshgrid(x_pixels_axis, y_pixels_axis)

# xx.ravel() really join the x_axis. Then, we use np.c_ to concatenate them.
# np.c_ operates as dictionaries, operating [] instead ().

# Concatanation to form grid, every pairs were formed

grid = np.c_[xx.ravel(), yy.ravel()]

# To avaliate our predict distribution, we must check our predict shape.
# Clearly, it won't have the same shape because we splitted our set. But we
# want to predict every possible subjects we have and avaliate the behavior

Z = model.predict(grid)

# but it wasn't in format. So, reshape it!

Z = Z.reshape(xx.shape)

# Finally we'll plot them! We want a thorough control, so we use matplotlib

plt.figure(2, (16, 10))

#  Model got right, one color, got wrong, another. Make a another color
# to contour between decisions, a BOUNDARY DECISION countour where the model
# makes decision

plt.contourf(xx, yy, Z, alpha=.3)
plt.scatter(data_x, data_y, c=y_test, s=5)

# We saw that model was very improved because we scaled our features in the
# similar way and used SVC model instead LinearSVC
