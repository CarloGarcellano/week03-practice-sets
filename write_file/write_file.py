
#create
with open("source.txt", "w") as file:
    file.write("hello, world!\n")
    
#append
with open("source.txt", "a") as file:
    file.write("this is appended text.\n") 

#get content of src_text
with open("source.txt", "r") as source_txt:
    content = source_txt.read()

#copy content to destination.txt
with open("destination.txt", "w") as destination_file:
    destination_file.write(content)

   
