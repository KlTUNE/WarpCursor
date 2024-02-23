import pyautogui

flag = 0
BORDER = 0

while True:
    cursor_position = pyautogui.position()
    print(cursor_position, flag)
    if cursor_position.x >= BORDER and flag == 1:
        flag = 0
        # pyautogui.moveTo(cursor_position.x, 800)
    elif cursor_position.x < BORDER and flag == 0:
        flag = 1
        if cursor_position.y >= 0:
            # aa = 400
            aa = int((cursor_position.y*(1727/1079)) - 1080)
            pyautogui.moveTo(cursor_position.x, aa)
        else:
            pyautogui.moveTo(cursor_position.x, -1080)
