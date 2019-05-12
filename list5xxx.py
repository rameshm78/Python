print("Welcome to the List Less Than 5 program..")
print("\nEnter a space separated list of numbers\n")
a=[int(i) for i in input().split()]
b=[int(j) for j in a if j<5]
print(b)
print("Another way")
print(set([x for x in a if x < 5]))

input ("Press Enter key to exit")