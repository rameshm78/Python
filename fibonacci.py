count = int(input("Enter the length of the fibonacci series: "))
if count == 0:
    fib = []
elif count == 1:
    fib = [1]
elif count == 2:
    fib = [1,1]
elif count > 2:
    fib = [1,1]
    for i in range (1,count-1):
        fib.append(fib[i] + fib[i-1])
print(fib)

input ("Press Enter key to exit")