import random
a = random.randint(1,9)
b = int(input("Enter a number: "))
if a>b:
    print("You guessed too low. The number was %d" % a)
elif a == b:
    print("You guessed correct, the number was indeed %d" % a)
elif a<b:
    print("You guessed too high. The number was %d" % a)

input("Press Enter to Exit")