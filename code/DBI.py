dog_breeds = r'C:\Users\eligi\Desktop\pythonProject\data\dog_breeds.fa'
target_seq = r'C:\Users\eligi\Desktop\pythonProject\data\mystery.fa'

from collections import defaultdict
from Levenshtein import distance

def read_fasta(filename):
    """Read a FASTA file and return a dictionary with the keys and values."""
    data = defaultdict(str)
    with open(filename, "r") as f:
        for line in f:
            if line[0] == '>':
                key = line.strip('\n')
            else:
                data[key] +=line.strip("\n")
    return data

def find_most_similar(target_seq_dict, dog_breeds_dict):
    """ Find the most similar sequence in the dog breeds dictionary to the target sequence,
     using the Levenshtein distance"""

    # empty variable used to store minimum distance
    min_distance = float('inf')
    # variable to store the key of the most similar sequence
    most_similar = None
    # iteration over the keys and values in the target_seq_dict
    for target_key, target_value in target_seq_dict.items():
        # iteration over the keys and values in the dog_breeds_DB
        for breed_key, breed_value in dog_breeds_DB.items():
            # calculating the Levenshtein distance between mystery/target sequence and all the sequences in the DB
            dist = distance(target_value, breed_value)
            # if the current distance is smaller than the one that is currently stored in minimum distance
            # it becomes the new current minimum distance
            if dist < min_distance:
                # updates minimum distance based on "if" results
                min_distance = dist
                # stores the key value pair that is currently the most similar to the target seq
                most_similar = breed_key
    return most_similar

#read the FASTA files into dictionaries
dog_breeds_DB = read_fasta(dog_breeds)
target_seq_dict = read_fasta(target_seq)

#find the most similar sequence
most_similar = find_most_similar(target_seq_dict,dog_breeds_DB)
print(most_similar)