import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

charts = soup.select('tr.list')
for chart in charts:
    rank = chart.select_one('td.number').text.strip().split(' ')[0].strip()
    title = chart.select_one('a.title').text.strip()
    artist = chart.select_one('a.artist').text.strip()

    # [rank] title / artist

    song = '[' + rank + '] ' + title + ' / ' + artist
    # song = '[{}] {} / {}'.format(rank, title, artist)
    print(song)