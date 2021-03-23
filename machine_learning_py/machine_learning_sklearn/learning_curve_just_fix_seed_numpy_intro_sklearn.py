#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 10:09:44 2021

@author: ricardo
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

file_address = 'https://gist.githubusercontent.com/guilhermesilveira/1b7d5475863c15f484ac495bd70975cf/raw/16aff7a0aee67e7c100a2a48b676a2d2d142f646/projects.csv'

budget_table = pd.read_csv(file_address)

budget_table.rename(columns={'unfinished': 'finished'}, inplace=True)

value_changes = {0: 1, 1: 0}

budget_table['finished'] = budget_table.finished.map(value_changes)

x = budget_table[['expected_hours', 'price']]

y = budget_table['finished']

SEED = 2447

np.random.seed(SEED)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.75,
                                                    stratify=y)
model = LinearSVC()

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

accuracy = accuracy_score(y_test, y_predict) * 100

print(f'The accuracy was {accuracy:.2f}%')

blind_guess_predict = np.ones(len(y_test))
accuracy_guess = accuracy_score(y_test, blind_guess_predict) * 100

print(f'The accuracy of the baseline algorithm was {accuracy_guess:.2f}%')
plt.close('all')

plt.figure(1)
# hue acepts array too, so data must be x array and hue y array
ax1 = sns.scatterplot(x="expected_hours", y="price", hue=y_test, data=x_test)
ax1.set_title('Hours Distribution')

# But a quantitative analysis is not enough, we must see the distribution
# points in all possible values to assess the behavior of our algorithm. Lets
# see them, possible only in two dimensions

# According to graph

x_min = x_test.expected_hours.min()
x_max = x_test.expected_hours.max()
y_min = x_test.price.min()
y_max = x_test.price.max()

print(x_min, x_max, y_min, y_max)

# Lets create a 100x100 grid in those limits. The more pixels I put, more
# readable it will be for me. However, 100 pixel are enough for good reading

pixels = 100

x_pixels_axis = np.arange(x_min, x_max, (x_max - x_min) / pixels)

y_pixels_axis = np.arange(y_min, y_max, (y_max - y_min) / pixels)

# Let's join the formed axes in a grid
# Meshgrid return x_axis, y_axis pixels times repeated. We still don't want
# that
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

# Model got rith, one color, got wrong, another. Make a another color
# to contour between decisions, a BOUNDARY DECISION countour where the model
# chooses right or wrong

plt.contourf(xx, yy, Z, alpha=.3)
plt.scatter(x_test.expected_hours, x_test.price, c=y_test, s=5)

# We saw that model was very bad because we used SVC, and that only works
# to one 1-D line and our data hasn't a straight distribution.

# Another problem is a randomness of the linearSVC model - random_state
# parameter -, that is, every time we train our algorithm, we train it
# differently. Remember that the seed only was applied only in separation of
# training and test sets. So we are going to create a copy of this file in
# which we use the same seed in the training. Thus, we'll be able to replicate
# our result always
