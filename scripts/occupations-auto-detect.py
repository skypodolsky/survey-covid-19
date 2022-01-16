#!/usr/bin/env python

import difflib
import pandas as pd

#  1 ЗАКОНОДАВЦІ, ВИЩІ ДЕРЖАВНІ СЛУЖБОВЦІ, КЕРІВНИКИ,
#  МЕНЕДЖЕРИ (УПРАВИТЕЛІ)
#  2 ПРОФЕСІОНАЛИ
#  3 ФАХІВЦІ
#  4 ТЕХНІЧНІ СЛУЖБОВЦІ
#  5 ПРАЦІВНИКИ СФЕРИ ТОРГІВЛІ ТА ПОСЛУГ
#  6 КВАЛІФІКОВАНІ РОБІТНИКИ СІЛЬСЬКОГО ТА ЛІСОВОГО
#  ГОСПОДАРСТВ, РИБОРОЗВЕДЕННЯ ТА РИБАЛЬСТВА
#  7 КВАЛІФІКОВАНІ РОБІТНИКИ З ІНСТРУМЕНТОМ
#  8 РОБІТНИКИ З ОБСЛУГОВУВАННЯ, ЕКСПЛУАТАЦІЇ ТА
#  КОНТРОЛЮВАННЯ ЗА РОБОТОЮ ТЕХНОЛОГІЧНОГО
#  УСТАТКУВАННЯ, СКЛАДАННЯ УСТАТКУВАННЯ ТА МАШИН
#  9 НАЙПРОСТІШІ ПРОФЕСІЇ
#  10 НЕЗАЙНЯТІ (ПЕНСІОНЕРИ, БЕЗРОБІТНІ, ДЕКРЕТ)
#  11 НЕЗАЙНЯТІ (ШКОЛЯРІ, СТУДЕНТИ)

specialities = [
		( 'лікар',          'врач', 2, 2 ),
		( 'програміст',     'программист', 2, 1 ), 
                ( 'прибиральник',   'уборщик', 9, 9),
                ( 'юрист',          'юрист', 2, 6 ),
                ( 'вчитель',        'учитель', 2, 5 ),
                ( 'викладач',       'преподаватель', 2, 5 ),
                ( 'менеджер',       'менеджер', 1, 7 ),
                ( 'фельдшер',       'фельдшер', 3, 2 ),
                ( 'дизайнер',       'дизайнер', 2, 8 ),
                ( 'фрілансер',      'фрилансер', 3, 10 ),
                ( 'домогосподарка', 'домохозяйка', 10, 10 ),
                ( 'аналітик',       'аналитик', 2, 1 ),
                ( 'дослідник',      'исследователь', 2, 1 ),
                ( 'тестувальник',   'тестировщик', 2, 1 ),
                ( 'продавець',      'продавец', 5, 4 ),
                ( 'будівельник',    'строитель', 7, 1 ),
                ( 'журналіст',      'журналист', 2, 8 ),
                ( 'торгівельник',   'торговец', 5, 4 ),
                ( 'пенсіонер',      'пенсионер', 10, 10 ),
                ( 'інженер',        'инженер', 2, 1 ),
                ( 'різноробочий',   'разнорабочий', 9, 9 ),
                ( 'підприємець',    'предприниматель', 1, 7 ),
                ( 'бухгалтер',      'бухгалтер', 3, 3 ),
                ( 'психолог',       'психолог', 2, 2 ),
                ( 'спортсмен',      'спортсмен', 3, 11 ),
                ( 'економіст',      'экономист', 3, 3 ),
                ( 'приватний підприємець', 'частный предприниматель', 1, 7 ),
                ( 'водій',          'водитель', 8, 4 ),
                ( 'студент',        'студент', 11, 10 ),
                ( 'фінанси',        'финансы', 2, 3 ),
                ( 'школяр',         'школьник', 11, 10 ),
                ( 'декрет',         'декрет', 10, 10 ),
                ( 'мама',           'мама', 10, 10 ),
                ( 'декретна відпустка', 'декретный отпуск', 10, 10 ),
                ( 'лікар-інтерн',   'врач-интерн', 3, 2 ),
                ( 'безробітна',     'безработная', 10, 10 ),
                ( 'мама в декреті', 'мама в декрете', 10, 10 ),
                ( 'адміністратор',  'администратор', 1, 7 ),
                ( 'координатор', 'координатор', 3, 7 ),
                ( 'it',             'ит', 2, 1 ),
                ( 'іт',             'ит', 2, 1 ),
                ( 'qa',             'qa', 2, 1 ),
                ( 'контент-менеджер', 'контент-менеджер', 5, 8 ),
                ( 'відпустка',      'отпуск', 10, 10 ),
                ( 'маркетолог',     'маркетолог', 2, 4 ),
                ( 'лікар-інтерн',   'врач-интерн', 3, 2 ),
                ( 'ріелтер',        'риелтор', 3, 4 ),
                ( 'провізор-інтерн', 'провизор-интерн', 3, 2 ),
                ( 'стоматолог',     'стоматолог', 2, 2 ),
                ( 'фотограф',       'фотограф', 3, 4 ),
                ( 'ФОП',            'ФЛП', 1, 7 ),
                ( 'сфера послуг',   'сфера услуг', 5, 4 ),
                ( 'будівельник',    'строитель', 7, 1 ),
                ( 'hr', 'hr', 3, 11 ),
                ( 'системний адміністратор', 'системный администратор', 2, 1 ),
                ( 'адмін', 'админ', 2, 1 ),
                ( 'головний бухгалтер', 'главный бухгалтер', 1, 3 ),
                ( 'директор', 'директор', 1, 7 ),
                ( 'столяр', 'столяр', 7, 1 ),
                ( 'не працюю', 'не работаю', 10, 10 ),
                ( 'фінансист', 'финансист', 2, 3 ),
                ( 'хімік', 'химик', 2, 1 ),
                ( 'шкільний лікар-педіатр', 'школьный врач-педиатр', 2, 2 ),
                ( 'ні', 'нет', 10, 10 ),
                ( 'пп', 'чп', 1, 7 ),
                ( 'державний службовець', 'государственный служащий', 5, 4 ),
                ( 'держслужбовець', 'госслужащий', 5, 4 ),
                ( 'соцпрацівник', 'соцработник', 5, 4),
                #  ( '', '', ),
               ]

