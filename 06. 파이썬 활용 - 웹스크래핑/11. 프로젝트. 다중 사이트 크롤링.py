# 프로젝트: 웹 스크래핑을 이용하여 나만의 비서를 만드시오

# 조건
# 1. 네이버에서 오늘 서울의 날씨 정보를 가져온다.
# 2. 헤드라인 뉴스 3건을 가져온다.
# 3. it 뉴스 3건을 가져온다.
# 4. 해커스 어학원 홈페이지에서 오늘의 영어 회화 지문을 가져온다. 

# 예시

# [오늘의 날씨]
# 흐림, 어제보다 00도 높아요
# 현재 00도 (최저 00도/ 최고 00도)
# 오전 강수확률 00%/ 오후 강수확률 00%

# 미세먼지 00 좋음
# 초미세먼지 00 좋음

# [헤드라인 뉴스]
# 1. 무슨 무슨 일이~
# (링크: ~~)
# ...

# [IT 뉴스]
# 1. 무슨 무슨 일이~
# (링크: ~~)
# ...

# [오늘의 영어 회화]
# (영어 지문)
# ~~

# (한글 지문0)
# ~~

import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

url_3="https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
url_4="https://www.hackers.co.kr/?c=s_lec/lec_study/lec_I_others_english"


def create_soup(url):
    res=requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml") 
    return soup

def scrape_weather():
    url="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    
    area = soup.find("h2", attrs={"class":"blind"}).get_text()
    print("오늘 {} 날씨".format(area))
    
    # 흐림, 어제보다 00도 높아요
    compare_yesterday=soup.find("p", attrs={"class":["summary","temperature down","temperature up"]})
    print(compare_yesterday.get_text())
    
    # 현재 00도 (최저 00도/ 최고 00도)
    current_temp=soup.find("div", attrs={"class":["weather_graphic"]})
    max_temp=soup.find("span", attrs={"class":["highest"]})
    min_temp=soup.find("span", attrs={"class":"lowest"})
    print("{}/ {}/ {}".format(current_temp.get_text().replace("  ", ""), min_temp.get_text().replace("  ", " "),  max_temp.get_text().replace("  ", " ")))
    
    # 오전 오후 강우 확률
    rain_ration=soup.find("div", attrs={"class":"cell_weather"})
    print(rain_ration.get_text().replace("   ","/"))
   
    #미세먼지, 자외선, 일몰
    dust=soup.find("ul", attrs={"class":"today_chart_list"})
    print("{}".format(dust.get_text().replace("   ", "/").replace("  ", "")))

def main_news():
    print("오늘 메인 뉴스")
    url="https://news.naver.com/"
    count=1
    while count < 4:
        soup = create_soup(url)
        news= soup.find("div", attrs={"class":"cjs_journal_wrap _item_contents"}).find("div", attrs={"class":"cjs_t"})
        link = soup.find('div', class_={"cjs_journal_wrap _item_contents"})
        print("{}. ".format(count), news.get_text())
        print("링크: ".format(link.find("a").attrs["href"]))
        
        count+=1

def it_news():
    pass

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]: # 8문장이 있다고 가정할 때, index 기준 4~7 까지 잘라서 가져옴
        print(sentence.get_text().strip())

    print()
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]: # 8문장이 있다고 가정할 때, index 기준 0~3 까지 잘라서 가져옴
        print(sentence.get_text().strip())
    print()




# scrape_weather()
# main_news()
scrape_english()