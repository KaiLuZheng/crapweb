#!/usr/bin/python3

from bs4 import BeautifulSoup as bs
import re

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

title = re.findall(r'<h1>(.*?)</h1>', aim_text)
print(title[0])

title = re.findall(r'<p>(.*?)</p>', aim_text, re.S)

for i in title:
    t = i.replace('\n' or '\r' or '\\s' or '\r\n' or '\n\r', '')
    if len(t) >= 1:
        #print('%s'%t)
        pass

author = re.findall(r'<p.*?><span>(.*?)</span></p>', aim_text)[0]
print(author)

print(aim[0].find_all('p', class_='article_author'))



'''
for i in title:
    if i == '\n' or i == '\r' or i == '\r\n' or i == '\n\r':
        pass
    else:
        print('[%s]'%i)
'''

#with open('simple.html', 'w') as f:
#    f.write(another)



