menu = ['chao', 'com', 'bun']
print(*menu, sep=', ')

n = input("Muon xoa chi?")

if n in menu:
    menu.remove(n)
    print(*menu, sep=', ')
else:
    print("menu khong co", n)
