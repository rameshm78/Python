p = 0
n = int(input("Enter a number: "))
if n == 1:
    p = 0
else:
    for a in range(2,(n-1)):
        if n%a != 0:
            p = 1
            continue
        else:
            p = 0
            break
if p == 0:
    print(n, " is not Prime")
else:
    print(n, " is a Prime")

input("Press Enter to exit")
