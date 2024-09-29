# File Handling
#1. How to read a text, and write into it using Python code.
#2. open("file_name", "mode")
#3. mode - 'r' for reading (default)
#4. 'w' for writing (creates a new file or truncates an existing one.
#5. 'a' for appending.
#6. 'b' for binary mode. zoom.exe - binary
#7. '+' for updating (reading & writing)

# Read and Write content

# Read a file
# Reading entire content = file_object.read()
# line = file_object.readline() for a single line
# lines = file_object.readlines() for all lines in a list.
# close the file

file = open('Toshi.txt', 'r')
content = file.read()
print(content)