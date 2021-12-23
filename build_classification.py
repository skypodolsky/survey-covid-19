#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#  basic_classification = [
#              "Законодавці, вищі державні службовці, керівники, менеджери (управителі)",
#              "Професіонали",
#              "Фахівці",
#              "Технічні службовці",
#              "Працівники сфери торгівлі та послуг",
#              "Кваліфіковані робітники сільського та лісового господарств, риборозведення та рибальства",
#              "Кваліфіковані робітники з інструментом",
#              "Робітники з обслуговування, експлуатації та контролювання за роботою технологічного устаткування, складання устаткування та машин",
#              "Найпростіші професії",
#              "Незайняті (пенсіонери, безробітні, декрет)",
#              "Незайняті (школярі, студенти)"
#          ]

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
    #  print(df)
    #  fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize=(10,10))

    counts_series = df['basic_classification'].value_counts()
    counts_sum = counts_series.sum()
    labels = counts_series.index.tolist()
    counts = counts_series.values
    percents = counts / counts_sum * 100

    #  print(counts_sum)
    #  print(labels)
    #  print(counts)

    res = zip(labels, percents)

    fin_labels = []
    for i,j in res:
        e_num = 50
        templ = '{' + ': <{}'.format(e_num) + '} - {:.2f} %'
        st = templ.format(i, j)
        fin_labels.append(st)

    explode = np.full(len(fin_labels), 0.03)

    plot = df['basic_classification'].value_counts().plot.pie(autopct='%.1f%%', startangle=0, fontsize=10, pctdistance=0.6, explode=explode, labels=fin_labels)
    plot.set_xlabel('Офіційна класифікація (' + name + ')',fontsize = 10)
    plot.set_ylabel('', fontsize = 10)
    #plot.legend(loc='upper right', frameon=True)
    #plot.legend(loc=' ', fancybox=True, framealpha=1, shadow=True, borderpad=1)
    plot.legend(loc='upper left', bbox_to_anchor=(1, 1.05),
          ncol=1, fancybox=True, shadow=True)

    plt.tight_layout()
    plt.show()
    #  plot = df['modified_classification'].value_counts().plot.pie(ax=axes[1], autopct='%.1f%%', startangle=0, fontsize=5)
    #  plot.set_xlabel('Авторська класифікація (' + name + ')',fontsize = 10)
    #  plot.set_ylabel('', fontsize = 10)

    #  plt.show()
    #  fig.savefig('specialities-' + name + '.png', dpi=200)
