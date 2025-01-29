with open("find_replace.txt", "r") as file:
    content = file.read()

new_word = content.replace("old", "new")


with open("find_replace.txt", "w") as file:
    file.write(new_word)

