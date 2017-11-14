n = int(input("Month? "))

p1 = 0
p2 = 1

for i in range(n + 1):
    total_p = p1 + p2
    print("Month {0}: {1} pair(s) of rabbit".format(i, total_p))
    p1 = p2
    p2 = total_p
