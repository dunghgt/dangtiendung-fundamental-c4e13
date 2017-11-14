numbers = [1, 6, 8 ,1, 2, 1, 5, 6]

n = int(input("Enter a number: "))

count = 0

for i in numbers:
    if n == i:
        count += 1

if count == 0:
    print(n, "not found!!")

else:
    print("{0} appear(s) {1} time in my list~". format(n, count))
