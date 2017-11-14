numbers = [-1, 0, 10, -100, 300]

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
            if numbers[i] > numbers[j]:
                a = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = a
print(*numbers)
