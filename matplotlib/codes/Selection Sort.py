# Selection Sort
from random import shuffle, randint
import matplotlib.pyplot as plt
import matplotlib.animation as ani

raw = [randint(0, 100) for i in range(101)]
shuffle(raw)
x = [i for i in range(101)]

temp = 0
tempmax = len(raw)

fig, ax=plt.subplots()
ax.set_xlim(-1, 101)

def selection_sort_step():
    global temp, raw
    if temp < tempmax:
        min_id = temp
        for j in range(temp+1, tempmax):
            if raw[min_id] > raw[j]:
                min_id = j
        raw[temp], raw[min_id] = raw[min_id], raw[temp]
        temp+=1
        for bar in ax.containers:
            bar.remove()
        return plt.bar(x,raw, color='cornflowerblue')


def animate(i):
    global x, raw
    return selection_sort_step()

anim= ani.FuncAnimation(fig,animate,frames=100,
                             interval=100,repeat=False)
plt.grid(True)
plt.show()
