n = int(input("Nhap n: "))

result = 0
for i in range(1, n + 1):
    result += 1/(i*i)

print("Ket qua la: ", result)
