
strings = ["This is the first string", "Second string", "Third string", "And so on..."]


with open("strings.txt", "w") as file:
    for string in strings:
        file.write(string + "\n")

        print(string)