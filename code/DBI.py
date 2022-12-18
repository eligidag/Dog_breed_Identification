dog_breeds = r'C:\Users\eligi\Desktop\pythonProject\data\dog_breeds.fa'
target_seq = r'C:\Users\eligi\Desktop\pythonProject\data\mystery.fa'

from collections import defaultdict
from Levenshtein import distance

dog_breeds_DB = defaultdict(str)
with open(dog_breeds, "r") as f:
    for line in f:
        if line[0] == '>':
            key = line.strip('\n')
        else:
            dog_breeds_DB[key] += line.strip('\n')

target_seq_dict = defaultdict(str)
with open(target_seq, "r") as f:
    for line in f:
        if line[0] == '>':
            key = line.strip('\n')
        else:
            target_seq_dict[key] += line.strip('\n')

#empty variable used to store minimum distance
min_distance = float('inf')
#variable to store the key of the most similar sequence
most_similar = None
#iteration over the keys and values in the target_seq_dict
for target_key, target_value in target_seq_dict.items():
    #iteration over the keys and values in the dog_breeds_DB
    for breed_key, breed_value in dog_breeds_DB.items():
        #calculating the Levenshtein distance between mystery/target sequence and all the sequences in the DB
        dist = distance(target_value, breed_value)
        #if the current distance is smaller than the one that is currently stored in minimum distance
        #it becomes the new current minimum distance
        if dist < min_distance:
            #updates minimum distance based on "if" results
            min_distance = dist
            #stores the key value pair that is currently the most similar to the target seq
            most_similar = breed_key
print(most_similar)