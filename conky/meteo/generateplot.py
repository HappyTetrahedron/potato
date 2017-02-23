#!/usr/bin/env python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json
import itertools
import datetime as dt
from matplotlib import ticker

# create a time format string from an unix timestamp
def format_time(time, pos=None):
    return dt.datetime.fromtimestamp(time).strftime('%H:%M')

# open file in which the JSON has been stored, load json
f = open("/home/alinea/conkystuff/meteo/weather")
j = json.load(f)
f.close()

# Extract the temperatures, precipitations and timestamps for the first two days in the json file.
temps = [ row[1]           for k in [0,1] for row in j[k].get("temperature") ]
precs = [ row[1]           for k in [0,1] for row in j[k].get("rainfall")    ]
times = [ int(row[0]/1000) for k in [0,1] for row in j[k].get("temperature") ]

# current time as reported by json, in seconds
now = j[0].get("current_time") / 1000

# timespan to display
starttime = now - 3600
endtime = now + 24 * 3600

# filter the temps, precs and times array such that only values within the timespan are included
indices = [ starttime < x and x < endtime for x in times ]
temps = list(itertools.compress(temps, indices))
precs = list(itertools.compress(precs, indices))
times = list(itertools.compress(times, indices))

# where ticks on the x axis should go
xticks = times[2::3] 

# max and min temperature, for adjusting the y axis range
maxtemp = max(temps)
mintemp = min(temps)

# Set up plot
fig, ax1 = plt.subplots(figsize=(6,3))
for tl in ax1.get_xticklabels():
    tl.set_color('w') # set all x tick labels to white
ax1.xaxis.set_major_formatter(ticker.FuncFormatter(format_time)) # make the x axis convert unix timestamps to time strings
ax1.xaxis.set_ticks(xticks) # set tick interval according to our xticks list

# Plot precipitation
ax1.bar([x-1750 for x in times], precs, 3500, color='#aaaaff')
ax1.set_ylim([0,8]) # y axis range hardcoded to 0-8, that's usually fine
ax1.set_facecolor('k') 

# Set all y tick labels to white (for the precipitation values)
for tl in ax1.get_yticklabels():
    tl.set_color('w')

# Add new y axis and plot temperature
ax2 = ax1.twinx()
ax2.plot(times, temps, 'w',  linewidth=3)
ax2.set_ylim([mintemp - 2, maxtemp + 2])  # y axis range
ax2.vlines(now, mintemp - 2, maxtemp + 1, colors='w', linestyles='dotted') # vertical line where the current time is

# set temperature y tick labels to white
for tl in ax2.get_yticklabels():
    tl.set_color('w')

# save figure to file
fig.savefig('/home/alinea/conkystuff/meteo/weather.png', facecolor='k', edgecolor='none', transparent=True, bbox_inches='tight', dpi=100)
