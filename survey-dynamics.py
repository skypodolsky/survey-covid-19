#!/usr/bin/env python

import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('survey-raw.csv', sep='\t')

vaxed = 0
not_vaxed = 0
for index, row in df.iterrows():
    if df.at[index, 'Ви вакциновані:'] == 'Так':
        vaxed += 1
        df.at[index, 'vax_vote_num'] = vaxed
        df.at[index, 'not_vax_vote_num'] = not_vaxed
    else:
        not_vaxed += 1
        df.at[index, 'vax_vote_num'] = vaxed
        df.at[index, 'not_vax_vote_num'] = not_vaxed

df['Timestamp']= pd.to_datetime(df['Timestamp'])

print(df)

print(vaxed)
print(not_vaxed)

vax_stats_df = vax_df = df[df['Ви вакциновані:'] == 'Так']
antivax_stats_df = antivax_df = df[df['Ви вакциновані:'] == 'Ні']

plot = df.plot.area(x='Timestamp', y=['vax_vote_num', 'not_vax_vote_num'], label=['Вакциновані респонденти', 'Невакциновані респонденти'], stacked=False)

# annotations
date_time_str = '12-07-2021 22:30:00'
dt = datetime.datetime.strptime(date_time_str, '%m-%d-%Y %H:%M:%S')
plt.annotate('Агітація серед антивакцинаторів', xy=(dt, 50), xytext=(dt, 150), horizontalalignment="left", arrowprops=dict(arrowstyle='->',lw=1))

date_time_str = '12-12-2021 20:23:00'
dt = datetime.datetime.strptime(date_time_str, '%m-%d-%Y %H:%M:%S')
plt.annotate('Початок загальної агітації', xy=(dt, 120), xytext=(dt, 220), horizontalalignment="center", arrowprops=dict(arrowstyle='->',lw=1))

date_time_str = '12-19-2021 20:00:00'
dt = datetime.datetime.strptime(date_time_str, '%m-%d-%Y %H:%M:%S')
plt.annotate('Реклама для широкого загалу', xy=(dt, 400), xytext=(dt, 500), horizontalalignment="center", arrowprops=dict(arrowstyle='->',lw=1))

plt.grid(True)

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()

plt.show()
plot.figure.savefig('survey-dynamics-.png', dpi=200) 
