# Selection Sort
from random import shuffle, randint
import matplotlib.pyplot as plt
import matplotlib.animation as ani

raw = [randint(0, 100) for i in range(101)]
shuffle(raw)
x = [i for i in range(101)]

tempmax = len(raw)

fig, ax=plt.subplots()
ax.set_xlim(-1, 101)

def bubble_sort_step():
    global tempmax, raw, x
    
    for j in range(0, tempmax-1):
        if raw[j] > raw[j+1]:
            raw[j], raw[j+1] = raw[j+1], raw[j]
    for bar in ax.containers:
        bar.remove()
    return plt.bar(x,raw, color='cornflowerblue')
            
        
def animate(i):
    global x, raw
    return bubble_sort_step()

anim= ani.FuncAnimation(fig,animate,frames=100,
                             interval=100)
plt.grid(True)
plt.show()
