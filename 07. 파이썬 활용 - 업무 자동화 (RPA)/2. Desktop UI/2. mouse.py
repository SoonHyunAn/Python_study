import pyautogui

# #마우스 이동
# pyautogui.moveTo(100, 100, duration=5) # 지정한 좌표로 마우스 커서 이동, duration: 지정된 시간동안 천천히 이동
# print(pyautogui.position())

# pyautogui.move(200,100) # 현재 커서 기준으로 상대 위치로 이동
# print(pyautogui.position())

# p=pyautogui.position()
# print(p[0], p[1])
# print(p.x, p.y)

# # 마우스 액션
# pyautogui.sleep(3) #3초 대기
# print (pyautogui.position())

# pyautogui.click(51,13,duration=1) # 메뉴바의 File을 클릭 (1초 동안 이동 후)
# #click =  pyautogui.mouseDown() + pyautogui.mouseUp()
# pyautogui.sleep(3) #3초 대기
# pyautogui.click(clicks=500)

# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown() # 마우스 버튼 누른 상태
# pyautogui.moveTo(300, 300)
# pyautogui.mouseUp() # 마우스 버튼 뗀 상태

# pyautogui.sleep(3) # 3초 대기
# pyautogui.rightClick() # 오른쪽 마우스
# pyautogui.middleClick() # 휠 클릭

# #메모장 이동하기
# print(pyautogui.position())
# pyautogui.moveTo(1114, 349)
# pyautogui.drag(100, 0) # 현재 위치 기준으로 x 100 만큼, y 0 만큼 드래그
# pyautogui.drag(100, 0, duration=0.25) # 너무 빠른 동작으로 drag 수행이 안될때는 duration 값 설정
# pyautogui.dragTo(1514, 349, duration=0.25) # 절대 좌표 기준으로 x 1514, y 349 로 드래그

# pyautogui.scroll(300) # 양수이면 위 방향으로, 음수이면 아래 방향으로 300만큼 스크롤.

# # 마우스 정보 얻기
# #pyautogui.FAILSAFE = False 중간에 마우스를 귀퉁이에 놓아 멈추는것을 제한 - 가급적 사용하지 않는것을 권고
# pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용
# #pyautogui.mouseInfo() - 마우스 커서 위치의 위치 정보와 색 정보를 알려줌
# # F1으로 좌표, RGB 값 추출 가능
# for i in range(5):
#     pyautogui.move(100, 100)