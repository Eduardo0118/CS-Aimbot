import mss
import mouse

import cv2
import numpy
import torch
import math

import triggerbot
import aimbot
import calc_enemy

model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/Eduardo/Documents/Yolo Study/yolov5/runs/train/exp/weights/best.pt')

SCREEN_SIZE=300
lastDistance=0

def distance_to_mouse(coords):
    mouseX, mouseY = mouse.get_position()

    enemyX, enemyY = calc_enemy.GetEnemyPosition2(coords, SCREEN_SIZE)

    distance = math.sqrt(((mouseX - enemyX) ** 2) + ((mouseY - enemyY) ** 2))

    return distance

with mss.mss() as sct:
    dimensions = sct.monitors[1]

    monitor = {
        "top": int((dimensions['height'] / 2) - (SCREEN_SIZE / 2)),      
        "left": int((dimensions['width'] / 2) - (SCREEN_SIZE / 2)), 
        "width": SCREEN_SIZE, 
        "height": SCREEN_SIZE
    }

    while True:
        img = numpy.array(sct.grab(monitor))
        results = model(img)
        rl = results.xyxy[0].tolist()

        if len(rl) > 0:
            close_coords = rl[0]

            close_coords_distance_mouse = distance_to_mouse(close_coords)

            for coords in rl:
                coords_distance_mouse = distance_to_mouse(coords)

                if (coords_distance_mouse < close_coords_distance_mouse):
                    close_coords = coords
                    close_coords_distance_mouse = coords_distance_mouse

            x, y = calc_enemy.GetEnemyPosition(close_coords, SCREEN_SIZE)
            px, py = calc_enemy.GetDiffPosition(close_coords, SCREEN_SIZE)

            aimbot.Aimbot(x, y)
            triggerbot.TriggerBot(px)

        cv2.imshow("Cs 1.6", numpy.squeeze(results.render()))
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break