def similar(word, array):
    full = []
    s = difflib.SequenceMatcher()

    s.set_seq2(word)
    for ua, rus, cl_z, cl_m in (array):
        s.set_seq1(ua)
        ratio1 = s.ratio()
        s.set_seq1(rus)
        ratio2 = s.ratio()

        if ratio1 > ratio2:
            full.append((ratio1, ua, cl_z, cl_m))
        else:
            full.append((ratio2, ua, cl_z, cl_m))

        full.sort(reverse=True)

    return full[0]

df = pd.read_csv('survey-raw.csv', sep='\t')

count = 0

for index, row in df.iterrows():
    value = row['Коротко про те, ким ви працюєте:'].lower().strip()

    # compare the whole phrase
    ret = similar(value, specialities)
    if ret[0] > 0.7:
        #  print('+++++++ ' + ret[1])
        df.at[index, 'category'] = str(ret[2]) + '-' + str(ret[3])
        df.at[index, 'probability'] = ret[0]
        df.at[index, 'speciality_auto_detected'] = ret[1]
        count += 1
        continue
 
    words = value.split(' ')
    if len(words) == 1:
        # we have already compared it then
        continue
    else:
        word = words[0]

    # if not matched, compare the first word
    ret = similar(word, specialities)
    if ret[0] > 0.7:
        print('1: ' + ret[1])
        df.at[index, 'category'] = str(ret[2]) + '-' + str(ret[3])
        df.at[index, 'probability'] = ret[0]
        df.at[index, 'speciality_auto_detected'] = ret[1]
        count += 1
    else:
        word = words[1]

        # if not matched, compare the second word
        ret = similar(word, specialities)
        if ret[0] > 0.7:
            print('2: ' + ret[1])
            df.at[index, 'category'] = str(ret[2]) + '-' + str(ret[3])
            df.at[index, 'probability'] = ret[0]
            df.at[index, 'speciality_auto_detected'] = ret[1] + '(2)'
            count += 1

column_names = list(df.columns.values)

for i in range(3):
    elem = column_names.pop()
    column_names.insert(2, elem)

df = df.reindex(columns=column_names)
print(df)

print(count)

df.to_csv('res.csv', sep='\t', index=False)