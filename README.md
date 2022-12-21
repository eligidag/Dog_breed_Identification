
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
Functions used in the project:
The read_fasta function reads a FASTA file and returns a dictionary with the keys and values.
he read_fasta function takes a filename as an argument and opens the file in read mode.
It reads each line in the file and checks if the first character is a > symbol.
If it is, it stores the line (minus the newline character) as the key in the data dictionary.
If it is not, it adds the line (minus the newline character) to the value of the current key in the data dictionary.
When it has finished reading the file, it returns the data dictionary.

The find_most_similar function takes two arguments: target_seq_dict and dog_breeds_DB.
target_seq_dict is a dictionary containing a single target sequence, and dog_breeds_DB is a dictionary containing a set of sequences representing different dog breeds.
The function iterates over the keys and values in target_seq_dict and dog_breeds_DB,
calculating the Levenshtein distance between the target sequence and each of the sequences in the dog breed dictionary.
It then stores the key and value of the most similar sequence, along with the length difference between the target sequence and the most similar sequence, and returns these values.

The calculate_similarity function takes three arguments: target_seq_dict, most_similar_breed, and length_difference.
target_seq_dict is a dictionary containing a single target sequence, most_similar_breed is a string representing the key of the most similar sequence in the dog breed dictionary,
and length_difference is an integer representing the length difference between the target sequence and the most similar sequence.
The function calculates the length of the target sequence and the length of the most similar sequence, and then calculates the percentage of similarity between the two sequences based on the length difference.
It returns the percentage of similarity as a floating point value.

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
