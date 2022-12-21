import unittest
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
