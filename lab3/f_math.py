from random import choice, randint
from simp_cal import eval

x = randint(0, 10)
y = randint(0, 10)
oper_ls = ['+', '-', '*', '/']
oper = choice(oper_ls)

a = eval(x, y, oper)

error = randint(-1, 1)
a_rand = a + error

print(x, oper, y, '=', a_rand)
n = input("y/n? ")
n = n.lower()

if a_rand == a:
    if n == 'y':
        print("bingo~")
    elif n == 'n':
        print("wrong~")
else:
    if n == 'n':
        print("bingo~")
    elif n == 'y':
        print("wrong~")
