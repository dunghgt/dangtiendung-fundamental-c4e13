n = input("Phep tinh: ")

n_ls = []
for i in n.split():
    n_ls.append(i)

if n_ls[1] == '*':
    a = n_ls[0] * n_ls[2]
elif n_ls[1] == '/':
    a = n_ls[0] / n_ls[2]
elif n_ls[1] == '+':
    a = n_ls[0] + n_ls[2]
elif n_ls[1] == '-':
    a = n_ls[0] - n_ls[2]

print(*n_ls, '=', a)
