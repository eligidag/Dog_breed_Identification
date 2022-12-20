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
                data[key] += line.strip("\n")
    return data

def find_most_similar(target_seq_dict, dog_breeds_DB):
    """ Find the most similar sequence in the dog breeds dictionary to the target sequence,
     using the Levenshtein distance"""



    # empty variable used to store minimum distance
    min_distance = float('inf')
    # variable to store the key of the most similar sequence
    most_similar = None
    #variable to store the length difference between the most similar sequence and the target sequence
    # iteration over the keys and values in the target_seq_dict
    for target_key, target_value in target_seq_dict.items():
        # iteration over the keys and values in the dog_breeds_DB
        for breed_key, breed_value in dog_breeds_DB.items():
            # calculating the Levenshtein distance between mystery/target sequence and all the sequences in the DB
            dist = distance(target_value, breed_value)
            # Calculate the length difference between the target sequence and the current sequence
            len_diff = abs(len(target_value) - len(breed_value))
            # if the current distance is smaller than the one that is currently stored in minimum distance
            # it becomes the new current minimum distance
            if dist < min_distance:
                # updates minimum distance based on "if" results
                min_distance = dist
                most_similar = breed_key
                breed_name = breed_key[breed_key.index("breed=")+len("breed="):breed_key.index("]", breed_key.index("breed="))]

    return (breed_name, min_distance)

def calculate_similarity(target_seq_dict, most_similar_breed, length_difference, dog_breeds_DB):

    target_seq_length = len(next(iter(target_seq_dict.values())))

    #length of the most similar sequence
    most_similar_length = len(dog_breeds_DB[most_similar_breed])

    #percentage of similarity between target seq and most similar seq
    similarity = (100 - (((length_difference / target_seq_length)) * 100))

    return similarity