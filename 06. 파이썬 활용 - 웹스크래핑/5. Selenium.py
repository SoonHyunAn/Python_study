# 크롬 버전 116.0.5845.188
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service("./chromedriver.exe")
browser = webdriver.Chrome(service=service, options=chrome_options)

browser.get("http://naver.com")

# 로그인 창 클릭하기
elem = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW") 
elem.click()

# 앞으로 뒤로 가기, 새로 고침
browser.back()
browser.forward()
browser.refresh()
browser.back()


# 검색창에 입력하고 엔터치기 
elem = browser.find_element(By. ID, "query")
elem.send_keys("나도 코딩 한다")
elem.send_keys(Keys.ENTER)

# 화면의 href값 가져오기 - 모든 정보를 위해 elements
elem = browser.find_elements(By. TAG_NAME, "a")
for e in elem:
    e.get_attribute("href")

# 다음에 가서 검색창 사용하기
browser.get("http://daum.net")

elem = browser.find_element(By. NAME, "q")
elem.send_keys("나도 코딩")
elem.send_keys(Keys. ENTER)

browser.back()

# +돋보기 버튼을 눌러서 검색하기 - Xpath 사용
elem = browser.find_element(By. NAME, "q")
elem.send_keys("나도 코딩")
elem = browser.find_element(By. XPATH, "//*[@id='daumSearch']/fieldset/div/div/button[3]")
elem.click()

# close는 탭 하나, quit은 브라우저 전체
browser.close()
browser.quit()