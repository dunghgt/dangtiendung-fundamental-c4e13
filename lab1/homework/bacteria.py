b = int(input("How many B bacterias are there? "))

if b < 0:
    print("Number of B bacteria not found~~")

else:
    time = int(input("How much time in minutes will we wait? "))
    if time < 0:
        print("Time not found~~")

    else:
        total_b = b * (2 ** (time//2))
        print("After {0} minutes, we would have {1} B bacterias". format(time, total_b))
