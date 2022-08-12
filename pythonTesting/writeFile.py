# Read the file and store all the lines in the list
# Reverse the list
# Write the list back to the file

with open('test.txt', 'r') as reader:
    content = reader.readlines()
    w = reversed(content)
    with open('test.txt', 'w') as writer:
        for line in w:
            writer.write(line)