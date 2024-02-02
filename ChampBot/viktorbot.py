
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


class ViktorBot(cb.Bot):
    def __init__(self, ability_combo, ability_delay, lane_coord, move_speed, cooldown, name_plate) -> None:
        cb.Bot.__init__(self, ability_combo, ability_delay, lane_coord, move_speed, cooldown, name_plate)
        self.x = 0
        self.y = 0
        self.center_coord = cb.Coordinate(1155, 672)
    
    
    def begin_game_delay(self):
        time.sleep(3)
        di.keyDown('ctrlleft')
        di.keyDown('e')
        di.keyUp('e')
        di.keyUp('ctrlleft')

    def tether(self):
        self.x = self.lane_coord.x
        self.y = self.lane_coord.y
        radius = 300
        total_time = random.uniform(self.cooldown, self.cooldown * 1.0)
        is_detecting = False
        while (total_time > 0): #Finish viktor tether, then execute combo
            if (not(is_detecting) and total_time < 1.5):
                is_detecting = True
                detect = cb.detect_thread(args=(self,))
                detect.start()
            new_x, new_y = self.random_click(300)
            begin =  time.perf_counter()
            time_elapsed = random.uniform(0, 0.5)
            time.sleep(time_elapsed)
            moving_end = time.perf_counter()
            direction = cb.Coordinate(new_x - self.x, new_y - self.y).normalize()
            self.x += direction.x * (self.move_speed * 2 / 3) * (begin - moving_end)
            self.y += direction.y * (self.move_speed * 2 / 3) * (begin - moving_end)
            end = time.perf_counter()
            total_time -= begin - end
            

    def random_click(self, radius):
        new_x = random.randint(-radius, radius)
        new_y = random.randint(-radius, radius)
        ag.click(self.lane_coord.x + new_x, self.lane_coord.y + new_y, button="right")
        print(new_x, new_y)
        return new_x, new_y
        





if __name__ == "__main__": 
    stopper = cb.stop_thread()
    stopper.start()
    bot = ViktorBot(["e"], [0], cb.Coordinate(2116, 1334), 335, 10, "EnemyHP.JPG")
    bot.begin_game_delay()
    iterations = 25
    for i in range(iterations):
        bot.move_to_lane()
        bot.tether()
        bot.execute_combo()

