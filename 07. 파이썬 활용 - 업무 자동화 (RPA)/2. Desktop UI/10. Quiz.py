# Quiz) 아래 동작을 자동으로 수행하는 프로그램을 작성하시오

# 1. 그림판 실행 (단축키 : win + r, 입력값 : mspaint) 및 최대화

# 2. 상단의 텍스트 기능을 이용하여 흰 영역 아무 곳에다가 글자 입력
#  - 입력 글자 : "참 잘했어요"

# 3. 5초 대기 후 그림판 종료
#  이 때, 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함

import pyautogui
import pyperclip

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

pyautogui.PAUSE = 1
pyautogui.hotkey("win", "r")

my_write("mspaint")
pyautogui.press("enter")

w = pyautogui.getWindowsWithTitle("제목 없음")[0] 
if w.isMaximized == False: 
    w.maximize() # 최대화

word_icon = pyautogui.locateOnScreen("write_word.png")
pyautogui.moveTo(word_icon)
pyautogui.click()
pyautogui.move(0,200)
pyautogui.click()

my_write("참 잘했어요")

pyautogui.sleep(5)

w.close() 
pyautogui.press("right")
pyautogui.press("enter")

""" 답안
import sys
import pyautogui
import pyperclip

pyautogui.hotkey("win", "r") # 단축키 : win + r 입력
pyautogui.write("mspaint") # 프로그램 명 입력
pyautogui.press("enter") # 엔터 키 입력

# 그림판 나타날 때까지 2초 대기
pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0] # 그림판 1개만 뜨워져 있다고 가정
#if window.isMaximized == False:
#    window.maximize() # 최대화

# 글자 버튼 클릭
btn_text = pyautogui.locateOnScreen("btn_text.png", confidence=0.8)
if btn_text:
    pyautogui.click(btn_text, duration=0.5)
else:
    print("찾기 실패")
    sys.exit()

# 흰 영역 클릭
#pyautogui.click(200, 200, duration=0.5)

btn_brush = pyautogui.locateOnScreen("btn_brush.png")
pyautogui.click(btn_brush.left - 200, btn_brush.top + 200)

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("참 잘했어요")

# 5초 대기
pyautogui.sleep(5)

# 프로그램 종료
window.close()
pyautogui.sleep(0.5)
pyautogui.press("n") # 저장하지 않음

"""