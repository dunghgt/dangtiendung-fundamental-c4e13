from random import *

loop_continue = True
while True:
    x = randint(0, 10)
    y = randint(1, 10)
    opers = ['*', '+', '-', '/']
    oper = choice(opers)

    if oper == '*':
        a = x * y
    elif oper == '+':
        a = x + y
    elif oper == '-':
        a = x - y
    elif oper == '/':
        if y == 0:
            print('nana')
        else:
            a = x / y

    error = randint(-1, 1)
    a_rand = a + error

    def generate_quiz():
        # Hint: Return [x, y, op, result]
        return [x, y, oper, a_rand]

    def check_answer(x, y, oper, a_rand, user_choice):
        if error == 0:
            if user_choice:
                return True
            else:
                return False
                loop_continue = False
        else:
            if user_choice:
                return False
                loop_continue = False
            else:
                return True
