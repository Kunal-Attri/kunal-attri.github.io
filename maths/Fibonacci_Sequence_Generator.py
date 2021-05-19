def into_integer(x, msg='Cannot be converted into a integer'):
    try:
        x = int(x)
    except ValueError:
        print(msg)
    else:
        return x


terms = get_integer('No of terms: ')
prev_first = 0
prev_second = 1

print(prev_first)
print(prev_second)

while 2 < terms:
    new = prev_second + prev_first
    prev_first = prev_second
    prev_second = new
    print(new)
    terms -= 1

input("Press enter to exit...")
