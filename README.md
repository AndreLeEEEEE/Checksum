# Checksum
This repository contains two programs, for generating the checksum of a file and another for checking the checksum of a file.

Both programs utilize sha-256, Secure Hashing Algorithm, into other to read in the binary of files and convert it to a hex string.

The Checksum program allows the user to enter in the name of a file and have its hashed value written into a similarly named
text file, except there's a "- Checksum" at the end.

The CompareSum program allows the user to enter in a file and, assuming that file already has a corresponding checksum file, 
compare it's old hashed value with its current hash value. If the values are the same, a "Clear" message is printed out. If
the values are different, it means the entered file has been modified and a "Warning" message is printed.

All files, entered and checksum, should be in the same directory as the programs since methods to search the entire computer,
or at least the current drive, have proved unfruitful.
