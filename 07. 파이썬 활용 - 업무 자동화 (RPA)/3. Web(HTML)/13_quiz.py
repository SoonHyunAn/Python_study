# Quiz) Selenium 을 이용하여 아래 업무를 자동으로 수행하는 프로그램을 작성하시오

# 1. https://www.w3schools.com 접속 (URL 은 구글에서 w3schools 검색)
# 2. 화면 중간 LEARN HTML 클릭
# 3. 상단 메뉴 중 HOW TO 클릭
# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭
# 5. 입력란에 아래 값 입력
#   First Name : 나도
#   Last Name : 코딩
#   Country : Canada
#   Subject : 퀴즈 완료하였습니다.
#   ※ 위 값들은 변수로 미리 저장해두세요
# 6. 5초 대기 후 Submit 버튼 클릭
# 7. 5초 대기 후 브라우저 종료

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://www.w3schools.com')
browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[1]').click()
time.sleep(2)

browser.find_element(By.XPATH, '//*[@id="subtopnav"]/a[8]').click()
time.sleep(2)

browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[120]').click()
# browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click() 
time.sleep(2)

elem = browser.find_element(By.XPATH, '//*[@id="fname"]')
elem.send_keys('나도')
elem = browser.find_element(By.XPATH, '//*[@id="lname"]')
elem.send_keys('코딩')
elem = browser.find_element(By.XPATH, '//*[@id="country"]/option[contains(text(), "Ca")]')
elem.click()
elem = browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea')
elem.send_keys('퀴즈 완료하였습니다.')

time.sleep(5)

elem = browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/a')
elem.click()

time.sleep(5)
browser.close()