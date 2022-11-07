import mouse
import math

def GetEnemyPosition2(coords, screen_size):
    x = int(coords[0])
    y = int(coords[1])
    width = int(coords[2])
    height = int(coords[3])

    centerX = int((width + x) / 2)
    centerY = int((height + y) / 2) 

    positionX, positionY = mouse.get_position()

    enemyX = positionX + (centerX - (screen_size / 2))
    enemyY = positionY + (centerY - (screen_size / 2))
    return enemyX, enemyY

def GetEnemyPosition(coords, screen_size):
    xmin = int(coords[0])
    ymin = int(coords[1])
    xmax = int(coords[2])
    ymax = int(coords[3])

    centerX = (xmax - xmin) / 2 + xmin
    centerY = (ymax - ymin) / 2 + ymin

    enemyX = centerX - (screen_size / 2)
    #enemyY = centerY - (screen_size / 2)
    enemyY = ymin - (screen_size / 2)
    return enemyX, enemyY    

def GetDiffPosition(coords, screen_size):
    x = GetEnemyPosition2(coords, screen_size)
    mX = mouse.get_position()

    diff = (mX - x) * 2

    return diff * diff