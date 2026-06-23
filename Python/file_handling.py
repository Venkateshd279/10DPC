# File Handling in Python
# How to write file, read file, create file, delete file, append file in Python

# Mode "W" - Write mode: Creates a new file or overwrites an existing file.
# Mode "R" - Read mode: Opens a file for reading (default mode).
# Mode "A" - Append mode: Opens a file for appending new content at the end of the file.


# 1. Writing to a file and overwriting existing content
with open("myfile.txt", "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("Hello, this is another line.\n")

print("File written successfully.")

# 2. Appending to a file
with open("myfile.txt", "a") as file:
    file.write("\nThis line is appended to the file.\n")

print("Content appended successfully.")

# 3. Reading from a file
with open("myfile.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# key points to remember about file handling in Python:
# 1. Use the open() function to open a file in the desired mode.
# 2. Use the write() method to write content to a file.
# 3. Use the read() method to read content from a file.
# 4. Use the close() method to close the file after operations are complete.