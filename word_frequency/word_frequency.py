with open('words.txt', 'r') as file:
    text = file.read()


words = text.split()
word_count = {}


for word in words:
    word = word.lower()  
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


with open('word_frequencies.txt', 'w') as file:
    for word, count in word_count.items():
        file.write(f"{word}: {count}\n")
