a = 0
h = 0
def anim(anim, uu):
    global a
    a += 1
    if a==len(anim):
        a = 0
    uu['text'] = anim[a]
    return uu, anim
def save(item, st):
    st.append(str(item))
    return item, st
def save_list(lis, st):
    global h
    for _ in range(len(lis)):
            st.append(str(lis[h]))
            h = h+1
    h = 0
    return lis, st, h
def save_game(file, st):
    for index in st:
        file.write(index + '\n')
    return file, st
