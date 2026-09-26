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
def Y(num, st):
    global b
    num = []
    for _ in range((len(st)//2)-1):
        num.append(st[b+1][1])
        b = b+2
    b = 0
    return num
def X(num, st):
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

class draw:
    @classmethod
    def polygon(cls, sc, obj):
        global b
        for _ in range(len(obj.data["store"])):
            pygame.draw.polygon(sc, obj.data["color"][b], obj.data["store"][b], width=0)
            b = b+1
        b = 0
    @classmethod
    def line(cls, sc, obj, col):
        global b
        for _ in range(len(obj.data["store"])):
            pygame.draw.polygon(sc, col, obj.data["store"][b], width=3)
            b = b+1
        b = 0
    @classmethod
    def polygon_shadow_1(cls, sc, obj):
        global st, b, c
        for _ in range(len(obj.data["store"])):
            for _ in range(len(obj.data["store"][b])):
                if obj.data["store"][b][c][0]<int(obj.numb[b]['X']):
                    st.append(obj.data["store"][b][c])
                c = c+1
                pygame.draw.polygon(sc, obj.data["shadow"][b], st, width=0)
                print(obj.numb[b]['X'])
            st = []
            b += 1
            c = 0
        b = 0
        c = 0
        st = []
    @classmethod
    def namste_1(cls, obj):
        global c, cou, b
        c = 0
        cou = 0
        obj.data = obj.f
        obj.stog = obj.data["store"]
        for _ in range(len(obj.data["store"])):
            for _ in range(len(obj.data["store"][b])):
                cou = np.random.randint(0, len(obj.data["winds_min"])-1)
                obj.data["store"][b][c][0] = obj.data["store"][b][c][0]+obj.data["winds_min"][cou]
                obj.data["store"][b][c][1] = obj.data["store"][b][c][1]+obj.data["winds_min"][cou]
                c = c+1
            c = 0
            b = b+1
        c = 0
        b = 0
        cou = 0
        return obj
    @classmethod
    def retr(cls, obj, file, x, y):
        global c, b, cou
        with open(file, 'r', encoding="utf-8") as f:
              cou = json.load(f)
        obj = Object(cou, x, y)
        if obj.data["store"]==cou["store"]:
            print(f'True')
        else:
            print(f'False')
        cou = 0
        return obj
class Object:
    def __init__(self, f, x, y):
        global b, c
        self.f = f
        self.data = f
        self.color = f["color"]
        self.numb = []
        for i in f["store"]:
            self.numb.append({'X': np.mean(np.array(f["store"][b])),
            'Y': np.mean(np.array(f["store"][b]))})
            b += 1
        b = 0
        c = 0
