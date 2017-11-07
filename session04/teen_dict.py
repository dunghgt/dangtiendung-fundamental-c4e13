teen_dict = {
    'r': 'roi',
    'bt': 'biet',
    'ny': 'nguoi yeu',
    'h': 'gio',
    'hc': 'hoc'
}

loop_continue = True

while loop_continue:
    print("* " * 25)
    print(*teen_dict)
    n = input("Wanna search? ")
    if n in teen_dict:
        print("translation: ", teen_dict[n])
    elif n.lower() == "not thing" and "no" and "n":
        print("bye bye~")
        loop_continue = False
    else:
        yesno = input("Not found, do you want to contribute this word? (Y/N)")
        if yesno.lower() == "y":
            y = input("meaning:")
            teen_dict[n] = y
        else:
            print("bye bye~")
            loop_continue = False
