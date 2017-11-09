f_alice = open("D:\\code\\techkids\\fundmental\\session04\\homework\\AAIW.txt", "r")
alice_words = f_alice.read()
f_alice.close()

alice_words = alice_words.lower()

for letter in "!()_-:;,.?*0123456789\"\`\'[]":
    alice_words = alice_words.replace(letter, ' ')

words_count = {}

longget_word = ""

for i in alice_words.split():
    if len(i) > len(longget_word):
        longget_word = i

count = 0

for i in longget_word:
    count += 1

print("Longget word: ", longget_word)
print("And it have: {0} characters".format(count))
