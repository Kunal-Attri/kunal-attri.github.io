from math import cos, pi

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
This code calculates the length of the shortest possible diagonal in a regular polygon
""")

while True:
    no_of_sides = get_integer("Sides: ", wrong_message="No of sides of a polygon can only be an integer like 3, 4, 5, "
                                                       "etc")
    if no_of_sides > 2:
        side_length = get_float("Length: ")
        if side_length >= 0:
            shortest_diagonal = 2 * side_length * cos(pi / no_of_sides)
            print(f"Shortest Diagonal = {shortest_diagonal} units")
        else:
            print('Length of a side cannot be less than 0')
    else:
        print('Polygon with less than 3 sides cannot be formed')
    print('')
