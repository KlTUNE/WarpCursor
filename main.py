import pyautogui

flag = 0
BORDER = 900

while True:
    cursor_position = pyautogui.position()
    print(cursor_position.x, flag)
    if cursor_position.x >= 900 and flag == 0:
        flag = 1
        pyautogui.moveTo(cursor_position.x, 800)
    elif cursor_position.x <= 900 and flag == 1:
        flag = 0
        pyautogui.moveTo(cursor_position.x, 0)
