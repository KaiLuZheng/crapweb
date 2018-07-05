#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

user_agent_ = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'


headers_ = {'User-Agent':user_agent_
}


url = 'https://meiriyiwen.com/random'

filetype = '.html'

filename = 'temp'


'''
    other headers see https 
'''

chrome_options = Options()

options_add_argument = ('--headless','--disabel-gpu')

for i in options_add_argument:
    chrome_options.add_argument(i)

opener = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities = headers_)

opener.get(url)

with open(filename+filetype, 'w') as f:
    f.write(opener.page_source)

