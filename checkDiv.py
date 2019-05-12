n = int(input("Enter a number: "))
divisor = []
for a in range(1,n):
    if n%a == 0:
        divisor.append(a)
print(divisor)

input ("Press Enter key to exit")