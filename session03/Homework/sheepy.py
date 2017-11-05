#2.1
sizes = [5, 7, 300, 45, 52, 69]
print("Hello, these are my sheep sizes: \n", sizes)

total_size = 0
#2.5
n_month = int(input("Month?"))
for i in range(n_month):
    print("MONTH", i + 1)
    #2.2
    maxsize = 0
    for i in sizes:
        if i > maxsize:
            maxsize = i

    print("Now my biggest sheep has size ", maxsize, "lets shear it")

    #2.3
    psmax = sizes.index(maxsize)
    sizes.insert(psmax, 8)
    sizes.remove(maxsize)
    print("After shearing, here my flock: \n", sizes)

    total_size = total_size + maxsize
    #2.4
    for (i, j) in enumerate(sizes):
        j1 = j + 50
        sizes.remove(j)
        sizes.insert(i, j1)
    print("After one month, their size increased: \n", sizes)

#2.6
print("My flock has size in total: ", total_size)
print("I would get ", total_size, " * 2$ = ", total_size * 2, "$")
