#!/usr/bin/env python

import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('survey-processed-with-antivax-feedbacks-analyzed.csv', sep='\t')

df = df[df['Ви вакциновані:'] == 'Ні']

lst = [ df['Соціальні'].value_counts().values[0], df['Конспірологічні'].value_counts().values[0],
        df['Недовіра'].value_counts().values[0], df['Дезінформація'].value_counts().values[0] ]
labels = [ 'Соціальні', 'Конспірологічні', 'Недовіра', 'Дезінформація' ]
percents = lst / sum(lst) * 100

labels = labels

print(lst)
print(labels)
print(percents)

explode = (0, 0.1, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(lst, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 14})
ax1.axis('equal')

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()

plt.show()

fig1.savefig('survey-antivax-feedbacks.png', dpi=200) 
