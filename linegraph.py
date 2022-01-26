import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import AutoMinorLocator
import pandas as pd
import csv

"""
Customizaton instructions:
https://matplotlib.org/stable/tutorials/introductory/customizing.html
#print(fig.canvas.get_supported_filetypes())
"""

def setOutputFilename(name, extension):
    value = name[0] + '.' + extension[0]
    return value

def removeEmptyValuesFromList(input_list):
    while ("" in input_list):
        input_list.remove("")


#-------------------------------------------------------------------------------
#PART 0: Define global variables
#-------------------------------------------------------------------------------

input_file = 'inegraph_input_file.csv'
char_enc = ['utf-8']


#-------------------------------------------------------------------------------
#PART 1: Import graph settings from csv file and clean data
#-------------------------------------------------------------------------------

#Import graph properties with CSV
with open(input_file) as csv_file:
    reader = csv.reader(csv_file)

    #First skip the formatting instruction rows
    for skip in range(23):
        next(reader)
    
    #Import filename, file format, figure title, and x/y axes titles
    file_name = next(reader)
    file_ext = next(reader)
    graph_title = next(reader)
    x_axis_title = next(reader)
    y_axis_title = next(reader)
    next(reader)

    #Import data trace parameters
    data_num = next(reader)
    data_labels = next(reader)
    data_colors = next(reader)
    data_markers = next(reader)
    next(reader)

    #Import x/y axis ranges
    next(reader)
    x_axis_range = next(reader)
    next(reader)
    y_axis_range = next(reader)

#Import graph data with Pandas
dataframe1 = pd.read_csv(input_file, skiprows=39, encoding=char_enc[0])

#Clean inputs (remove empty values)
removeEmptyValuesFromList(file_name)
removeEmptyValuesFromList(file_ext)
removeEmptyValuesFromList(graph_title)
removeEmptyValuesFromList(x_axis_title)
removeEmptyValuesFromList(y_axis_title)
removeEmptyValuesFromList(data_num)
removeEmptyValuesFromList(data_labels)
removeEmptyValuesFromList(data_colors)
removeEmptyValuesFromList(data_markers)
removeEmptyValuesFromList(x_axis_range)
removeEmptyValuesFromList(y_axis_range)
dataframe1 = dataframe1.dropna(axis=1, how='all')

#Clean inputs (convert str to int)
x_axis_range = list(map(int, x_axis_range))
y_axis_range = list(map(int, y_axis_range))

"""
print('\nInput Verification\n')
print(file_name[0])
print(file_ext[0])
print(graph_title[0])
print(x_axis_title[0])
print(y_axis_title[0])
print('')
print(data_num)
print(data_labels)
print(data_colors)
print(data_markers)
print('')
print(x_axis_range)
print(y_axis_range)
print('')
print(dataframe1)
"""


#-------------------------------------------------------------------------------
#PART 2: Process inputs for graphing
#-------------------------------------------------------------------------------

#Set output file name
output_filename = setOutputFilename(file_name, file_ext)

#Increment axes end values for proper display
x_axis_range[1] += 1
y_axis_range[1] += 1

#Convert dataframe columns to list
x_data = dataframe1['x_axis'].tolist()
y1_data = dataframe1['y_axis1'].tolist()
y2_data = dataframe1['y_axis2'].tolist()


#-------------------------------------------------------------------------------
#PART 3: Set graph properties
#-------------------------------------------------------------------------------

#Global style parameters
mpl.rcParams['lines.linewidth'] = 10
mpl.rcParams['font.size'] = 40
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['Tahoma']
mpl.rcParams['axes.linewidth'] = 1.5

#Generate figure object, axes object(s), and set size
fig, ax = plt.subplots(figsize=(10,8))

#Generate each individual axis object
ax.plot(
    x_data,
    y1_data,
    color=data_colors[0],
    label=data_labels[0],
    marker=data_markers[0],
    markersize=16
)
ax.plot(
    x_data,
    y2_data,
    color=data_colors[1],
    label=data_labels[1],
    marker=data_markers[1],
    markersize=16
)

#Set axis labels
ax.set_ylabel(y_axis_title[0], fontsize=44, labelpad=28)
ax.set_xlabel(x_axis_title[0], fontsize=44, labelpad=16)

#Set axis ranges
ax.set_xticks(range(x_axis_range[0], x_axis_range[1], x_axis_range[2]))
ax.set_yticks(range(y_axis_range[0], y_axis_range[1], y_axis_range[2]))
ax.xaxis.set_minor_locator(AutoMinorLocator(2))
ax.yaxis.set_minor_locator(AutoMinorLocator(2))

#Set tick styles
ax.tick_params(which='major', length=8, width=3)
ax.tick_params(which='minor', length=6, width=3)

#Set spines
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
ax.spines['top'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)

#Set title and legend
fig.suptitle(graph_title[0], fontsize=48, y=1.05)
ax.legend(
    loc='lower center',
    ncol=2,
    bbox_to_anchor=(0.5,-0.45),
    fontsize=36,
    markerscale=1.5
)

#Display and save figure to disk
fig.savefig(
    output_filename,
    transparent=False,
    dpi=80,
    bbox_inches='tight'
)
#plt.show()
print('\nGraph generated successfully')