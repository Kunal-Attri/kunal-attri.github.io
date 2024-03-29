def get_integer(msg="Number: ", wrng_msg="Invalid Input"):
    try:
        i = int(input(msg))
    except ValueError:
        print(wrng_msg)
        return get_integer(msg, wrng_msg)
    else:
        return i

def factorial(num):
    return math.factorial(num)


print('''
This code calculates no of possible permutations and combinations. Kindly provide data as n and r
n: total no of items 
r: required no. of items
''')

while True:
    n = get_integer("n: ")
    r = get_integer('r: ')
    if n - r < 0:
        print('Invalid input, since n can never be less than r')
    else:
        perm = int(factorial(n) / factorial(n - r))
        comb = int(factorial(n) / (factorial(r) * factorial(n - r)))
        print(f'Possible permutations = {perm}')
        print(f'Possible Combinations = {comb}')
    print('')
