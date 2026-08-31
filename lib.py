# -*- coding: cp1251 -*-
import pygame
import numpy as np
import json
b = 0
c = 0
cou = 0
def read(st, h, col, sc):
    global b
    for _ in range((len(st)//2)-1):
        pygame.draw.line(sc, col, [st[b], st[b+1]], [st[b+2], st[b+3]], h)
        b = b+2
    b = 0
    return st, b, h, col, sc
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
def pr(body, st, via):
    global b
    for _ in range(len(st)):
        body.append(via+st[b][0])
        b = b+1
    b = 0
    return body, via, st
class reader:
    def __init__(self, sc, f):
        self.sc = sc
        self.f = f
        self.data = f
        self.stog = self.data["store"]
    def polygon(self):
        pygame.draw.polygon(self.sc, self.data["color"], self.stog, width=0)
    def namste_В(self):
        global c, cou
        self.data = self.f
        self.stog = self.data["store"]
        for _ in range(len(self.data["store"])):
            cou = np.random.randint(0, len(self.data["winds"])-1)
            self.stog[c] = [self.data["store"][c][0]+self.data["winds"][cou],
                            self.data["store"][c][1]]
            c = c+1
        c = 0
        cou = 0
    def namste_З(self):
        global c, cou
        self.data = self.f
        self.stog = self.data["store"]
        for _ in range(len(self.data["store"])):
            cou = np.random.randint(0, len(self.data["winds"])-1)
            self.stog[c] = [self.data["store"][c][0]-self.data["winds"][cou],
                            self.data["store"][c][1]]
            c = c+1
        c = 0
        cou = 0
    def namste_Ю(self):
        global c, cou
        self.data = self.f
        self.stog = self.data["store"]
        for _ in range(len(self.data["store"])):
            cou = np.random.randint(0, len(self.data["winds"])-1)
            self.stog[c] = [self.data["store"][c][0],
                            self.data["store"][c][1]-self.data["winds"][cou]]
            c = c+1
        c = 0
        cou = 0
    def namste_С(self):
        global c, cou
        self.data = self.f
        self.stog = self.data["store"]
        for _ in range(len(self.data["store"])):
            cou = np.random.randint(0, len(self.data["winds"])-1)
            self.stog[c] = [self.data["store"][c][0],
                            self.data["store"][c][1]+self.data["winds"][cou]]
            c = c+1
        c = 0
        cou = 0
