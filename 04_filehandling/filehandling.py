# Write to File
file = open("example.txt", "w")
file.write("This file is being written from python code\n\n")
file.write("Learning Python is fun !!")
file.close()

#Read from File
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# using "with" keyword
with open("example.txt","r") as f:
    for line in f:
        print(line.strip())