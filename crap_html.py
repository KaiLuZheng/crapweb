#!/usr/bin/python3

import urllib.request
import chardet

from bs4 import BeautifulSoup as bs


url = 'https://meiriyiwen.com/'

filetype = '.html'

filename = 'temp'

_user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36'

_headers = {'User-Agent':_user_agent
}


req = urllib.request.Request(url, headers=_headers)
res = urllib.request.urlopen(req, timeout=5)

rhtml = res.read()
encode = chardet.detect(rhtml)['encoding']



with open(filename+filetype, 'w') as f:
    f.write(rhtml.decode(encode))




