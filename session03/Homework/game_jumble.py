from random import choice

s = "proud"
characters = list(s)
for i in range(len(characters)):
    c = choice(characters)
    print(c, end=' ')
    characters.remove(c)
print( )

loop_continue = True
while loop_continue:
    guess = input("Doan la chi? ")
    if guess == "proud":
        print("bingo~")
        loop_continue = False
    else:
        print("em sai r~")
