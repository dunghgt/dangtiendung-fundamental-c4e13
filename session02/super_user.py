
while True:
    us =input("Nhap username: ")

    if us.upper() == "C4E":
        pas = input("Nhap password: ")
        if pas == "hihi":
            print("chinh xac")
        else:
            print("password sai")
    else:
        print("User not found~")
