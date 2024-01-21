# 크롬 버전 116.0.5845.188
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import datetime

current_day = datetime.now().day

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service("./chromedriver.exe")
browser = webdriver.Chrome(service=service, options=chrome_options)
browser.maximize_window() # 창 큰화면으로 전환

browser.get("https://flight.naver.com/")

elem = browser.find_element(By.XPATH, '//button[text()="가는 날"]').click()

# 이번달 27~28일 선택, 모든 달에 있기 때문에 
# 리스트로 정보를 가져오고, 원하는 (월 순서 -1) 값을 선택함
day27 = browser.find_elements(By. XPATH, '//b[text()="27"]')
day27[1].click()
day28 = browser.find_elements(By. XPATH, '//b[text()="28"]')
day28[1].click()


def wait_a_moment(i, o):
    WebDriverWait(browser, i).until(EC.presence_of_element_located((By. XPATH, o)))

# 도착지 설정.
wait_a_moment(2, '//b[text()="도착"]')
arrival = browser.find_element(By. XPATH, '//b[text()="도착"]').click()
wait_a_moment(2, '//button[text()="국내"]')
domestic = browser.find_element(By. XPATH, '//button[text()="국내"]').click()
wait_a_moment(2, '//i[contains(text(), "제주국제공항")]')
jeju = browser.find_element(By.XPATH, '//i[contains(text(), "제주국제공항")]').click()
wait_a_moment(2, '//span[contains(text(), "항공권 검색")]')
search = browser.find_element(By. XPATH, '//span[contains(text(), "항공권 검색")]').click()
elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By. XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))
print(elem.text)

browser.quit()