import hashlib
import sys

try:
    name = input("Enter the file name with its extension: ")
    with open(name, 'rb') as file:  # Open up the generating file
        name = name.split('.')
        name.pop()
        name = '.'.join(name)
        with open(name + " - Checksum.txt", 'w') as new:  # Create or open the output file
            sha_256 = hashlib.sha256()  # Get the hash ready
            for b_block in iter(lambda: file.read(4096),b""):
                sha_256.update(b_block)
            new.write(sha_256.hexdigest())
        input("Checksum created, press the enter key to exit the program")
except:
    print("Warning: Target file not in same directory")
    input("Press the enter key to exit the program")
    sys.exit()