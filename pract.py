# -*- coding: cp1251 -*-
import pygame as pg
import numpy as np
import json
sc = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
run = True
strin = str(input('File:'))
v = int(input('line_strong:'))
st = []
blu = (255, 255, 255)
gr = (int(input('red:')), int(input('green:')), int(input('blue:')))
sc.fill(blu)
st2 = []
while run:
        for event in pg.event.get():
                if event.type == pg.QUIT:
                          run = False
                if event.type == pg.MOUSEBUTTONDOWN:
                          pre = pg.mouse.get_pressed()
                          pos = pg.mouse.get_pos()
                          if st==[]:
                                  st = [[pos[0], pos[1]]]
                          pg.draw.line(sc, gr, st[0], pos, v)
                          st = []
                          st.append([pos[0], pos[1]])
                          st2.append(st[0])
        pg.display.flip()
sttts = {"store": st2, "color": gr, "winds": [0,0,0,1,2,10,20,30,40,0,0,0], "shadow": (gr[0]//2, gr[1]//2, gr[2]//2)}
with open(f'{strin}.json', 'w', encoding='utf-8') as file:
    json.dump(sttts, file, ensure_ascii=False, indent=4)
