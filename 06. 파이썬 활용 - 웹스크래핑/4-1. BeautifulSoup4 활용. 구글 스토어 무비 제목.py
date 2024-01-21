import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies"
# Accept-Language: 기본 언어가 한글이 아닌 곳에서 한글로 된 버전이 있을경우 불러올 수 있게 함.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko"
    }

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"Epkrse"})
print(len(movies))

# 긁어오는 값을 확인하는 것
with open("movie.html", "w", encoding="utf8") as f:
     #f.write(res.text)
    f.write(soup.prettify()) # html 문서를 예쁘게 출력

for movie in movies:
    print(movie.get_text())