from random import choice

words = ['rum','gin','vodka']

c = choice(words)

ls_ = []
for i in range(len(c)):
    ls_.insert(i, '_ ')
print(*ls_)

ls_c = list(c)

count = 0
loop_continue = True

while loop_continue:
    gs = input("Guess a character? ")

    if gs in ls_c:

        for i in range(len(c)):
            if gs == ls_c[i]:
                ls_[i] = ls_c[i]

    else:
        count += 1

        if count == 1:
            print(
            """
             ----------
             |        O
             |
             |
             |
            _|_
            """
            )
        elif count == 2:
            print(
            """
             ----------
             |        O
             |        |
             |
             |
            _|_
            """
            )
        elif count == 3:
            print(
            """
             ----------
             |        O
             |       -|
             |
             |
            _|_
            """
            )
        elif count == 4:
            print(
            """
             ----------
             |        O
             |       -|-
             |
             |
            _|_
            """
            )
        elif count == 5:
            print(
            """
             ----------
             |        O
             |       -|-
             |       /
             |
            _|_
            """
            )
        elif count == 6:
            print(
            """
             ----------
             |        O
             |       -|-
             |       / \\
             |
            _|_
            """
            )
            print("you lose~")
            loop_continue = False
    print(*ls_)
    if ls_ == ls_c:
        print("Winn ne`")
        loop_continue = False
