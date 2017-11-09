f_alice = open("D:\\code\\techkids\\fundmental\\session04\\homework\\AAIW.txt", "r")
alice_words = f_alice.read()
f_alice.close()

alice_words = alice_words.lower()

for letter in "!()_-:;,.?*0123456789\"\`\'[]":
    alice_words = alice_words.replace(letter, ' ')

words_count = {}

for i in alice_words.split():
    words_count[i] = words_count.get(i, 0) + 1

words_items = list(words_count.items())

words_items.sort()


file_word = "D:\\code\\techkids\\fundmental\\session04\\homework\\alice_words.txt"
open(file_word, "a")
f = open(file_word, "w")

f.write("{:15}{:3}\n".format("word", "count"))
f.write("====================\n")

for (i, j) in words_items:
    f.write("{:15}{:3}\n".format(i, j))

    alice_dict = dict(words_items)

if "alice" not in alice_dict.keys():
    alice_dict["alice"] = 0
f.write("{0}{1}".format("Alice occur in the book: ", alice_dict["alice"]))

f.close()
