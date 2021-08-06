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


from math import ceil

def find_lcm(numbers):
    divisors = {}
    for x in numbers:
        i = 2
        while x > 1:
            quantity = 0
            while x % i == 0:
                if isprime(i):
                    quantity += 1
                    x /= i
            if quantity > divisors.get(i, 0):
                divisors[i] = divisors.get(i, 0) + quantity
            i += 1

    lcm = 1
    for key, value in divisors.items():
        lcm *= (key ** value)
    return lcm


print("""
To calculate LCM of numbers, type the numbers with spaces between them,
like '12 14 8'
""") 
x = input("Numbers: ").split()
n = [int(i) for i in x]
lcm = find_lcm(n)
print(f"LCM of {n} is {lcm}")
print()
input("Press enter to exit...")    
