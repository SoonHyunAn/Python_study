import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 브라우저를 띄우지 않고 백그라운드에서 진행하기 위한 조건
options = webdriver.ChromeOptions()
options.headless=True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36")

service = Service("./chromedriver.exe")
browser = webdriver.Chrome(service=service, options=options)
browser.maximize_window()


url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
# AppleWebKit/537.36 (KHTML, like Gecko) 
# Chrome/116.0.0.0 
# Safari/537.36
#----------------------
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
# AppleWebKit/537.36 (KHTML, like Gecko) 
# HeadlessChrome/116.0.5845.188  -- headless를 사용할경우 chrome의 값이 headless로 변환됨을 확인할 수 있음. 따라서 13번 줄 처럼 user-agent를 넣어주면 정상적으로 추출가능
# Safari/537.36
detected_value = browser.find_element(By. ID, "detected_value")
print(detected_value.text)
browser.quit()
