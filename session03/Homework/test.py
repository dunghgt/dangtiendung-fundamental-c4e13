sizes = [5, 7, 300, 45, 52, 69]

for (i, j) in enumerate(sizes):
    j1 = j + 50
    sizes.remove(j)
    sizes.insert(i, j1)
print("After one month, their size increased: ", sizes)
