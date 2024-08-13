"""Модуль парсит главную яндекс-маркета. и из этого рандома выбирает предложение с наибольшей скидкой"""

import requests
import pandas as pd
source='https://market.yandex.ru/'
html = requests.get(source)
print(str(html))
with open('result.html', 'w', encoding="utf-8") as file:
    file.write(html.text)
html = html.text
start_0 = '<!--BEGIN [@light/RecomSnippet]'
end_0 = '<!--END [@light/RecomSnippet]'
span_0 = 'data-auto="snippet-link">'
span_1 = '</span>'
span_2 = '>'
sep1 = 'href="/product'
sep2 = '&amp;'
s1 = html.find(start_0)
e1 = html.rfind(end_0)
html = html[s1:e1]
e1 = 1
chk = 0
res = []
res1 = []
res2 = []
while e1 != -1 or s1 != -1:
    s1 = html.find(span_0, e1 + 1)
    e1 = html.find(span_1, e1 + 1)
    txt = str(html[s1:e1])
    s2 = html[:s1].rfind(sep1)
    e2 = html[s2:].find(sep2)

    link = html[s2 + 7:s2+e2]
    s3 = txt.rfind('>')
    txt = (txt[s3 + 1:].replace('\u2009', '')
           .replace('Цена ', 'Цена :')
           .replace(' ₽ вместо ', '/')
           .replace('&quot',chr(34))
           .replace(' ',''))

    if len(txt):
        if 'цена' in txt.lower():
            chk += 1
            if chk == 1:
                res1.append(txt.replace('Цена :', '').split('/'))
        else:
            chk = 0
            res.append(txt.replace('&amp;','&').replace('&#x27;','`'))
            res2.append(source+link)

d = pd.DataFrame(list(zip(res, [i[0] for i in res1], [i[1] for i in res1],res2)),
                 columns=['name', 'price', 'old_price','link'])
d['price'] = pd.to_numeric(d['price'])
d['old_price'] = pd.to_numeric(d['old_price'])
d['discount'] = round((1 - d.price / d.old_price) * 100, 2)
d.to_csv('result_table.csv')
d_best=d[d.discount==d['discount'].max()].values[0]
print(f'Максимальная скидка на товар: {d_best[0]} - {d_best[4]}% \nЦена: {d_best[1]} \nЦена без скидки: {d_best[2]} \nСсылка: {d_best[3]}')
