#-------------------------------------------------------------------------------
# This file contains presets for different types of pie charts
# Contents are pretty much boilerplate code; either cut and paste or import this
#   file into your driver file
#-------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import AutoMinorLocator, MultipleLocator
import pandas as pd


def calculate_exponential_decay(initial_amount, decay_rate, time):
    data_list = [initial_amount*((1-(decay_rate/100))**t) for t in range(0, time, 1)]
    return data_list

def calculate_x_axis_pos(number_of_items, unit):
    start = 0
    stop = (number_of_items-1)*unit
    array = np.linspace(start, stop, number_of_items)
    return array

def line_graph_basic(input_y_data, input_x_data, input_labels, xy_labels, output_file_name):
    #Set font
    set_default_font()

    #Generate graph and data traces
    fig, ax = plt.subplots(figsize=(10,8))

    ax.plot(input_x_data, input_y_data[0], color='red', marker='s', markersize=8)
    ax.plot(input_x_data, input_y_data[1], color='blue', marker='o', markersize=8)

    #Set axis labels
    ax.set_ylabel(xy_labels[0], fontsize=24, labelpad=10, weight='bold')
    ax.set_xlabel(xy_labels[1], fontsize=24, labelpad=5, weight='bold')

    #Set axis ranges
    ax.set_xlim(-0.25, 10.25)
    ax.set_ylim(-0.25, 101)

    #Set major and minor ticks
    ax.xaxis.set_major_locator(MultipleLocator(2))
    ax.xaxis.set_minor_locator(AutoMinorLocator(2))

    ax.yaxis.set_major_locator(MultipleLocator(20))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))

    #Set line widths
    set_line_properties()

    #Set tick length and width
    ax.tick_params(which='major', length=7, width=2)
    ax.tick_params(which='minor', length=4, width=2)

    #Set legend
    ax.legend(labels, loc="center right", fontsize=20, bbox_to_anchor=(1.35,0.5))

    #Write to file
    plt.savefig(output_file_name, bbox_inches='tight', pad_inches = 0.1)

def set_default_font():
    mpl.rcParams['font.size'] = 24
    mpl.rcParams['font.family'] = 'sans-serif'
    mpl.rcParams['font.sans-serif'] = ['Tahoma']
    mpl.rcParams['font.weight'] = 'bold'

def set_line_properties():
    mpl.rcParams['lines.linewidth'] = 4
    mpl.rcParams['axes.linewidth'] = 2


#-------------------------------------------------------------------------------
# Basic linegraph - Sample
#-------------------------------------------------------------------------------

#Data and labels
labels = ['Sample 1', 'Sample 2']
y_data = [
    calculate_exponential_decay(100, 50, 100),
    calculate_exponential_decay(100, 20, 100)
    ]
x_data = calculate_x_axis_pos(len(y_data[0]), 1)

#Axis labels
xy_axis_labels = ['Amount Remaining (kg)', 't (years)']

#Output file name
file_name = 'output_line_graph.png'

#Generate graph
line_graph_basic(y_data, x_data, labels, xy_axis_labels, file_name)