a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
overlap = []
for x in a:
    for y in b:
        if x == y:
            if x not in overlap:
                overlap.append(x)

print(overlap)
input ("Press Enter key to exit")