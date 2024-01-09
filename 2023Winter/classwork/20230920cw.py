# Creating and writing to a file

#filename = "filename.txt"

#file = open(filename, "w") # "w" is the mode to open the file in. All options are "w", "a" and "r".
                            # Representing "write"(create a new file), "append"(add onto existing file) and "read"(read from the file).
                            # By adding a "b" after the mode used(like "wb"), the file will be opened in binary.
#file.close()

# Another way:

#with open(filename, "w") as file: # With this way, you dont need file.close to close the file after use.
    
    #file.write("string")

# Example:

fileName = "test_0.txt"

with open(fileName, "wb") as file: # Create and open the file "test_0.txt" in binary.

    for number in range(65, 68): # Loop through 65, 66 and 67.

        file.write(bytes([number])) # Write the current number into "test_0.txt" in binary.

        print(f"Added {bytes([number])} to {fileName}.\n")

with open(fileName, "rb") as file: # Read from the created file "test_0.txt" in binary.

    for letterBin in (file.readline()): # Loop through all letters in the first line of "test_0.txt".

        print(f"Read binary {letterBin}(which is {bytes([letterBin])}) from {fileName}.\n")

# Difference between read(), readline() and readlines()

charDrawingName = "charDrawing_0.txt" # Change between "charDrawing_0.txt", "charDrawing_1.txt" and "charDrawing_2.txt" 

with open(charDrawingName, "r", encoding = "utf8") as drawing:

    for line in drawing:

        print(line, end = "")