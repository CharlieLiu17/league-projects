
import pyautogui as ag
import pydirectinput as di
import time
import random
import cv2
import threading
import keyboard
import os
import time
import math


width = ag.size().width
height = ag.size().height

begin = 0
end = 0
# while (True):
#     print(ag.position())
# print(width, height) 
# ag.moveTo(103, 100, duration = 0.25)

class stop_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
 
        # helper function to execute the threads
    def run(self):
        while (True):
            if (keyboard.is_pressed('esc')):
                os._exit(1)

class detect_thread(threading.Thread):
    # 0.405, 0.039, -0.653
    def __init__(self, args=()):
        self.bot = args[0]
        threading.Thread.__init__(self)

    def run(self):
        global begin
        print("---")
        print("beginning detection", time.perf_counter())
        self.bot.detect_enemy()
        begin = time.perf_counter()
        print("detected", begin)


def hash(rgb):
    return rgb[0] * 0.25 + rgb[1] + rgb[2] * 4

def is_same_pixel(original, current):
    original_hash = hash(original)
    current_hash = hash(current)
    bounds = 50
    return current_hash < original_hash + bounds and current_hash > original_hash - bounds

class Coordinate:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def get_coord_tuple(self):
        return (self.x, self.y)
    
    def normalize(self):
        mag = math.sqrt(self.x ** 2 + self.y ** 2)
        return Coordinate(self.x / mag, self.y / mag)
        

class Bot:
    def __init__(self, ability_combo, ability_delay, lane_coord, move_speed, cooldown, name_plate) -> None:
        self.ability_combo = ability_combo
        self.ability_delay = ability_delay
        self.lane_coord = lane_coord #on minimap
        self.move_speed = move_speed
        self.cooldown = cooldown
        self.name_plate = name_plate
        self.center_screen_coord = Coordinate(1315, 832)
        self.enemy_x = 0
        self.enemy_y = 0
    
    def begin_game_delay(self):
        time.sleep(3)
        di.keyDown('ctrlleft')
        di.keyDown('q')
        di.keyUp('q')
        di.keyUp('ctrlleft')
        time.sleep(0.5)
        di.keyDown('ctrlleft')
        di.keyDown('w')
        di.keyUp('w')
        di.keyUp('ctrlleft')
        time.sleep(0.5)
        di.keyDown('ctrlleft')
        di.keyDown('e')
        di.keyUp('e')
        di.keyUp('ctrlleft')


    def move_to_lane(self):
        ag.click(self.lane_coord.x, self.lane_coord.y)
        time.sleep(0.5)
        ag.click(self.center_screen_coord.x, self.center_screen_coord.y, button="right")
        time.sleep(1)
        pixel = ag.pixel(self.center_screen_coord.x, self.center_screen_coord.y)
        while(is_same_pixel(pixel, ag.pixel(self.center_screen_coord.x, self.center_screen_coord.y))):
            time.sleep(1)
        time.sleep(2)

    def detect_enemy(self):
        try:
            self.enemy_x, self.enemy_y = ag.locateCenterOnScreen("_images/" + self.name_plate, confidence=0.9)
            self.enemy_y += 200
        except:
            print('no find')
            self.enemy_x, self.enemy_y = self.center_screen_coord.get_coord_tuple()
            return

    def tether(self):
        total_time = random.uniform(self.cooldown, self.cooldown * 1.0)
        is_detecting = False
        while (total_time > 0):
            begin =  time.perf_counter()
            if (not(is_detecting) and total_time < 1.5):
                is_detecting = True
                detect = detect_thread(args=(self,))
                detect.start()
            time_elapsed = random.uniform(0, 0.5)
            time.sleep(time_elapsed)
            self.random_click(300)
            end = time.perf_counter()
            total_time -= end - begin

    def random_click(self, radius):
        x = self.center_screen_coord.x + random.randint(-radius, radius)
        y = self.center_screen_coord.y + random.randint(-radius, radius)
        ag.click(x, y, button="right")

    def execute_combo(self):
        global begin, end
        end = time.perf_counter()
        print("executing at ", end)
        print("difference is" , end - begin)
        x = self.enemy_x
        y = self.enemy_y
        radius = 10
        for i, move in enumerate(self.ability_combo):
            if (i == 0 or self.ability_delay[i - 1] != 0):
                ag.moveTo(x + random.randint(-radius, radius), y + random.randint(-radius, radius), duration=0.1)
            di.press(move)
            if (self.ability_delay[i] == 0):
                continue
            self.random_click(200)
            time.sleep(self.ability_delay[i])

if (__name__ == "__main__"):
    stopper = stop_thread()
    stopper.start()
    bot = Bot(["q"], [0], Coordinate(2116, 1334), 335, 7, "GoodFoodName.JPG")
    # bot.begin_game_delay()
    bot.move_to_lane()
    iterations = 75
    for i in range(iterations):
        bot.tether()
        bot.execute_combo()

