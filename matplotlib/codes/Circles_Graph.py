import matplotlib.pyplot as plt
from math import pi, cos, sin

def get_integer(msg="Number: ", wrng_msg="Invalid Input"):
    try:
        i = int(input(msg))
    except ValueError:
        print(wrng_msg)
        return get_integer(msg, wrng_msg)
    else:
        return i


def get_float(msg="Number: ", wrng_msg="Invalid Input"):
    try:
        f = float(input(msg))
    except ValueError:
        print(wrng_msg)
        return get_float(msg, wrng_msg)
    else:
        return f


print('''
1. First enter the no of circles you want to plot
2. Enter the radius of first circle
3. Enter the coordinates of its centres in the form "x y", for eg, '3 0'
4. Repeat steps 2 and 3 for the no of circles you want to plot.
''')
no = get_integer("No of circles to plot: ")
while no > 0:
    x = []
    y = []
        
    start = 0
    end = 2 * pi
    i = start
        
    radius = get_float("Radius: ")
    cx, cy = input("Centre coords: ").split()
    cx, cy = float(cx), float(cy)
    resolution = pi / 180

    while i < end + resolution:
        x.append(cx + radius * cos(i))
        y.append(cy + radius * sin(i))
        i += resolution
        

    plt.grid(True)
    plt.plot(x, y)
    plt.plot(cx, cy, "o")
    no -= 1

plt.title("Circles")
plt.show()
