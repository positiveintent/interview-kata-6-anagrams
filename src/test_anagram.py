import unittest

from anagram import Anagram


class TestAnagram(unittest.TestCase):

    def test_primes_by_char(self):
        """
        Test that primes_by_char is a dictionary of lower-case letters assigned to prime numbers
        """
        obj = Anagram(word='')

        self.assertEqual(26, len(obj.primes_by_char), 'Dict length should equal number of letters in the alphabet.')
        for key in obj.primes_by_char.keys():
            self.assertEqual(1, len(key), 'Each key should be a single character.')
            self.assertTrue(key.islower(), 'Each key should be lower-case.')
            self.assertTrue(key.isalpha(), 'Each key should be alpha.')
        
        self.assertEqual(67, obj.primes_by_char['s'], 'Spot check value for \'s\'.')
        self.assertEqual(53, obj.primes_by_char['p'], 'Spot check value for \'p\'.')
        self.assertEqual(47, obj.primes_by_char['o'], 'Spot check value for \'o\'.')
        self.assertEqual(71, obj.primes_by_char['t'], 'Spot check value for \'t\'.')
    

    def test_get_prime_value(self):
        obj = Anagram(word='')

        self.assertEqual(1, obj._get_prime_value(''), 'Blank string should be 1.')
        self.assertEqual(2, obj._get_prime_value('a'), 'A single character should be its assigned prime number.')
        self.assertEqual(98, obj._get_prime_value('add'), '\'add\' should be 2*7*7=98')
        self.assertEqual(obj._get_prime_value('add'), obj._get_prime_value('dad'), 'Anagram values should equal.')
        self.assertEqual(obj._get_prime_value('door'), obj._get_prime_value('odor'), 'Anagram values should equal.')


    def test_scrub_should_convert_to_lowercase(self):
        self.assertEqual('lowercase', Anagram._scrub('LOWERCASE'), 'Should convert to lowercase.')


    def test_scrub_should_remove_special_characters(self):
        self.assertEqual('doesnthavespecialcharacters', Anagram._scrub("Doesn't ^^ have ** special __ characters!!"), 'Should convert to lowercase.')

    
    def test_anagram_a(self):
        obj = Anagram(word='a')
        self.assertEqual(2, len(obj.anagrams))
        self.assertIn('A', obj.anagrams, 'Should retain unscrubbed version of the found anagram.')
        self.assertIn('a', obj.anagrams)

    def test_anagram_formats(self):
        obj = Anagram(word='formats')
        self.assertEqual(3, len(obj.anagrams))
        self.assertIn('farmost', obj.anagrams)
        self.assertIn('formats', obj.anagrams)
        self.assertIn('format\'s', obj.anagrams, 'Should retain anagram with special character.')
    
    def test_invalid_anagram(self):
        obj = Anagram(word='_')
        self.assertEqual(0, len(obj.anagrams))


if __name__ == '__main__':
    unittest.main()
