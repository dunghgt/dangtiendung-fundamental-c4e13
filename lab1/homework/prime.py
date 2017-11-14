n = int(input("Enter a number: "))
n1 = n // 2

pri_num = True

if n < 2:
    print(n, "is not a prime number")
    pri_num = False

elif n == 2:
    pass

else:
    for i in range(2, n1 + 1):
        if n % i == 0:
            print(n, "is not a prime number")
            pri_num = False
            break

if pri_num == True:
    print(n, "is a prime number")
