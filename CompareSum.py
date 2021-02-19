import hashlib
import sys

def getHash(fileName):
    try:
        with open(fileName, 'rb') as file:
            sha_256 = hashlib.sha256()  # Get the hash ready
            for b_block in iter(lambda: file.read(4096),b""):  # Read in blocks of bytes
                sha_256.update(b_block)

            return sha_256.hexdigest()
    except:
        print("Warning: Target file not in same directory")
        input("Press the enter key to exit the program")
        sys.exit()

def main():
    name = input("Enter the file name with its extension: ")
    name.strip()
    current_hash = getHash(name)

    name = name.split('.')
    name.pop()
    name = '.'.join(name)
    try:
        with open(name + " - Checksum.txt", "rt") as f:
            original_hash = f.read()
    except:
        print("Warning: Corresponding Checksum.txt not in same directory")
        input("Press the enter key to exit the program")
        sys.exit()

    try:
        if current_hash != original_hash:
            raise Exception
        print("Clear: The checksums match")
    except:
        print("Warning: The checksum values don't match")
    finally:
        input("Press the enter key to exit the program")

main()
