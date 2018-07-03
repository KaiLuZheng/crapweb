#!/usr/bin/python3

from bs4 import BeautifulSoup as bs


with open('temp.html', 'r') as f:
    html = f.read()


soup = bs(html, 'html.parser')

aim = soup.find_all('div',id='article_show')

if len(aim) > 0:
    aim_text = str(aim[0])
else:
    print(aim)

with open('aim_text.html', 'w') as f:
    f.write(aim_text)

another = str(aim[0].find_all('div', class_='article_text')[0])

with open('simple.html', 'w') as f:
    f.write(another)



