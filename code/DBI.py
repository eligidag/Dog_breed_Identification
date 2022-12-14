dog_breeds = r'C:\Users\eligi\Desktop\pythonProject\data\dog_breeds.fa'
target_seq = r'C:\Users\eligi\Desktop\pythonProject\data\mystery.fa'

from collections import defaultdict

dog_breeds_DB = defaultdict(str)
with open(dog_breeds, "r") as f:
    for line in f:
        if line[0] == '>':
            key = line.strip('\n')
        else:
            dog_breeds_DB[key] += line.strip('\n')
print(dog_breeds_DB)