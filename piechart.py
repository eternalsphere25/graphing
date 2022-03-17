#-------------------------------------------------------------------------------
# This file contains presets for different types of pie charts
# Contents are pretty much boilerplate code; either cut and paste or import this
#   file into your driver file
#-------------------------------------------------------------------------------

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os


def calculate_percent(percent, values):
    absolute = int(np.round(percent/100.*np.sum(values)))
    return "{:.1f}%\n({:d})".format(percent, absolute)

def pie_chart_basic(input_labels, input_data, output_file_name):
    #Set font
    set_default_font()

    #Generate pie chart and slices
    fig, ax = plt.subplots(figsize=(10,8))
    wedges, texts,autotexts = ax.pie(input_data, autopct=lambda percent:calculate_percent(percent, input_data), textprops=dict(color="w"), startangle=90)

    #Generate legend
    ax.legend(wedges, input_labels, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    #Save chart to file
    plt.savefig(output_file_name, bbox_inches='tight', pad_inches = 0.1)
    print('Pie chart generated successfully')
    print('\nPie chart saved to the following directory:')
    print(os.getcwd() + '\\' + output_file_name)

def pie_chart_3x3(input_labels1, input_labels2, input_labels3, input_data1, input_data2, input_data3, output_file_name):
    #Set font
    set_default_font()

    #Set pie slice colors
    colors = plt.get_cmap('coolwarm')(np.linspace(0.1, 0.9, len(input_data1[0])))

    #Generate pie charts and slices
    fig, ((ax1, ax2, ax3),(ax4, ax5, ax6),(ax7, ax8, ax9)) = plt.subplots(3, 3, figsize=(30,25))

    #Row 1
    wedges, texts, autotexts = ax1.pie(input_data1[0], autopct=lambda percent:calculate_percent(percent, input_data1[0]), textprops=dict(color="w"), startangle=90, colors=colors)
    ax1.legend(wedges, input_labels1[0], loc='lower center', bbox_to_anchor=(0.5, -0.2))
    wedges, texts, autotexts = ax2.pie(input_data1[1], autopct=lambda percent:calculate_percent(percent, input_data1[1]), textprops=dict(color="w"), startangle=90, colors=colors)
    ax2.legend(wedges, input_labels1[1], loc='lower center', bbox_to_anchor=(0.5, -0.2))
    wedges, texts, autotexts = ax3.pie(input_data1[2], autopct=lambda percent:calculate_percent(percent, input_data1[2]), textprops=dict(color="w"), startangle=90, colors=colors)
    ax3.legend(wedges, input_labels1[2], loc='lower center', bbox_to_anchor=(0.5, -0.2))

    #Row 2
    wedges, texts, autotexts = ax4.pie(input_data2[0], autopct=lambda percent:calculate_percent(percent, input_data2[0]), textprops=dict(color="w"), startangle=90, colors=colors)
    ax4.legend(wedges, input_labels2[0], loc='lower center', bbox_to_anchor=(0.5, -0.2))
    wedges, texts, autotexts = ax5.pie(input_data2[1], autopct=lambda percent:calculate_percent(percent, input_data2[1]), textprops=dict(color="w"), startangle=90, colors=colors)
    ax5.legend(wedges, input_labels2[1], loc='lower center', bbox_to_anchor=(0.5, -0.2))
    wedges, texts, autotexts = ax6.pie(input_data2[2], autopct=lambda percent:calculate_percent(percent, input_data2[2]), textprops=dict(color="w"), startangle=90, colors=colors)
    ax6.legend(wedges, input_labels2[2], loc='lower center', bbox_to_anchor=(0.5, -0.2))

    #Row 3
    wedges, texts, autotexts = ax7.pie(input_data3[0], autopct=lambda percent:calculate_percent(percent, input_data3[0]), textprops=dict(color="w"), startangle=90, colors=colors)
    ax7.legend(wedges, input_labels3[0], loc='lower center', bbox_to_anchor=(0.5, -0.2))
    wedges, texts, autotexts = ax8.pie(input_data3[1], autopct=lambda percent:calculate_percent(percent, input_data3[1]), textprops=dict(color="w"), startangle=90, colors=colors)
    ax8.legend(wedges, input_labels3[1], loc='lower center', bbox_to_anchor=(0.5, -0.2))
    wedges, texts, autotexts = ax9.pie(input_data3[2], autopct=lambda percent:calculate_percent(percent, input_data3[2]), textprops=dict(color="w"), startangle=90, colors=colors)
    ax9.legend(wedges, input_labels3[2], loc='lower center', bbox_to_anchor=(0.5, -0.2))

    plt.savefig(output_file_name, bbox_inches='tight', pad_inches = 0.1)
    print('Pie chart generated successfully')
    print('\nPie chart saved to the following directory:')
    print(os.getcwd() + '\\' + output_file_name)

def set_default_font():
    mpl.rcParams['font.size'] = 28
    mpl.rcParams['font.family'] = 'sans-serif'
    mpl.rcParams['font.sans-serif'] = ['Tahoma']
    mpl.rcParams['font.weight'] = 'bold'


#-------------------------------------------------------------------------------
# Basic Pie Chart - Sample Code
#-------------------------------------------------------------------------------

print('\nGraphing data as a pie chart...')

#Data and labels
sample_labels = ['Yes', 'No']
sample_data = [70, 30]

#Set output filename
file_name = 'output_pie_chart.png'

#Generate pie chart
pie_chart_basic(sample_labels, sample_data, file_name)


#-------------------------------------------------------------------------------
# Multi-Row Pie Chart - Sample Code
#-------------------------------------------------------------------------------

print('\nGraphing data as a 3x3 pie chart...')

#Row 1 (data from left to right)
labels1 = [['Person A', 'Person B'],['Place A', 'Place B'],['Item A', 'Item B']]
data1 = [[18, 4],[7, 4],[10, 1]]

#Row 2 (data from left to right)
labels2 = [['Person A', 'Person B'],['Place A', 'Place B'],['Item A', 'Item B']]
data2 = [[20, 2],[9, 21],[6, 2]]

#Row 3 (data from left to right)
labels3 = [['Person A', 'Person B'],['Place A', 'Place B'],['Item A', 'Item B']]
data3 = [[2, 1],[10, 3],[6, 3]]

#Set output filename
file_name = 'output_pie_chart_3x3.png'

#Generate pie chart
pie_chart_3x3(labels1, labels2, labels3, data1, data2, data3, file_name)