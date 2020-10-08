import math
import re
from time import time

def char_range(c1='a', c2='z'):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

def prime_range():
    num = 1
    while True:
        num += 1
        for i in range(2, num):
            if num != 2 and num % i == 0:
                break
        else:
            yield(num)

class Anagram:

    def __init__(self, word: str, word_list_file: str = 'wordlist.txt'):
        self.anagrams = set()
        self.anagrams_scrubbed = set()
        self.possible_anagram_count = math.factorial(len(word))
        self.primes_by_char = dict(zip(char_range(), prime_range()))
        self.word = self._scrub(word)
        self.word_length = len(self.word)
        self.word_prime_value = self._get_prime_value(self.word)
        self.word_list_file = word_list_file

        self._process()


    def __str__(self):
        return '\n'.join(map(str, self.anagrams))


    def __repr__(self):
        return str(self.anagrams)


    def _process(self):

        try:
            with open(self.word_list_file) as f:
                while True:
                    line = f.readline()
                    if not line:
                        break

                    line_scrubbed = self._scrub(line)

                    if not line_scrubbed[0] in self.word:
                        continue

                    if len(line_scrubbed) != self.word_length:
                        continue

                    if self.word_prime_value == self._get_prime_value(line_scrubbed):
                        self.anagrams.add(line.strip())
                        self.anagrams_scrubbed.add(line_scrubbed)
                        
                        # NOTE: we cannot do this because anagrams can be encountered with special characters further down the file
                        # if len(self.anagrams_scrubbed) == self.possible_anagram_count:
                        #     break;

        except OSError as err:
            print("OS error: {0}".format(err))
    

    def _get_prime_value(self, word: str = ''):

        prime_value = 1
        if not word is None:
            for char in word:
                prime_value *= self.primes_by_char[char]

        return prime_value
    
    @staticmethod
    def _scrub(word: str):
        return re.sub(r"[^a-z]+", '', word.lower())


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Find anagrams of input string within a word-list file.')
    parser.add_argument('--file', metavar='file', required=False, default='wordlist.txt',
                        help='The path to word-list file')
    parser.add_argument('--word', metavar='word', required=True,
                        help='Input string')
    args = parser.parse_args()

    start = time()
    print(Anagram(word=args.word, word_list_file=args.file))
    print(f'Execution time (sec): {str(time() - start)}')
