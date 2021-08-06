def get_integer(msg="Number: ", wrng_msg="Invalid Input"):
    try:
        i = int(input(msg))
    except ValueError:
        print(wrng_msg)
        return get_integer(msg, wrng_msg)
    else:
        return i

def find_hcf(numbers):
    smaller = min(numbers)
    for i in range(smaller, 0, -1):
        hcf = True
        for j in numbers:
            if j % i != 0:
                hcf = False
                break
        if hcf:
            return i
        

print("""
To calculate HCF of numbers, type the numbers with spaces between them,
like '12 14 8'
""") 
x = input("Numbers: ").split()
n = [int(i) for i in x]
hcf = find_hcf(n)
print(f"HCF of {n} is {hcf}")
print()
input("Press enter to exit...")
