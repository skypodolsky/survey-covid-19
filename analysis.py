#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('survey-raw.csv', sep='\t')
#  print(df.dropna(axis = 0, how = 'any'))

print(df)

vax_stats_df = vax_df = df[df['Ви вакциновані:'] == 'Так']
antivax_stats_df = antivax_df = df[df['Ви вакциновані:'] == 'Ні']
colors = [ 'blue', 'orange', 'red', 'green', 'purple', 'brown', 'gray', 'pink' ]

#  antivax_stats_df = antivax_stats_df.drop('Timestamp', 1)
#  antivax_stats_df = antivax_stats_df.drop('Коротко про те, ким ви працюєте:', 1)
#  antivax_stats_df = antivax_stats_df.drop('У чому, на вашу думку, основна причина відмови людей від вакцинації?', 1)

cols = [ 'Ваш вік', 'Чи вважаєте Ви COVID-19 небезпечним респіраторним захворюванням?', 'Чи довіряєте Ви уряду щодо кампанії вакцинації від COVID-19?', 'Чи довіряєте Ви сфері медицини, окрім кампанії вакцинації?', 'В цілому, я довіряю новинам:', 'Я вважаю, що усунення від роботи невакцинованих співробітників погіршує ситуацію:', 'Як багато Ваших знайомих вакциновано?', 'Ви готові придбати або вже придбали підроблений сертифікат COVID-19:', 'Крім питання персональної довіри до вакцин, в цілому ви ставитеся до вакцинації від COVID-19:', 'Незалежно від позиції по вакцинації, ви відстоюєте її:', 'Ви часто приєднуєтеся до громадських мітингів на важливі для вас теми:' ]
#cols = [ 'Як ваше рішення щодо вакцинації позначилося на ставленні людей до вас?', 'Як епідемія вплинула на ваших знайомих?' ]

count = 0
for df, name in [(vax_stats_df, 'vax'), (antivax_stats_df, 'antivax')]:

    for col in cols:
        count += 1
        counts_series = df[col].value_counts().sort_index(ascending=False)
        labels = counts_series.index.tolist()
        counts = counts_series.values.tolist()
        percents = counts / counts_series.sum() * 100
        percents = percents.tolist()

        print(percents)
        print(labels)
        print('===')
    
        res = zip(labels, percents)

        fin_labels = []
        for i, j in res:
            fin_labels.append('{:} - {:.2f} %'.format(i, j))

#        fin_labels.sort()
        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

        wedges, texts = ax.pie(percents, colors=colors, wedgeprops=dict(width=0.5), startangle=-40)

        bbox_props = dict(boxstyle="square,pad=0.5", fc="w", ec="k", lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="-"),
                bbox=bbox_props, zorder=0, va="center")

        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            ax.annotate(fin_labels[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw, fontsize=14)

        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()

        plt.show()

        fig.figure.savefig('survey-' + col + '-' + name + '.png', dpi=200)
