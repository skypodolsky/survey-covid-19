#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('survey-raw.csv', sep='\t')
print(df.dropna(axis = 0, how = 'any'))

print(df)

vax_stats_df = vax_df = df[df['Ви вакциновані:'] == 'Так']
antivax_stats_df = antivax_df = df[df['Ви вакциновані:'] == 'Ні']

antivax_stats_df = antivax_stats_df.drop('Timestamp', 1)
antivax_stats_df = antivax_stats_df.drop('Коротко про те, ким ви працюєте:', 1)
antivax_stats_df = antivax_stats_df.drop('У чому, на вашу думку, основна причина відмови людей від вакцинації?', 1)

#  for df in [vax_stats_df, antivax_stats_df]:
    
fig, axes = plt.subplots(nrows = 4, ncols = 3, figsize=(4,4))

plot = antivax_stats_df['Ваш вік'].value_counts().plot.pie(ax=axes[0, 0], autopct='%.1f%%', startangle=270, fontsize=7)
plot.set_xlabel('Вік респондентів',fontsize = 10)
plot.set_ylabel('', fontsize = 10)
#  plot.legend(frameon=True)

plot = antivax_stats_df['Чи довіряєте Ви сфері медицини, окрім кампанії вакцинації?'].value_counts().plot.pie(ax=axes[0, 1], autopct='%.1f%%', startangle=270, fontsize=7)
plot.set_xlabel('Довіра до медицини (за виключенням кампанії вакцинації)', fontsize = 10)
plot.set_ylabel('', fontsize = 10)

plot = antivax_stats_df['В цілому, я довіряю новинам:'].value_counts().plot.pie(ax=axes[0, 2], autopct='%.1f%%', startangle=270, fontsize=7)
plot.set_xlabel('Довіра до ЗМІ', fontsize = 10)
plot.set_ylabel('', fontsize = 10)

###

plot = antivax_stats_df['Я вважаю, що усунення від роботи невакцинованих співробітників погіршує ситуацію:'].value_counts().plot.pie(ax=axes[1, 0], autopct='%.1f%%', startangle=270, fontsize=7)
plot.set_xlabel('Усунення від роботи невакцинованих співробітників погіршує ситуацію', fontsize = 10)
plot.set_ylabel('', fontsize = 10)

plot = antivax_stats_df['Як багато Ваших знайомих вакциновано?'].value_counts().plot.pie(ax=axes[1, 1], autopct='%.1f%%', startangle=270, fontsize=7)
plot.set_xlabel('Частка вакцинованих знайомих', fontsize = 10)
plot.set_ylabel('', fontsize = 10)

plot = antivax_stats_df['Як ваше рішення щодо вакцинації позначилося на ставленні людей до вас?'].value_counts().plot.pie(ax=axes[1, 2], autopct='%.1f%%', startangle=270, fontsize=7)
plot.set_xlabel('Рішення щодо вакцинації позначилося на респондентах', fontsize = 10)
plot.set_ylabel('', fontsize = 10)

###

plot = antivax_stats_df['Як епідемія вплинула на ваших знайомих?'].value_counts().plot.pie(ax=axes[2, 0], autopct='%.1f%%', startangle=270, fontsize=7)
plot.set_xlabel('Як епідемія вплинула на ваших знайомих?', fontsize = 10)
plot.set_ylabel('', fontsize = 10)

plot = antivax_stats_df['Ви готові придбати або вже придбали підроблений сертифікат COVID-19:'].value_counts().plot.pie(ax=axes[2, 1], autopct='%.1f%%', startangle=270, fontsize=7)
plot.set_xlabel('Чи готові придбати або вже придбали підроблений сертифікат', fontsize = 10)
plot.set_ylabel('', fontsize = 10)

plot = antivax_stats_df['Крім питання персональної довіри до вакцин, в цілому ви ставитеся до вакцинації від COVID-19:'].value_counts().plot.pie(ax=axes[2, 2], autopct='%.1f%%', startangle=270, fontsize=7)
plot.set_xlabel('Ставлення до вакцинації (за виключенням персональної довіри до вакцин)', fontsize = 10)
plot.set_ylabel('', fontsize = 10)

###

plot = antivax_stats_df['Незалежно від позиції по вакцинації, ви відстоюєте її:'].value_counts().plot.pie(ax=axes[3, 0], autopct='%.1f%%', startangle=270, fontsize=7)
plot.set_xlabel('Незалежно від позиції по вакцинації, респонденти відстоюють її',fontsize = 10)
plot.set_ylabel('', fontsize = 10)

plot = antivax_stats_df['Ви часто приєднуєтеся до громадських мітингів на важливі для вас теми:'].value_counts().plot.pie(ax=axes[3, 1], autopct='%.1f%%', startangle=270, fontsize=7)
plot.set_xlabel('Респондент часто приєднується до громадських мітингів на важливі теми',fontsize = 10)
plot.set_ylabel('', fontsize = 10)

#  plot = antivax_stats_df['Ви часто приєднуєтеся до громадських мітингів на важливі для вас теми:'].value_counts().plot.pie(ax=axes[3, 2], autopct='%.1f%%', startangle=270, fontsize=7)
#  plot.set_xlabel('Респондент часто приєднується до громадських мітингів на важливі теми',fontsize = 10)
#  plot.set_ylabel('', fontsize = 10)

### vaxers ###

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()

plt.show()

