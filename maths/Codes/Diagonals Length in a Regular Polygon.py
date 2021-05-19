from math import ceil, cos, pi

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


while True:
    n = get_integer("No of sides: ")
    a = get_float("Each side length: ")
    diagonals = [a]
    d = n - 3

    if d % 2 == 0:
        temp = -1
    else:
        temp = -2

    for i in range(d):
        if i + 1 <= ceil(d / 2):
            value = (diagonals[-1] * cos(pi / n)) + (diagonals[0] * cos((i + 1) * pi / n))
        else:
            value = diagonals[temp]
            temp -= 2
        diagonals.append(round(value, 3))

    for i in range(1, len(diagonals)):
        print(f"Diagonal {i} = {diagonals[i]}")
    print()





























