with open('file1.txt', 'r') as file1:
    content1 = file1.read()


with open('file2.txt', 'r') as file2:
    content2 = file2.read()


merged_content = content1 + '\n' + content2


with open('merged.txt', 'w') as merged_file:
    merged_file.write(merged_content)
