import pyautogui
# 스크린 샷 찍기
img = pyautogui.screenshot()
img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 23,19 50,165,241 #32A5F1 - 로고 정보

pixel = pyautogui.pixel(23, 19)
print(pixel)

#print(pyautogui.pixelMatchesColor(23, 19, (50,165,241)))
#print(pyautogui.pixelMatchesColor(23, 19, pixel))
print(pyautogui.pixelMatchesColor(23, 19, (50,165,241)))