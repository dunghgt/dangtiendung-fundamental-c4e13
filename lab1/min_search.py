numbers = [1, 7, 8, -10, 50, -100, 20]

min_num = numbers[0]
max_num = numbers[0]
for i in numbers:
    if min_num > i:
        min_num = i
    if max_num < i:
        max_num = i
print("min:", min_num)
print("max:", max_num)
