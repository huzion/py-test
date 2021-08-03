import os
import jieba
from bs4 import BeautifulSoup

os.chdir('zhe-shi-yi-ge-ye-mian/wordfre-test')
txt = open('./test.html').read()
html = BeautifulSoup(txt, 'html.parser')
content = html.get_text()

wordsls = jieba.lcut(content)ß
wcdict = {}
for word in wordsls:
    if len(word) == 1:ß
        continue
    else:
        wcdict[word] = wcdict.get(word,0)+1ß

wcls = list(wcdict.items())
wcls.sort(key = lambda x:x[1], reverse = True)

for i in range (10):
    print(wcls[i])
