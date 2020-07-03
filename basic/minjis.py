import requests
from bs4 import BeautifulSoup

from dataclasses import dataclass
import nltk
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt
from nltk import FreqDist

import pandas as pd
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

search_keyword = 'fkj'
url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search_keyword}'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
news_titles = soup.select('.news .type01 li dt a[title]')

print('총', len(news_titles), '개의 뉴스 제목이 있습니다')
print()
for title in news_titles:
    print(title['title'])



https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query=fkj&sm=tab_pge&srchby=all&st=sim&where=post&start=11
https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query=fkj&sm=tab_pge&srchby=all&st=sim&where=post&start=21
https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query=fkj&sm=tab_pge&srchby=all&st=sim&where=post&start=121