# menu = []
# print(menu)
#
# menu = ['chan ga sa ot']
# print(menu)

menu = ['chan ga sa ot', 'ga xao pho mai', 'com rang dua bo']
print(*menu, sep=', ') #separator

continue_21 = True
while continue_21:
    n = input("Nhap mon moi:")
    menu.append(n)
    print(*menu, sep=', ')
