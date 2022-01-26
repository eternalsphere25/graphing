import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import AutoMinorLocator
import pandas as pd
import math

"""
Customizaton instructions:
https://matplotlib.org/stable/tutorials/introductory/customizing.html
#print(fig.canvas.get_supported_filetypes())
"""

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
    [0, 2, 4],
    [100, 100, 100],
    color='blue',
    label='Device',
    marker='o',
    markersize=16
)
ax.plot(
    [0, 2, 4],
    [100, 100, 100],
    color='red',
    label='Patch',
    marker='s',
    markersize=16
)

#Set axis labels
ax.set_ylabel(
    "% of Initial Value",
    fontsize=44,
    labelpad=28
)
ax.set_xlabel(
    "t (Weeks)",
    fontsize=44,
    labelpad=16
)

#Set axis ranges
ax.set_xticks(
    range(0, 5, 2)
)
ax.set_yticks(
    range(80, 121, 10)
)
ax.xaxis.set_minor_locator(
    AutoMinorLocator(2)
)
ax.yaxis.set_minor_locator(
    AutoMinorLocator(2)
)

#Set tick styles
ax.tick_params(
    which='major',
    length=8,
    width=3
)
ax.tick_params(
    which='minor',
    length=6,
    width=3
)

#Set spines
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
ax.spines['top'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)

#Set title and legend
fig.suptitle(
    'TEWL (Eyes)',
    fontsize=48,
    y=1.05
)
ax.legend(
    loc='lower center',
    ncol=2,
    bbox_to_anchor=(0.5,-0.45),
    fontsize=36,
    markerscale=1.5
)

#Display and save figure to disk
fig.savefig(
    'test.png',
    transparent=False,
    dpi=80,
    bbox_inches='tight'
)
#plt.show()
print('\nGraph generated successfully')