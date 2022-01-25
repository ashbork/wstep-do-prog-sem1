import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
import pandas as pd
from datetime import datetime
import matplotlib.dates

with open("artists.csv", newline='') as f:
    artists = pd.read_csv(f).head(10).to_dict()

with open("wyniki-pm.csv", newline='') as f:
    pm_dataframe = pd.read_csv(f, sep=";")
    temp = pm_dataframe.to_dict()
    print(len(temp))
    pm_over_time = {temp['PM2.5 [µg/m3]'][i]: datetime.strptime(temp['Datetime'][i], "%Y-%m-%d %H:%M")
                    for i in range(len(temp['Datetime'].items()))}

    pm = pm_dataframe.sort_values(
        ['PM2.5 [µg/m3]']).to_dict()['PM2.5 [µg/m3]'].values()
    pm = [float(x) for x in pm]

with open("polska_nierownosci.csv") as f:
    topten = pd.read_csv(f, sep=";").to_dict()
    years = list(topten['rok'].values())
    percents = list(topten['procent'].values())

cmap = plt.get_cmap('Purples')
colors = [cmap(i) for i in range(240, 40, -20)]
fig, axs = plt.subplots(2, 2, figsize=(18, 20))

axs[0, 0].pie(list(artists['count'].values()),
              autopct='%1.1f%%', colors=colors)
axs[0, 0].set_title("Top 10 artists by plays")
axs[0, 0].legend(list(artists['artist_name'].values()),
                 bbox_to_anchor=(1.05, 0.6))

axs[0, 1].plot(years, percents)
axs[0, 1].set_title("Income inequality in Poland")
axs[0, 1].set_xlabel("Time")
axs[0, 1].set_ylabel("Income share of top 10%")

axs[1, 0].set_title("Air pollution in Wrocław (2018-2019)")
axs[1, 0].hist(pm, bins=20, linewidth=0.5, edgecolor='black')
axs[1, 0].set_xlabel("Air pollution (PM2.5 [µg/m3])")
axs[1, 0].set_ylabel("Occurences")

axs[1, 1].set_title("Air pollution in Wrocław over time")
axs[1, 1].scatter(pm_over_time.values(), pm_over_time.keys(), alpha=0.5)
axs[1, 1].set_xlabel("Time")
axs[1, 1].set_ylabel("Air pollution (PM2.5 [µg/m3])")

plt.show()
