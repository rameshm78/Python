a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [int(i) for i in a if i in b]
print(c)
d = []
d.append(set(a).intersection(b))
print(d)
e=[]
e.append(set(a) & set(b))
print(e)

result = [x for x in set(a) if x in b]
print(result)

input("Press Enter to exit")