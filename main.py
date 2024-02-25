import pyautogui

flag = 0
BORDER = 0

while True:
    cursor_position = pyautogui.position()
    print(cursor_position, flag)

    if cursor_position.x >= BORDER and flag == 1:
        flag = 0
        # if cursor_position.y < 420: pyautogui.moveTo(cursor_position.x, (cursor_position_old.y+1080) * (1079/1500))
        # else: pyautogui.moveTo(cursor_position.x, 1079)

    elif cursor_position.x < BORDER and flag == 0:
        flag = 1
        if cursor_position.y >= 0: pyautogui.moveTo(cursor_position.x, cursor_position_old.y*(1500/1079) - 1080)
        else: pyautogui.moveTo(cursor_position.x, -1080)
    cursor_position_old = cursor_position
