items = ["T-Shirt", "Sweater"]
print("     My shop: ", *items)

loop_continue = True

while loop_continue:
    crud = input("Wellcome to shop, What do you want (C, R, U, D) ? ")
    crud = crud.upper()
    #Create
    if crud == "C":
        new_item = input("Enter new item: ")
        items.insert(len(items) + 1, new_item)
    #Read
    elif crud == "R":
        pass
    #Update
    elif crud == "U":
        press = input("Press P to update position, I to update item: ")
        if press.upper() == "P":
            p = int(input("Update position: "))
            p = p - 1
            if p < len(items):
                new_item = input("New item: ")
                items[p] = new_item
            else:
                print("Position wrong~")
        elif press.upper() == "I":
            i = input("Update item: ")
            if i in items:
                new_item = input("new item: ")
                items.insert(items.index(i), new_item)
                items.remove(i)
            else:
                print("Item not found~")
    #Delete
    elif crud == "D":
        press = input("Press P to delete position, I to delete item: ")
        if press == "p":
            p = int(input("Delete position: "))
            p = p - 1
            if p < len(items):
                del items[p]
            else:
                print("Position wrong~")
        elif press == "i":
            i = input("Delete item: ")
            if i in items:
                items.remove(i)
            else:
                print("Item not found~")
    print("     My shop: ", *items)
    yesno = input("Wanna more? (Y/N)")
    if yesno.upper() == "Y":
        pass
    else:
        loop_continue = False
