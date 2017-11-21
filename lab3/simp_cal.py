def eval(x, y, oper):
    if oper == '*':
        a = x * y
    elif oper == '+':
        a = x + y
    elif oper == '-':
        a = x - y
    elif oper == '/':
        if y == 0:
            print('Nah')
        else:
            a = x / y
    return a

# x1 = 10
# y2 = 5
# oper3 = '+'
# r = eval(x1, y2, oper3)
# print(r)
# s = eval()
#
#
# x = int(input("x = "))
# oper = input("Operation(+, -, *, /): ")
# y = int(input("y = "))
#
# if oper in ['+', '-', '*', '/']:
#     r = eval()
#
#     print(r)
# else:
#     print('Operation not found!')
