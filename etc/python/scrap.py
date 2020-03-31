import requests
import bs4

r = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")

soup = bs4.BeautifulSoup(r.text, 'html.parser')

aTags = soup.select('div.tit3 > a')
for a in aTags[:10]:
    print(a.text)