from sqlite3 import Timestamp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import dates as mpl_dates
import matplotlib.dates as mdates

#loading the data


data = pd.read_csv("export_final.csv", sep=";")
datum = data['timestamp']
download_bandwidth = data['download_bandwidth']
download_bandwidth_normalized = []
for i in download_bandwidth:
    download_bandwidth_normalized.append(i/154/1000)


plt.plot(datum, download_bandwidth_normalized, linestyle = 'solid')

plt.gcf().autofmt_xdate()

dtFmt = mdates.DateFormatter('%Y-%b') # define the formatting
plt.gca().xaxis.set_major_formatter(dtFmt) 

plt.xticks(rotation=25, fontsize="x-small", color="black", weight="normal", fontfamily="sans-serif")
#plt.tight_layout()

plt.show()

