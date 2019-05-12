import time

name = input("What is your name? ")
age = int(input("How old are you? "))
print("You're ", age, "years old.")

now = int(time.strftime("%Y"))

ost = int((100 - age))
yr = now + ost
print(name, " you will be 100 years old in", yr)

input ("Press Enter key to exit")