import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import AutoMinorLocator
import pandas as pd
import math
import numpy as np

"""
Customizaton instructions:
https://matplotlib.org/stable/tutorials/introductory/customizing.html

Colors:
https://matplotlib.org/stable/gallery/color/named_colors.html

#print(fig.canvas.get_supported_filetypes())
"""


#-------------------------------------------------------------------------------
#PART 1: Data import
#-------------------------------------------------------------------------------

#dataframe1 = pd.read_csv('linegraph_input_file.csv')
#print(dataframe1)


labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
year_2019 = [216, 166, 127, 87, 73, 156, 231, 317, 143, 141, 81, 126]
year_2020 = [164, 222, 175, 142, 189, 263, 292, 298, 301, 177, 112, 269]
year_2021 = [344, 206, 171, 161, 161, 166, 358, 292, 312, 202, 165, 189]


#-------------------------------------------------------------------------------
#PART 2: Graph output
#-------------------------------------------------------------------------------

#Global style parameters
#mpl.rcParams['lines.linewidth'] = 10
mpl.rcParams['font.size'] = 24
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['Tahoma']
#mpl.rcParams['axes.linewidth'] = 1.5

#Label locations and bar width
x = (np.arange(len(labels)))*2
print(x)
width = 0.55

#Generate figure object, axes object(s), and set size
fig, ax = plt.subplots(figsize=(12,10))

#Generate each individual axis object
series1 = ax.bar(
    x - width,
    year_2019,
    width,
    label='2019',
    color='dodgerblue'
    )
series2 = ax.bar(
    x,
    year_2020,
    width,
    label='2020',
    color='forestgreen'
    )
series3 = ax.bar(
    x + width,
    year_2021,
    width,
    label='2021',
    color='salmon'
    )

#Set axis labels
ax.set_ylabel(
    "Usage (kWh)",
    fontsize=28,
    labelpad=12
    )

#Activate bar data labels
ax.bar_label(series1, padding=3, fontsize=9, fontweight='bold')
ax.bar_label(series2, padding=3, fontsize=9, fontweight='bold')
ax.bar_label(series3, padding=3, fontsize=9, fontweight='bold')

#Set axis ranges
ax.set_xticks(x, labels)
ax.yaxis.set_minor_locator(
    AutoMinorLocator(2)
    )

#Set tick styles
ax.tick_params(
    which='major',
    length=8,
    width=2
    )
ax.tick_params(
    which='minor',
    length=6,
    width=2
    )

#Set spines
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)

#Set title and legend
fig.suptitle(
    'Electricity Usage (kWh)',
    fontsize=32
    )
ax.legend(
    loc='lower center',
    ncol=3,
    bbox_to_anchor=(0.5,-0.15),
    fontsize=18,
    markerscale=1.5
    )

"""
#Display and save figure to disk
fig.savefig(
    'test.png',
    transparent=False,
    dpi=80,
    bbox_inches='tight'
)
#plt.show()
print('\nGraph generated successfully')
"""

plt.show()