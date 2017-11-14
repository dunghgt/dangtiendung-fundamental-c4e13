numbers = [1, 6, 8 ,1, 2, 1, 5, 6]

n = int(input("Enter a number: "))

count = numbers.count(n)

if count == 0:
    print(n, "not found!!")

else:
    print("{0} appear(s) {1} time in my list~". format(n, count))
