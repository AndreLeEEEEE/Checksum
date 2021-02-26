# Checksum
This repository contains two programs, for generating the checksum of a file and another for checking the checksum of a file.

Versions of python and installed modules:
- python 3.7.8
- Visual Studio 16.8.4

Both programs utilize sha-256, Secure Hashing Algorithm, into other to read in the binary of files and convert it to a hex string.

The Checksum program allows the user to enter in the name of a file and have its hashed value written into a similarly named
text file, except there's a "- Checksum" at the end.

The CompareSum program allows the user to enter in a file and, assuming that file already has a corresponding checksum file, 
compare it's old hashed value with its current hash value. If the values are the same, a "Clear" message is printed out. If
the values are different, it means the entered file has been modified and a "Warning" message is printed.

All files, entered and checksum, should be in the same directory as the programs since methods to search the entire computer,
or at least the current drive, have proved unfruitful.

Update 2/19/2021: I'm not sure if this program is gonna be useful since 7-Zip File Manager adds the CRC SHA option to the
contextual menu (when you right click a file). While this project uses one program to generate a sha256 hash value and 
another for comparison, CRC SHA allows the user to look at the SHA256 hash value of any file instantaneously. The latter
doesn't do comparisons, but that isn't hard to do manually when you already have the old hash value saved somewhere.
