import random
len = int(input("Enter the length of required password: "))
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
p = "".join(random.sample(s,len))
print("Password is: "+p)

input("Press Enter to exit")    