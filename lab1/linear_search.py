numbers = [0, 1, 7, -1, 10]

n = int(input("Nhap vao 1 so: "))

# for i, j in enumerate(numbers):
#     if n == j:
#         print("Tim thay {0} o vi tri {1}".format(n, i))
#         break
#     elif i == len(numbers) - 1:
#         print("not found")

found_index = -1
for i, j in enumerate(numbers):
    if x == number:
        found_index = i
        break

if found_index == -1:
    print("not found")
else:
    print("found: ", found_index)
