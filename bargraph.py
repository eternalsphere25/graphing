#-------------------------------------------------------------------------------
# This file contains presets for different types of bar graphs
# Contents are pretty much boilerplate code; either cut and paste or import this
#   file into your driver file
#-------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.ticker import AutoMinorLocator, MultipleLocator


def bar_graph_basic(input_data, input_stdev, input_labels, ax_labels, y_max, output_file_name):
    #Set text font
    set_default_font()

    #Calculate bar label positions
    x_pos = calculate_x_axis_label_pos(len(input_labels))

    #Generate bar graph
    fig, ax = plt.subplots(figsize=(10,8))
    ax.bar(x_pos, input_data, width=0.4, yerr=input_stdev, capsize=20)

    #Set axis labels
    ax.set_ylabel(ax_labels[1], fontsize=24, labelpad=24, weight='bold')
    ax.set_xlabel(ax_labels[0], fontsize=24, labelpad=8, weight='bold')

    #Set axis ranges and labels
    ax.set_ylim(-1, y_max+1)
    ax.yaxis.set_major_locator(MultipleLocator(5))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))
    ax.set_xticks(x_pos)
    ax.set_xticklabels(input_labels)

    #Set tick styles
    ax.tick_params(which='major', length=8, width=2)
    ax.tick_params(which='minor', length=6, width=2)

    #Set axis linewidth
    set_axes_linewidth()

    #Generate graph
    plt.savefig(output_file_name, bbox_inches='tight', pad_inches = 0.1)

def bar_graph_multi(input_data, input_labels, x_labels, y_label, y_max, output_file_name):
    #Set text font
    set_default_font()

    #Set bar width
    x = np.arange(len(x_labels))
    width = 0.2

    #Generate graph and bars
    fig, ax = plt.subplots(figsize=(10,8))
    rects1 = ax.bar(x-width*(3/2), input_data[0], width, label=input_labels[0])
    rects2 = ax.bar(x-width/2, input_data[1], width, label=input_labels[1])
    rects3 = ax.bar(x+width/2, input_data[2], width, label=input_labels[2])
    rects4 = ax.bar(x+width*(3/2), input_data[3], width, label=input_labels[3])

    #Set x and y axis labels
    ax.set_ylabel(y_label[0], fontsize=36, labelpad=24, weight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)

    #Set axis ranges
    ax.set_ylim(0, y_max+1)
    ax.yaxis.set_major_locator(MultipleLocator(2))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))

    #Set axis linewidth
    set_axes_linewidth()

    #Generate legend
    ax.legend()

    #Save to disk
    plt.savefig(output_file_name, bbox_inches='tight', pad_inches = 0.1)

def bar_graph_stacked(input_data, input_labels, x_labels, y_label, y_max, output_file_name):
    #Set font
    set_default_font()

    #Bar width and heights
    width = 0.5
    bar_12 = np.add(input_data[0], input_data[1]).tolist()
    bar_123 = np.add(bar_12, input_data[2]).tolist()
    bar_1234 = np.add(bar_123, input_data[3]).tolist()

    #Generate graph and bars
    fig, ax = plt.subplots(figsize=(10,8))
    p1 = ax.bar(x_labels, input_data[0], width, label=input_labels[0])
    p2 = ax.bar(x_labels, input_data[1], width, bottom=input_data[0], label=input_labels[1])
    p3 = ax.bar(x_labels, input_data[2], width, bottom=bar_12, label=input_labels[2])
    p4 = ax.bar(x_labels, input_data[3], width, bottom=bar_123, label=input_labels[3])
    p5 = ax.bar(x_labels, input_data[4], width, bottom=bar_1234, label=input_labels[4])

    #Set axis labels
    ax.set_ylabel(y_label[0], fontsize=36, labelpad=24, weight='bold')

    #Set axis ranges and labels
    ax.set_ylim(0, y_max+1)
    ax.yaxis.set_major_locator(MultipleLocator(4))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))

    #Set axis linewidth
    set_axes_linewidth()

    #Set bar data labels [Step 1/3: Generate label numbers]
    label1 = convert_list_of_int_to_str(input_data[0])
    label2 = convert_list_of_int_to_str(input_data[1])
    label3 = convert_list_of_int_to_str(input_data[2])
    label4 = convert_list_of_int_to_str(input_data[3])
    label5 = convert_list_of_int_to_str(input_data[4])

    #Set bar data labels [Step 2/3: Remove zero values]
    label_list = [label1, label2, label3, label4, label5]
    remove_zero_value_labels(label_list)

    #Set bar data labels [Step 3/3: Set the labels]
    ax.bar_label(p1, labels=label1, label_type='center')
    ax.bar_label(p2, labels=label2, label_type='center')
    ax.bar_label(p3, labels=label3, label_type='center')
    ax.bar_label(p4, labels=label4, label_type='center')
    ax.bar_label(p5, labels=label5, label_type='center')

    #Set tick styles
    ax.tick_params(which='major', length=8, width=2)
    ax.tick_params(which='minor', length=6, width=2)

    #Generate legend
    ax.legend()

    #Generate graph
    plt.savefig(output_file_name, bbox_inches='tight', pad_inches = 0.1)

