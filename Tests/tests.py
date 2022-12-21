import unittest
import io
from functions.sequence_functions import read_fasta,find_most_similar, calculate_similarity

class TestFunctions(unittest.TestCase):
    def test_read_fasta(self):
        #information to be tested
        test_fasta = '>breed=affenpinscher\nATCGATCG\n>breed=african_hunting_dog\nATCGATCGATCG\n>breed=airedale\nATCGATCGATCGATCG\n'
        #file object creation from the test FASTA string
        f = io.stringIO(test_fasta)
        #read_fasta test using file object
        result = read_fasta(f)
        #check if it is whats expected
        self.assertEqual(result, {
            '>breed=affenpinscher': 'ATCGATCG',
            '>breed=african_hunting_dog': 'ATCGATCGATCG',
            '>breed=airedale': 'ATCGATCGATCGATCG'
        })
    def test_find_most_similar(self):
        #dictionary of breeds for testing
        dog_breeds_DB = {
            '>breed=affenpinscher': 'ATCGATCG',
            '>breed=african_hunting_dog': 'ATCGATCGATCG',
            '>breed=airedale': 'ATCGATCGATCGATCG'
        }
        #dictionary of target sequence
        target_seq_dict = {
            '>mystery': 'ATCGATCG'
        }
        #function testing with the test data
        result = find_most_similar(target_seq_dict,dog_breeds_DB)
        #check if it is whats expected
        self.assertEqual(result, ('affenpinscher', 0))

    def test_calculate_similarity(self):
        #dictionary of breeds for testing
        dog_breeds_DB = {
            '>breed=affenpinscher': 'ATCGATCG',
            '>breed=african_hunting_dog': 'ATCGATCGATCG',
            '>breed=airedale': 'ATCGATCGATCGATCG'
        }
        #dictionary of target sequence
        target_seq_dict = {
            '>mystery': 'ATCGATCG'
        }
        #find the most similar breed and the length difference
        most_similar_breed, length_difference = find_most_similar(target_seq_dict, dog_breeds_DB)
        #test calculate_similarity()
        result = calculate_similarity(target_seq_dict, most_similar_breed, length_difference)
        #check if the results are as expected
        self.assertEqual(result, 100)

unittest.main()