import keyboard
import mouse
import math

def TriggerBot(enemyX):
    positionX, _ = mouse.get_position()
    diffPosition = (positionX - enemyX) * 2

    if keyboard.is_pressed('v'):
        if diffPosition > 0:
            positionResult = math.sqrt(diffPosition)
            if positionResult < 7:
                mouse.click()