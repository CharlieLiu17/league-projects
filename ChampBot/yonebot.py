
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



#TODO: Why is yone bot not working? Theory: the target dummy healing interferes with detection
class YoneBot(cb.Bot):
    def __init__(self, ability_combo, ability_delay, lane_coord, move_speed, cooldown, name_plate) -> None:
        cb.Bot.__init__(self, ability_combo, ability_delay, lane_coord, move_speed, cooldown, name_plate)
    
    def begin_game_delay(self):
        time.sleep(3)
        di.keyDown('ctrlleft')
        di.keyDown('q')
        di.keyUp('q')
        di.keyUp('ctrlleft')

    def tether(self):
        total_time = random.uniform(self.cooldown, self.cooldown * 1.0)
        is_detecting = False
        while (total_time > 0):
            begin =  time.perf_counter()
            if (not(is_detecting) and total_time < 1.5):
                is_detecting = True
                detect = cb.detect_thread(args=(self,))
                detect.start()
            time_elapsed = random.uniform(0, 0.5)
            time.sleep(time_elapsed)
            self.random_click(300)
            end = time.perf_counter()
            total_time -= end - begin


if __name__ == "__main__": 
    stopper = cb.stop_thread()
    stopper.start()
    bot = YoneBot(["q"], [0], cb.Coordinate(2120, 1345), 335, 2.5, "GoodFoodName.JPG")
    bot.begin_game_delay()
    bot.move_to_lane()
    iterations = 100
    for i in range(iterations):
        bot.tether()
        bot.execute_combo()

