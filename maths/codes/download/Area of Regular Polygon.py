from math import tan, pi

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


print("""
This code calculates the area of a given regular polygon. Please enter the no of sides and length of each side.
""")
while True:
    no_of_sides = get_integer("Sides: ")
    if no_of_sides > 2:
        side_length = get_float("Length: ")
        if side_length > 0:
            area = no_of_sides * (side_length ** 2) / (4 * tan(pi / no_of_sides))
            print(f"Area =  {area} square units")
        else:
            print('Length of a side cannot be negative')
    else:
        print('Polygon with less than 3 sides cannot be formed')
    print('')
