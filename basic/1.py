import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

plusUrl = urllib.parse.quote_plus(input('검색어 입력:'))
# 사용자가 원하는 키워드 입력

pageNum = 1

i = input('몇페이지 크롤링?\n')
lastPage = int(i)

while pageNum < lastPage + 1:

    url = f'https://www.data.go.kr/search/index.do?index=DATA&currentPage={pageNum}&countPerPage=10&sortType=VIEW_COUNT&data-order="DESC"&query={plusUrl}'

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    for j in soup.find_all('div', class_='data-item'):
        tag1 = j.find('div', attrs={'class': 'data-title'}).find('a')
        tag2 = j.find('div', attrs={'class': 'data-desc'})
        tag3 = tag1['href']
        url1 = f'https://www.data.go.kr{tag3}'

        html1 = urllib.request.urlopen(url1).read()
        soup1 = BeautifulSoup(html1, 'html.parser')
        tag4 = soup1.find('a', {'id': 'url-in-detail-btn'})
        print(tag4)

        print('--------------------')
        # tag1 중 text만 추출(.text)하고, 왼쪽의 공백을 제거(.lstrip())한다
        print(tag1.text.lstrip())
        print(url1)
        print(tag2.text.lstrip())

    pageNum += 1