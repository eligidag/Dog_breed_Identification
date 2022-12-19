import os
from functions.sequence_functions import read_fasta,find_most_similar
dog_breeds = os.path.join(os.getcwd(), 'data', 'dog_breeds.fa')
target_seq = os.path.join(os.getcwd(), 'data', 'mystery.fa')

dog_breeds_DB = read_fasta(dog_breeds)
target_seq_dict = read_fasta(target_seq)
most_similar_breed, length_difference = find_most_similar(target_seq_dict, dog_breeds_DB)

print(f"The mystery sequence is the most similar to the one of {most_similar_breed}")
print(f"With the sequence length difference of: {length_difference}")
