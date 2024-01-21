import pyautogui
# file_menu = pyautogui.locateOnScreen("file_sample.png")
# print(file_menu) # 저장된 이미지와 똑같은 부분을 클릭
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen) #찾지 못하면 None 라고 출력

# for i in pyautogui.locateAllOnScreen("checkbox.png"): # 모든 파일 이미지 클릭하기
#     print(i)
#     pyautogui.click(i, duration=0.25)

# checkbox = pyautogui.locateOnScreen("checkbox.png") #이건 맨 먼저 만나는것만 클릭
# pyautogui.click(checkbox)



# 속도 개선
# 기준 
# # trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 1. GrayScale 약 30퍼 개선 - 흑백 변환후 찾기
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정.
# pyautogui.mouseInfo() 
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(822, 701, 900 - 822, 100)) # x, y, width, height
# pyautogui.moveTo(trash_icon)


# 3. 정확도 조정 - 완벽히 같지 않아도 찾아냄
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9) # 90% 기본은 99.9퍼센트
# pyautogui.moveTo(run_btn)


# 자동화 대상이 바로 보여지지 않는 경우

#file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견 실패")

# 1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")
# pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (TimeOut)
import time
import sys

timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout: # 지정한 10초를 초과하면
#         print("시간 종료")
#         sys.exit()
#pyautogui.click(file_menu_notepad)

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()

my_click("file_menu_notepad.png", 10)
