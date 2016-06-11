#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import json
import datetime as dt
from matplotlib import ticker

def format_time(time, pos=None):
    return dt.datetime.fromtimestamp(time).strftime('%H:%M')

f = open("/home/alinea/conky/meteo/weather")
j = json.load(f)
f.close()

# get the various data from the json file
temps = [row[1] for row in j.get("temperature")]
precs = [row[1] for row in j.get("rainfall")]
times = [int(row[0]/1000) for row in j.get("temperature")]
now = j.get("current_time") / 1000
xticks = times[2::3] 

maxtemp = max(temps)
mintemp = min(temps)

# layout x axis
fig, ax1 = plt.subplots(figsize=(6,3))
for tl in ax1.get_xticklabels():
    tl.set_color('w')
ax1.xaxis.set_major_formatter(ticker.FuncFormatter(format_time))
ax1.xaxis.set_ticks(xticks)

# plot precipitation
ax1.bar([x-1750 for x in times], precs, 3500, color='#aaaaff')
ax1.set_ylim([0,8])
ax1.set_axis_bgcolor('k')

for tl in ax1.get_yticklabels():
    tl.set_color('w')

# plot temperature
ax2 = ax1.twinx()
ax2.plot(times, temps, 'w',  linewidth=3)
ax2.set_ylim([mintemp - 2, maxtemp + 2])
ax2.vlines(now, mintemp - 2, maxtemp + 1, colors='w', linestyles='dotted')

for tl in ax2.get_yticklabels():
    tl.set_color('w')

# save figure
fig.savefig('/home/alinea/conky/meteo/weather.png', facecolor='k', edgecolor='none', transparent=True, bbox_inches='tight', dpi=100)
