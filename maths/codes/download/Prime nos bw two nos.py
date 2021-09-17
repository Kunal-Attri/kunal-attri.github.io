def get_integer(msg="Number: ", wrng_msg="Invalid Input"):
    try:
        i = int(input(msg))
    except ValueError:
        print(wrng_msg)
        return get_integer(msg, wrng_msg)
    else:
        return i

def isodd(num):
    odd = True
    if num % 2 == 0:
        odd = False
    return odd


def iseven(num):
    even = True
    if num % 2 != 0:
        even = False
    return even


def isprime(num):
    prime = True
    if iseven(num) and num / 2 != 1:
        prime = False
    if isodd(num):
        for i in basic_prime:
            if num % i == 0 and num / i == 1:
                break
            elif num % i == 0 and num / i != 1:
                prime = False
        if prime:
            for i in range(101, int(math.sqrt(num) + 1), 2):
                if num % i == 0:
                    prime = False
                    break
    return prime


from time import time

while True:
    ini_no = get_integer('Initial no: ')
    final_no = get_integer('Final no: ')
    
    total = 0
    print(f'Prime no.s in range from {ini_no} to {final_no} are: ')
    a = time()
    for i in range(ini_no, final_no + 1):
        if isprime(i) and i != 1:
            #print(i)
            total += 1
    if total == 0:
        print('None')
    else:
        print(f"Total = {total}")
    print(f"Time = {time() - a}\n")
        
    print('')
    if input("Wanna quit?(y/n): ") == 'y':
        break
