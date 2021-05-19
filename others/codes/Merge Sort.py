# Merge Sort
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

def merge_sort_step(arr):
    global tempmax, x, temp
    if len(arr) > 1:

        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort_step(L)
        merge_sort_step(R)
        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
        
def animate(i):
    global x, raw
    raw = merge_sort_step(raw)
    for bar in ax.containers:
        bar.remove()
    return plt.bar(x,raw, color='cornflowerblue')
    

anim= ani.FuncAnimation(fig,animate,frames=100,
                             interval=50)
plt.grid(True)
plt.show()
