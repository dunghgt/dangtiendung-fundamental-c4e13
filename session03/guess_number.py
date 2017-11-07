import random

n = random.randrange(1, 100)

loop_continue = True
while loop_continue:
    gn = int(input("Guess number: "))
    if gn < n:
        print("Too small")
    elif gn > n:
        print("Too big")
    else:
        print("biggo")
        loop_continue = False
