

line_count = 0
word_count = 0
char_count = 0

with open("examples.txt", "r") as file:
    for line in file:
        print(line.strip()) #print the exaple.txt content
        line_count += 1 #add an int every time it passes a line
        word_count += len(line.split()) #adds +1 everytime it passes a word every loop
        char_count += len(line.strip()) # adds +1  every time it passes letters/characters in the file every loop

print(f"\nTotal number of lines: {line_count}")
print(f"Total number of words: {word_count}")
print(f"Total number of characters: {char_count}")
    







    