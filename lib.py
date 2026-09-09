# -*- coding: cp1251 -*-
import pygame
import numpy as np
import json
b = 0
c = 0
cou = 0
st = []
def read(st, h, col, sc):
    global b
    for _ in range((len(st)//2)-1):
        pygame.draw.line(sc, col, [st[b], st[b+1]], [st[b+2], st[b+3]], h)
        b = b+2
    b = 0
    return st, b, h, col, sc
def gggY(num, st):
    global b
    num = []
    for _ in range((len(st)//2)-1):
        num.append(st[b+1][1])
        b = b+2
    b = 0
    return num
def gggX(num, st):
    global b
    num = []
    for _ in range(len(st)//2):
        num.append(st[b][0])
        b = b+2
    b = 0
    return num
def r2(file, via, st, body):
    global b
    st = [int(line.strip()) for line in file]
    for _ in range((len(st)//2)):
        body.append(via[0]+st[b])
        body.append(via[1]+st[b+1])
        b = b+2
    b = 0
    return body, via, file
def r3(body, st, via):
    global b
    for _ in range((len(st)//2)):
        body.append(via[0]+st[b])
        body.append(via[1]+st[b+1])
        b = b+2
    b = 0
    return body, via
def r4(body, st, via):
    global b
    for _ in range(len(st)):
        body.append(via+st[b])
        b = b+1
    b = 0
    return body, via, st
def r5(body, st, via):
    global b
    for _ in range(len(st)):
        body.append(st[b]-via)
        b = b+1
    b = 0
    return body, via, st
def r6(body, st):
    global b
    for _ in range(len(st)):
        body.append(st[b])
        b = b+1
    b = 0
    return body, st
def r7(body, st, via):
    global b
    for _ in range(len(st)):
        body.append(via+st[b])
        b = b+1
    b = 0
    return body, via, st
def r_r(body, st, via):
    global b
    for _ in range(len(st)):
        body.append(np.random.randint(-via, via+1)+st[b])
        b = b+1
    b = 0
    return body, st, via
def r_r2(body, st, via):
    global b
    for _ in range(len(st)):
        body.append(np.random.randint(-via, 0)+st[b])
        b = b+1
    b = 0
    return body, st, via
def pread(st, col, sc):
    pygame.draw.polygon(sc, col, st, width=0)
    return st, col, sc
def convert(st, st2, cou):
    global b
    for _ in range((len(st)//2)):
        cou = [st[b], st[b+1]]
        st2.append(cou)
        b = b+2
    b = 0
    return st2
def ejc(ind, wind):
    global c
    for _ in range(len(wind)):
          ind = ind+wind[c]
          c = c+1
    c = 0
    return ind
def pr(body, st, via):
    global b
    for _ in range(len(st)):
        body.append(via+st[b][0])
        b = b+1
    b = 0
    return body, via, st
class count:
    def __init__(self, sc, num):
        self.sc = sc
        self.num = num
    def draw(self):
        pygame.draw.rect(sc, (255, 0, 0), (0, 40, self.num, 40))
class reader:
    def __init__(self, sc, f, x, y):
        global b
        self.sc = sc
        self.sr = int(np.mean(np.array(f["store"])))
        for _ in range(len(f["store"])):
            f["store"][b][0] = f["store"][b][0]-self.sr
            f["store"][b][1] = f["store"][b][1]-self.sr
            b = b+1
        b = 0
        for _ in range(len(f["store"])):
            f["store"][b][0] = f["store"][b][0]+x
            f["store"][b][1] = f["store"][b][1]+y
            b = b+1
        b = 0
        self.f = f
        self.data = f
        self.stog = self.data["store"]
        self.numb = {'X': np.mean(np.array(gggX(0, f["store"]))),
                     'Y': np.mean(np.array(gggY(0, f["store"])))}
        b = 0
    def draw(self):
        reader.polygon(self)
        reader.polygon_shadow(self)
        reader.line(self)
    def polygon(self):
        pygame.draw.polygon(self.sc, self.data["color"], self.stog, width=0)
    def polygon_shadow(self):
        global st, b
        for _ in range(len(self.stog)):
            if self.stog[b][1]>self.numb['Y']:
                st.append(self.stog[b])
            b += 1
        pygame.draw.polygon(self.sc, self.data["shadow"], st, width=0)
        st = []
        b = 0
    def line(self):
        pygame.draw.polygon(self.sc, self.data["color"], self.stog, width=5)
    def namste_1(self):
        global c, cou, b
        self.data = self.f
        self.stog = self.data["store"]
        for _ in range(len(self.data["store"])):
            cou = np.random.randint(0, len(self.data["winds_min"])-1)
            if b==2:
                b = 0
                self.stog[c][0] = self.data["store"][c][0]+self.data["winds_min"][cou]
            c = np.random.randint(0, len(self.data["store"]))
            b = b+1
        c = 0
        b = 0
        cou = 0
    def namste_2(self):
        global c, cou, b
        self.data = self.f
        self.stog = self.data["store"]
        for _ in range(len(self.data["store"])):
            cou = np.random.randint(0, len(self.data["winds_min"])-1)
            if b==2:
                b = 0
                self.stog[c][1] = self.data["store"][c][1]-self.data["winds_min"][cou]
            c = np.random.randint(0, len(self.data["store"]))
            b = b+1
        c = 0
        b = 0
        cou = 0
    def namste_3(self):
        global c, cou, b
        self.data = self.f
        self.stog = self.data["store"]
        for _ in range(len(self.data["store"])):
            cou = np.random.randint(0, len(self.data["winds_min"])-1)
            if b==2:
                b = 0
                self.stog[c][1] = self.data["store"][c][1]+self.data["winds_min"][cou]
            c = np.random.randint(0, len(self.data["store"]))
            b = b+1
        c = 0
        b = 0
        cou = 0
    def namste_4(self):
        global c, cou, b
        self.data = self.f
        self.stog = self.data["store"]
        for _ in range(len(self.data["store"])):
            cou = np.random.randint(0, len(self.data["winds_min"])-1)
            if b==2:
                b = 0
                self.stog[c][0] = self.data["store"][c][0]-self.data["winds_min"][cou]
            c = np.random.randint(0, len(self.data["store"]))
            b = b+1
        c = 0
        b = 0
        cou = 0
