# Selection Sort
from random import shuffle, randint
import matplotlib.pyplot as plt
import matplotlib.animation as ani

raw = [randint(0, 100) for i in range(101)]
shuffle(raw)
x = [i for i in range(101)]

tempmax = len(raw)
temp = 0

fig, ax=plt.subplots()
ax.set_xlim(-1, 101)

def insertion_sort_step():
    global tempmax, raw, x, temp
    if temp < tempmax:
        key = raw[temp]
        j = temp-1
        while j >= 0 and key < raw[j]:
            raw[j+1] = raw[j]
            j -= 1
        raw[j+1] = key
        temp += 1
    
    for bar in ax.containers:
        bar.remove()
    return plt.bar(x,raw, color='cornflowerblue')
            
        
def animate(i):
    global x, raw
    return insertion_sort_step()

anim= ani.FuncAnimation(fig,animate,frames=100,
                             interval=100)
plt.grid(True)
plt.show()
