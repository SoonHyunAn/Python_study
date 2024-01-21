import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':r'H:\etc\Etc\Python\7. 파이썬 활용 - 업무 자동화 (RPA)\3. Web(HTML)'}) # 기본 경로 설정

browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

browser.switch_to.frame('iframeResult')

# download 링크 클릭
elem = browser.find_element(By.XPATH, '/html/body/p[2]/a')
elem.click()

time.sleep(5)
browser.quit()