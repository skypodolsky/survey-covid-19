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
                ( [ "примусовість", "примушення", "примус" ], 0 ),
                ( [ "експеримент", "евтаназія" ], 1),
                ( [ "випробування" ], 2),
                ( [ "корупція", "не довіря", "не довіра", "недовіра", "страх" ], 3),
                ( [ "тупі", "дурні", "необізн", "критичн", "неосвіч" ], 4 )
              ]

df = pd.read_csv('survey-final-interim.csv', sep='\t')

res = [ ["соц.", 0], ["консп.", 0], ["мед.", 0], ["дов.", 0], [ "тупі", 0] ]

count = 0

for index, row in df.iterrows():
    value = row['У чому, на вашу думку, основна причина відмови людей від вакцинації?'].lower().strip()

    for category in reasons:
        for reason in category[0]:
            if reason in value:
                res[category[1]][1] += 1
                count += 1

print(res)
print(count)

#  df.to_csv('res.csv', sep='\t', index=False)