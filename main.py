# -*- coding: cp1251 -*-
import pygame
from pynput import keyboard
import func
import time
import numpy as np
import lib as PR
import wind_tracer as Wind
import json
sc = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
xuu, yuu = 100, 300
x, y = 100, 400
wx, wy = x, y
speed = 50
cou = 0
F = 0
b = 0
V = x, y
sr = []
tm = 0
col = [(0,0,0), (200,0,0), (0,0,200), (0,200,0), (0,50,200), (0,150,255), (255,255,0)]
def on_press(key):
    global wx, x, speed, uu, cou, F, stp, hp, hp2, hp3
    if key == keyboard.Key.right:
        wx = wx-speed
        x = x-speed
    if key == keyboard.Key.left:
        wx = wx+speed
        x = x+speed
    cou = cou+1
    F = np.random.randint(-5, 6)+F
    if F>21 or F<-20:
        F = np.random.randint(-20, 21)
def on_release(key):
    global cou, F
    cou = 0
    F = 0
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
with open('pre.json', 'r', encoding="utf-8") as file:
              data = json.load(file)
player = PR.reader(sc, data)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    with open('pre.json', 'r', encoding="utf-8") as file:
              data = json.load(file)
    sc.fill(col[4])
    if tm==57:
         player = PR.reader(sc, data)
         player.namste_В()
         tm = 0
    player.polygon()
    pygame.display.flip()
    tm = tm+1
