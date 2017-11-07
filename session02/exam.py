n = int(input("Enter a number: "))

# for i in range(0, n, 2):
#     print(i, end=' ')

# for i in range(n):
#     if i % 2 == 0:
#         print(i, end=' ')

if (n % 2 == 0, n % 3 != 0):
    print("Fizz")
elif (n % 2 != 0, n % 3 == 0):
    print("Buzz")
elif (n % 2 == 0, n % 3 == 0):
    print("FizzBuzz")
