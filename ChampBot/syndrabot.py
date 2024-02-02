
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
# while (True):
#     print(ag.position())
# print(width, height)
# ag.moveTo(103, 100, duration = 0.25)


        
##TODO: Finish Inheritance work
class SyndraBot(cb.Bot):
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
    bot = SyndraBot(["q", "e"], [0, 0], cb.Coordinate(2120, 1345), 335, 7, "GoodFoodName.JPG")
    # bot.begin_game_delay()
    bot.move_to_lane()
    iterations = 100
    for i in range(iterations):
        bot.tether()
        bot.execute_combo()

