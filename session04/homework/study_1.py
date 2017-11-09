n = input("Nhap vao doan van ban: ")
n = n.lower()

letter_count = {}

for letter in n:

    if letter != " ":
        letter_count[letter] = letter_count.get(letter, 0) + 1
    
letter_items = list(letter_count.items())

letter_items.sort()

for i in letter_items:
    print(*i)
