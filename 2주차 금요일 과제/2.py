x = int(input("enter integer: "))

count = 0
while x != 1:
    count += 1
    if x%3 == 0:
        x /= 3
    elif x%2 == 0:
        x /= 2
    else:
        x -= 1

print(count) 