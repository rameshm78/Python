import datetime

name = input("What is your name? ")
age = int(input("How old are you? "))
print("You're ", age, "years old.")

now = datetime.datetime.now()
cyr = now.year

ost = int((100 - age))
yr = cyr + ost
print(name, " you will be 100 years old in", yr)

input ("Press Enter key to exit")