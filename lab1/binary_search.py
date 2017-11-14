numbers = [0, 1, 7, 9, 10]
n = int(input("Nhap n: "))



print(*numbers)

start = -1
stop = len(numbers)
# if n == numbers[start]

while True:
    a = (start + stop) // 2
    if n == numbers[a]:
        print("found n")
        break
    elif n < numbers[a]:
        stop = a
    elif n > numbers[a]:
        start = a
    # print(numbers[start], numbers[stop])

    if start == stop or start == stop -1:
        print("n not found~")
        break
