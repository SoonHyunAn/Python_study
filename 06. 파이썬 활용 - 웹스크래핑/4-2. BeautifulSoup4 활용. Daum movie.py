import requests
import re
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
}


for year in range (2015, 2020):
    url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q={}+%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84".format(year)
    res =requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    images=soup.find_all("img", attrs={"class":"thumb_img"})
    
    for idx, image in enumerate(images):
        image_url =image["src"]
        image_res=requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)

        if idx >= 4:
            break
