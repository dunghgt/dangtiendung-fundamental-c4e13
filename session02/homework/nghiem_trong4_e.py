h = int(input("Nhap so hang: "))
c = int(input("Nhap so cot: "))

for i in range(h):
    if i % 2 == 0:
        for j in range(c):
            if j % 2 == 0:
                print("X", end='')
            else:
                print("*", end='')
        print( )
    else:
        for j in range(c):
            if j % 2 == 0:
                print("*", end='')
            else:
                print("X", end='')
        print( )
