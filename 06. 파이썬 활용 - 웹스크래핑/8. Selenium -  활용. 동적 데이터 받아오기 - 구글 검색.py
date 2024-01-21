import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

url = "https://www.google.com/search?sca_esv=567840750&sxsrf=AM9HkKmikvsNq7rmMGIBR7g0z7CqUcux3Q:1695473482617&q=%EC%A7%95%EB%B2%84%EA%B1%B0&tbm=isch&source=lnms&sa=X&ved=2ahUKEwi_5KD14sCBAxUJCYgKHZ4NBtsQ0pQJegQIDRAB&biw=958&bih=937&dpr=1"
# Accept-Language: 기본 언어가 한글이 아닌 곳에서 한글로 된 버전이 있을경우 불러올 수 있게 함.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko"
    }

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service("./chromedriver.exe")
browser = webdriver.Chrome(service=service, options=chrome_options)
browser.maximize_window() # 창 큰화면으로 전환
browser.get(url)

# 스크롤을 내려서 새로 나오는 정보 확인하기, 반복해야함
# browser.execute_script("window.scrollTo(0, 1080)") #윈도우 세로 1080 으로 내림 (해상도)
interval=2
prev_height = browser.execute_script("return document.body.scrollHeight")

while True: # 검색 결과가 계속 있다면 무한대...
    #화면 가장 아래로 내리기
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #대기
    time.sleep(interval)
    #현재 문서 높이를 가져와서 저장
    curr_height=browser.execute_script("return document.body.scrollHeight")
    if curr_height==prev_height:
        print("스크롤 완료")
        time.sleep(20)
        break
    prev_height = curr_height
    search = []

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# 긁어오는 값을 확인하는 것 - HTML 형성
with open("search.html", "w", encoding="utf8") as f:
#      f.write(res.text)
    f.write(soup.prettify()) # html 문서를 예쁘게 출력

searches = soup.find_all("h3", attrs={"class":["bytUYc"]})
print(len(searches))
    
for search in searches:
    print(search.get_text())

# 스크롤을 끝까지 내리는데 정보를 가져오는 함수에 의해서 받아오는 값은 48개 뿐임.... 왜 그럴까... 더보기를 누르지 않을 경우 class name과 겹치는 값은 400개임.