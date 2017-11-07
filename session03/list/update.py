menu = ['bun', 'cha', 'com']
for index, item in enumerate(menu):
    print(index + 1, item, sep='. ')

n = int(input("position you want to replace? "))
remove_item = input("replace with: ")

menu[n - 1] = remove_item

for index, item in enumerate(menu):
    print(index + 1, item, sep='. ')
