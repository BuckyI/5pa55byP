from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
list = [11, 17, 23, 29, 41, 45, 53, 59, 71, 75, 79, 89, 121, 131, 171, 181]
time.sleep(5)
for number in list:
    with keyboard.pressed(Key.alt):
        time.sleep(0.5)
        keyboard.press('f')
        time.sleep(0.5)
        keyboard.release('f')
        time.sleep(0.5)
        keyboard.press('c')
        time.sleep(0.5)
        keyboard.release('c')
        time.sleep(0.5)
        # SECOND
        keyboard.press('f')
        time.sleep(0.5)
        keyboard.release('f')
        time.sleep(0.5)
        keyboard.press('c')
        time.sleep(0.5)
        keyboard.release('c')
        time.sleep(0.5)

        keyboard.press('f')
        time.sleep(0.5)
        keyboard.release('f')
        time.sleep(0.5)
        keyboard.press('2')
        time.sleep(0.5)
        keyboard.release('2')
        time.sleep(3)
        # SECOND
        keyboard.press('f')
        time.sleep(0.5)
        keyboard.release('f')
        time.sleep(0.5)
        keyboard.press('2')
        time.sleep(0.5)
        keyboard.release('2')
        time.sleep(3)

    # 先切换下标签
    with keyboard.pressed(Key.ctrl):
        time.sleep(0.5)
        keyboard.press(Key.tab)
        time.sleep(0.5)
        keyboard.release(Key.tab)
        time.sleep(0.5)

    with keyboard.pressed(Key.ctrl):
        time.sleep(0.5)
        keyboard.press('p')
        time.sleep(0.5)
        keyboard.release('p')
        time.sleep(0.5)
    for a in range(3):
        keyboard.press(Key.tab)
        time.sleep(0.5)
        keyboard.release(Key.tab)
        time.sleep(0.5)
    keyboard.type(str(number))
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.5)
    keyboard.type(str(number + 1))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    keyboard.type(str(number) + '-' + str(number + 1))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(30)
    