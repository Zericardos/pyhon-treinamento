#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 20:41:14 2021

@author: ricardo
"""


import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import autocorrelation_plot


class PlotDf:
    """Plot one plot per figure"""

    def __init__(
            self,
            dataframe,
            figure_size=(12, 6)
    ):
        """
        Init PlotDf

        Parameters
        ----------
        dataframe : Pandas DataFrame
            dataframe with data to be plot.



        figure_size : 2D tuple with int values, optional
            Size of the figure to plot. The default is (12, 6).

        Returns
        -------
        None.

        """
        self.dataframe = dataframe
        self.figure_size = figure_size

    def line(
            self,
            x_tag: str,
            y_tag: str,
            title: str,
            xlabel: str,
            ylabel: str,
            figure_number=0
    ):
        """Plot line

        Parameters
        ----------
        x_tag : str
            DataFrame tag to plot on the x axis .

        y_tag : str
            DataFrame tag to plot on the y axis.

        title : str
            Title of the lineplot.

        xlabel : str
            xlabel of the lineplot.

        ylabel : str
            ylabel of the lineplot.

        figure_number : int, optional
            Number of the figure to plot. The default is 0.

        Returns
        -------
        None.

        """
        plt.figure(
            num=figure_number,
            figsize=self.figure_size
        )
        ax = sns.lineplot(x=x_tag, y=y_tag, data=self.dataframe)
        sns.set_palette('Accent')
        sns.set_style('darkgrid')
        ax.set_title(title, loc='left', fontsize=18)
        ax.set_xlabel(xlabel, fontsize=14)
        ax.set_ylabel(ylabel, fontsize=14)
        ax = ax

    def correlation(self, to_correlate: str, title, figure_number=0
                    ):
        plt.figure(
            num=figure_number,
            figsize=self.figure_size
        )
        if self.dataframe[to_correlate].isna().sum() > 0:
            self.dataframe = self.dataframe[
                self.dataframe[
                    to_correlate
                ].notna()
            ]
        ax = autocorrelation_plot(self.dataframe[to_correlate])
        ax.set_title(title, loc='left', fontsize=18)
        ax = ax


class MultiplePlots:
    """Multiple Plots within same figure and same x-axis"""

    def lines(
            x: str,
            ys: list,
            dataframe,
            title: str,
            xlabel: str,
            ylabels: list,
            figure_number=0
    ):
        """
        Line plots

        Parameters
        ----------
        x : str
            header in dataframe
        ys : list
            list of headers in dataframe
        dataframe : Pandas DataFrame
            Contains data to be plot
        title : str
            Title of the figure.
        xlabel : str
            xlabel of the figure.
        ylabels : list
            ylabel in order to each plot.
        figure_number : int, optional
            Number of the figure. The default is 0.

        Returns
        -------
        None.

        """
        plt.figure(num=figure_number, figsize=(16, 12))
        sns.set_palette('Accent')
        sns.set_style('darkgrid')
        ax = plt.subplot(len(ys), 1, 1)
        ax.set_title(title, loc='left', fontsize=18)

        # ax.set_xlabel(xlabel, fontsize=14)

        for i, (y, ylabel) in enumerate(zip(ys, ylabels)):

            ax = plt.subplot(len(ys), 1, i + 1)
            sns.lineplot(x=x, y=y, data=dataframe)
            ax.set_ylabel(ylabel, fontsize=14)

        ax.set_xlabel(xlabel, fontsize=14)
        ax = ax


"""
        def correlations(
            correlations: list,
            dataframe,
            title: str,
            ylabels: list,
            figure_number=0
        ):
"""
