from random import *
from simp_cal import eval

def generate_quiz():
    x = randint(0, 10)
    y = randint(0, 10)
    opers = ['*', '+', '-', '/']
    oper = choice(opers)
    if y == 0 and oper == '/':
        y = randint(1, 10)
    a = eval(x, y, oper)

    error = randint(-1, 1)
    a_rand = a + error
    # Hint: Return [x, y, op, result]
    return [x, y, oper, a_rand]

def check_answer(x, y, oper, a_rand, user_choice):
    if eval(x, y, oper) == a_rand:
        if user_choice:
            return True
        else:
            return False
    else:
        if user_choice:
            return False
        else:
            return True
