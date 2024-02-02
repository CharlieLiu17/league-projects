
import pyautogui as ag
import pydirectinput as di
import time
import random
import cv2
import threading
import keyboard
import os
import time
import championbot as cb


class ZedBot(cb.Bot):
    def __init__(self, ability_combo, ability_delay, lane_coord, move_speed, cooldown, name_plate) -> None:
        cb.Bot.__init__(self, ability_combo, ability_delay, lane_coord, move_speed, cooldown, name_plate)
    
    
    def begin_game_delay(self):
        time.sleep(3)
        di.keyDown('ctrlleft')
        di.keyDown('q')
        di.keyUp('q')
        di.keyUp('ctrlleft')





if __name__ == "__main__": 
    stopper = cb.stop_thread()
    stopper.start()
    bot = Bot(["w", "e", "q"], [0, 0.5, 0], cb.Coordinate(2116, 1334), 335, 15, "EnemyHP.JPG")
    bot.move_to_lane()
    iterations = 25
    for i in range(iterations):
        bot.tether()
        bot.execute_combo()