def bar_graph_stacked_percent(input_data, input_labels, percent_label, x_labels, y_label, y_max, output_file_name):
    #Set font
    set_default_font()

    #Generate graph and bars
    fig, ax = plt.subplots(figsize=(10,8))
    width = 0.5
    p1 = ax.bar(x_labels, input_data[0], width, label=input_labels[0], color='tab:blue')
    p2 = ax.bar(x_labels, input_data[1], width, bottom=input_data[0], label=input_labels[1], color='tab:red')

    #Set axis labels
    ax.set_ylabel(y_label[0], fontsize=36, labelpad=24, weight='bold')

    #Set axis ranges and labels
    ax.set_ylim(0, y_max+1)
    ax.yaxis.set_major_locator(MultipleLocator(2))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))

    #Set bar data labels
    ax.bar_label(p1, label_type='center')
    ax.bar_label(p2, label_type='center')
    ax.bar_label(p2, labels=percent_label, padding=20)

    #Set tick styles
    ax.tick_params(which='major', length=8, width=2)
    ax.tick_params(which='minor', length=6, width=2)

    #Set axis linewidth
    set_axes_linewidth()

    #Generate legend
    ax.legend()

    #Generate graph
    plt.savefig(output_file_name, bbox_inches='tight', pad_inches = 0.1)

def calculate_x_axis_label_pos(number_of_items):
    start = 0
    stop = (number_of_items-1)*0.5
    array = np.linspace(start, stop, number_of_items)
    return array

def convert_list_of_int_to_str(input_list):
    list_str = [str(input_list[x]) for x in range(len(input_list))]
    return list_str

def remove_zero_value_labels(input_lists):
    for x in range(len(input_lists)):
        for y in range(len(input_lists[x])):
            if input_lists[x][y] == '0':
                input_lists[x][y] = ''

def set_default_font():
    mpl.rcParams['font.size'] = 24
    mpl.rcParams['font.family'] = 'sans-serif'
    mpl.rcParams['font.sans-serif'] = ['Tahoma']
    mpl.rcParams['font.weight'] = 'bold'

def set_axes_linewidth():
    mpl.rcParams['axes.linewidth'] = 2


#-------------------------------------------------------------------------------
# Basic Bar Graph With Error Bars - Sample
#-------------------------------------------------------------------------------

#Data and labels
labels = ['A', 'B', 'C', 'D']
data = [10, 5, 13, 8]
stdev = [3, 1.5, 4, 2]

#Axis labels and ranges
xy_axis_labels = ['Category', 'Number']
y_max = 25

#Set output filename
file_name = 'output_bar_graph.png'

#Generate bar graph
bar_graph_basic(data, stdev, labels, xy_axis_labels, y_max, file_name)


#-------------------------------------------------------------------------------
# Bar Graph with Multiple Bars Per Category - Sample
#-------------------------------------------------------------------------------

#Data and Labels
bar_labels = ['Type A', 'Type B', 'Type C', 'Type D']
data = [[1, 2, 3],[5, 1, 8],[3, 3, 3],[9, 4, 2]]

#Axis labels and ranges
x_axis_labels = ['Yes', 'No', 'Maybe']
y_axis_label = ['Number']
y_max = 10

#Output filename
file_name = 'output_bar_graph_multi.png'

#Generate bar graph
bar_graph_multi(data, bar_labels, x_axis_labels, y_axis_label, y_max, file_name)


#-------------------------------------------------------------------------------
# Stacked Bar Graph - Sample
#-------------------------------------------------------------------------------

#Data and Labels
group_labels = ['Area 1', 'Area 2', 'Area 3', 'Area 4', 'Area 5']
data = [[5, 1, 4],[3, 0, 1],[4, 0, 0],[2, 1, 3],[3, 10, 2]]

#Axis labels and ranges
x_labels = ['Team 1', 'Team 2', 'Team 3']
y_label = ['Count']
y_max = 20

#Set output file name
file_name = 'output_bar_graph_stacked.png'

#Generate bar graph
bar_graph_stacked(data, group_labels, x_labels, y_label, y_max, file_name)


#-------------------------------------------------------------------------------
# Stacked Bar Graph With Percent - Sample
#-------------------------------------------------------------------------------

#Define data
labels = ['Positive', 'Negative']
data = [[5, 4, 9],[5, 6, 1]]
percent_label = ['50%', '40%', '90%']

#Axis labels and ranges
x_labels = ['Subject A', 'Subject B', 'Subject C']
y_label = ['Answers (Count)']
y_max = 14

#Set output file name
file_name = 'output_bar_graph_stacked.png'

#Generage graph
bar_graph_stacked_percent(data, labels, percent_label, x_labels, y_label, y_max, file_name)