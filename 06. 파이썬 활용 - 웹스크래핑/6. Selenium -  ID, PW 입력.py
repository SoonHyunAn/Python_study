# 크롬 버전 116.0.5845.188
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service("./chromedriver.exe")
browser = webdriver.Chrome(service=service, options=chrome_options)

browser.get("http://naver.com")

elem = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW") 
elem.click()

id= browser.find_element(By. ID, "id")
id.send_keys("잘못된 아이디")

pw= browser.find_element(By. ID, "pw")
pw.send_keys("잘못된 비밀번호")

elem = browser.find_element(By.ID, "log.login").click()

time.sleep(3)

browser.find_element(By. ID, "id").clear()
browser.find_element(By. ID, "id").send_keys("옳은 아이디")

print(browser.page_source)

browser.quit()
