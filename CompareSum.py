import hashlib

name = input("Enter the file name with its extension: ")

current_hash = []
with open(name, 'r') as file:  # Open up the generating file
    for line in file:  # Go line by line
        rawLine = line.strip()  # Remove the terminating character from a line
        sha_256 = hashlib.sha3_256()  # Get the hash ready
        sha_256.update(rawLine.encode())  # Convert the line to bytes and put in hash function
        current_hash.append(sha_256.hexdigest())  # Store hex value for later

with open(name + " - Checksum.txt", 'r') as file:  # Open up the original checksum file
    try:
        original_length = sum(1 for _ in file)  # Get the line amount for the original
        if original_length != len(current_hash):  # If the line amounts are unequal
            raise Exception  # The file was changed

        for index, line in enumerate(file):  # Go line by line
            rawLine = line.strip()  # Remove the terminating character from a line
            if rawLine != current_hash[index]:  # If lines don't match
                raise Exception  # The file was changed
        print("Clear: The checksum values match")
    except:
        print("Warning: The checksum values don't match")

# Cases for mismatched checksum values
# Case 1: Equals line amount
# Case 2: Current > Original
# Case 3: Current < Original