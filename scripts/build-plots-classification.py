#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

colors = [ 'blue', 'orange', 'red', 'green', 'purple', 'brown', 'gray', 'pink' ]

basic_classification = [
            "ЗВДСКМ(У)",
            "Професіонали",
            "Фахівці",
            "Технічні службовці",
            "Працівники сфери торгівлі та послуг",
            "КРСЛГРР",
            "Кваліфіковані робітники з інструментом",
            "РОЕКРТУСУМ",
            "Найпростіші професії",
            "Незайняті (пенсіонери, безробітні, декрет)",
            "Незайняті (школярі, студенти)"
        ]


modified_classification = [
            "Спеціальності науково-технічної спрямованості",
            "Спеціальності сфери охорони здоров’я",
            "Спеціальності сфера фінансів",
            "Спеціальності сфери послуг",
            "Спеціальності сфери освіти",
            "Юридичні спеціальності",
            "Керівні спеціальності",
            "Творчі та гуманітарні спеціальності",
            "Сфера обслуговування",
            "Спеціальність невідома",
            "Інші спеціальності",
        ]

df = pd.read_csv('survey-processed.csv', sep='\t')

df.dropna(subset=['category'], inplace=True)

for index, row in df.iterrows():
    value = row['category']
    values = value.split('-')
    basic = basic_classification[int(values[0]) - 1]
    modified = modified_classification[int(values[1]) - 1]
    df.at[index, 'basic_classification'] = basic
    df.at[index, 'modified_classification'] = modified


vax_stats_df = vax_df = df[df['Ви вакциновані:'] == 'Так']
antivax_stats_df = antivax_df = df[df['Ви вакциновані:'] == 'Ні']


df.to_csv('survey-final.csv', sep='\t', index=False)

for df, name in [(vax_stats_df, 'vax'), (antivax_stats_df, 'antivax')]:
    for classification, desc in [ ('basic_classification', 'Розподіл вибірки респондентів за стандартною класифікацією професій'), ('modified_classification', 'Розподіл вибірки респондентів за модифікованою класифікацією професій') ]:

        counts_series = df[classification].value_counts()#.sort_index(ascending=False)
        labels = counts_series.index.tolist()
        counts = counts_series.values.tolist()
        percents = counts / counts_series.sum() * 100
        percents = percents.tolist()

        print(percents)
        print(labels)
        print('===')
        other = 0
        changed = False
        for percent in reversed(percents):
            if percent <= 5:
                changed = True
                other += percent
                print('drop percentage {}'.format(percent))
                #  counts.pop()
                percents.pop()
                labels.pop()

        if changed:
            percents.append(other)
            labels.append('Інші')

        print(percents)
        res = zip(labels, percents)

        fin_labels = []
        for i, j in res:
            fin_labels.append('{:} - {:.2f} %'.format(i, j))

        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

        wedges, texts = ax.pie(percents, colors=colors, wedgeprops=dict(width=0.5), startangle=-40)

        bbox_props = dict(boxstyle="square,pad=0.1", fc="w", ec="k", lw=0.72)
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
                    horizontalalignment=horizontalalignment, **kw, fontsize=11)

        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()

        plt.show()

        if classification == "basic_classification":
            fig.savefig('classification-' + name + '-standard', dpi=200)
        else:
            fig.savefig('classification-' + name + '-modified', dpi=200)
