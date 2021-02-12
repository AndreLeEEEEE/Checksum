import hashlib

name = input("Enter the file name with its extension: ")
with open(name, 'r') as file:  # Open up the generating file
    with open(name + " - Checksum.txt", 'w') as new:  # Create or open the output file
        for line in file:  # Go line by line
            rawLine = line.strip()  # Remove the terminating character from a line
            sha_256 = hashlib.sha3_256()  # Get the hash ready
            sha_256.update(rawLine.encode())  # Convert the line to bytes and put in hash function
            new.write(sha_256.hexdigest() + "\n")  # Write the new line in hex form to a new file