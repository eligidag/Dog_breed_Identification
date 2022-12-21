
DOG BREED IDENTIFIER    
***
This project is designed to take a DNA sequence of an unknown dog breed and 
compare it against a preselected database compiled of identified dog breeds.
Resulting in an identification of the closest sequence in the database to the provided sequence.
***
Used data:

The `dog_breeds.fa` file contains the sequence in our database, to compare against.

The `mystery.fa` sequence contains a sequence from an unknown dog type, and we want to identify what is the closest breed 
to it in our database.

***

Used packages:
collections is a built-in Python package that provides specialized container data types.
It includes defaultdict, which is a subclass of the built-in dict class that provides a default value for a nonexistent key.

Levenshtein is a third-party Python package that provides functions for calculating the Levenshtein distance between two strings.
The Levenshtein distance is a measure of the similarity between two strings,
based on the minimum number of single-character edits (insertions, deletions, or substitutions) required to transform one string into the other.

unittest is a built-in Python package that provides a set of tools for testing Python code.
It includes a testing framework and a number of utilities for constructing and running tests.

io is a built-in Python package that provides functions for working with input and output streams.
It includes a number of classes for reading and writing data in various formats, including text and binary data.

os is a built-in Python package that provides functions for interacting with the operating system.
It includes a number of utilities for working with files and directories, as well as functions for controlling processes and interacting with the environment.
***
To run the Dog breed identifier, once uploaded, type this in the terminal of your chosen python interpreter:
python DBI.py
