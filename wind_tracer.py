import random as rand
c = 0
b = 0
def numaa(st, f):
    global b
    for index in st:
         f = f+index
    f = f//len(st)
    print(f)
    for _ in range(len(st)):
         st[b] = st[b]-f
         b = b+1
    b = 0
    return st
def randlist(x, a, rb, rb2):
    global b
    for _ in range(200):
        b = rand.randint(0, rb2)
        a = rand.randint(0, rb)
        if b==5 or b==0:
             x.append(a)
    return x, a, b
def randlist2(st, a, rb, rb2, x):
    for _ in range(x):
         a = rand.randint(rb, rb2)
         rb = rb+10
         rb2 = rb2+12
         st.append(a)
    return st
def namste(st, x, a):
    global c
    for _ in range(len(st)):
        a = rand.randint(0, len(x)-1)
        st[c] = st[c]+x[a]
        c = c+1
    c = 0
    return st
def namste2(st, x, a):
    global c
    for _ in range(len(st)//2):
        a = rand.randint(0, len(x)-1)
        st[c] = st[c]+x[a]
        c = c+2
    c = 0
    return st
