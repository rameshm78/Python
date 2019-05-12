n = int(input("Enter a number: "))
def primo(n):
    p = 0
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
    return p
p = primo(n)
if p == 0:
    print(n, "is not Prime")
else:
    print(n, "is a Prime") 

input("Press Enter to exit")