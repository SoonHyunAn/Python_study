import pyautogui

size = pyautogui.size() # 현재 화면의 스크린 사이즈를 가져옴
print(size)

#마우스 이동
pyautogui.moveTo(100, 100, duration=5) # 지정한 좌표로 마우스 커서 이동, duration: 지정된 시간동안 천천히 이동
print(pyautogui.position())

pyautogui.move(200,100) # 현재 커서 기준으로 상대 위치로 이동
print(pyautogui.position())

p=pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)

# 마우스 액션
