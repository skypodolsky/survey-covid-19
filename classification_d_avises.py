#!/usr/bin/env python

import difflib
import pandas as pd

#  1  "Не пройшла медичні випробування або страх ускладнень"
#  2  "Недовіра до влади або системи охорони здоров'я"
#  3  "Обмеження соціальних прав"
#  4  "Конспірологічні причини"
#  5  "Релігійні причини"
#  6  "Дезінформація"
reasons = [
                ( [ "примусовість", "примушення", "примус", "принуждение", "нарушение прав", "порушення прав", "обмеження прав", "ограничение прав", "примушування", "тиск", "насильно" ], 0, "Соціальні" ), # соціальні
                ( [ "експеримент", "евтаназія", "шмурдяк", "барановирус", "лжепанд", "обман", "эксперимент", "геноцид", "смерть", "вбивство", "експеремент", "жижа", "не вакцина" ], 1, "Конспірологічні"), # конспірологічні
                ( [ "випробування", "недостовірність", "недоказанность", "бесполезность", "опасность", "неєффективность", "неефективність", "немає сенсу", "побічні" ], 2, "Дезінформація"), # дезінформація
                ( [ "корупція", "не довіря", "не довіра", "недовіра", "страх", "недоверие", "не доверие", "ложь", "брехн", "врань", "немає довіри", "нет доверия", "фальсификация" ], 3, "Недовіра"), # недовіра
                ( [], 4, "Інші")
              ]

df = pd.read_csv('survey-final-interim.csv', sep='\t')

res = [ ["соц.", 0], ["консп.", 0], ["мед.", 0], ["дов.", 0], [ "тупі", 0] ]

count = 0
print(df)

vax_stats_df = vax_df = df[df['Ви вакциновані:'] == 'Так']
antivax_stats_df = antivax_df = df[df['Ви вакциновані:'] == 'Ні']
print(antivax_stats_df)

for index, row in antivax_stats_df.iterrows():
    value = row['У чому, на вашу думку, основна причина відмови людей від вакцинації?'].lower().strip()

    change = False
    for category in reasons:
        for reason in category[0]:
            if reason in value:
                res[category[1]][1] += 1
                antivax_stats_df.at[index, category[2]] = 1
                count += 1
                change = True

    if change:
        df = df.drop(index=index)
    else:
        antivax_stats_df = antivax_stats_df.drop(index=index)


print(df)
print(res)
print(count)

antivax_stats_df.to_csv('res.csv', sep='\t', index=False)
antivax_stats_df = antivax_df = df[df['Ви вакциновані:'] == 'Ні']
antivax_stats_df.to_csv('res_to_process.csv', sep='\t', index=False)
