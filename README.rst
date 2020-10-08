Anagram Kata
============

This repo provides solution to Kata06: Anagrams (found here: http://codekata.com/kata/kata06-anagrams/)

Problem Statement
*****************

Given a file containing one word per line, and a random word (not necessarily in the file), print out all words that are anagrams.

Agreed-to stipulation: All leters must be used, and with the same occurrence. In other words, the anagram must be the same length as the input string.

Brain-storming
**************

Here are some efficiencies that I'm thinking of making as I'm parsing out the word and traversing through the word-list:

1. Noticing that the word-list file is in alphabetical order gives me the ability to evaluate words that begin with letter contained in the input-string. Of course, I can apply this to the second letter, etc... it'll be an implementation detail to see how much faster it'll make the algorithm.
2. Since I have to use all letters, matching on the length of the string is a quick win. This seems like a faster operation than considering a match on a second character.
3. There needs to be a quick way to assess whether the strings are anagrams. My first thought was to rearrange the characters (lowercase and without special chars) in alphabetical order and compare strings, but this would likely be very time consuming. Doing it in a (mathematical) way without needing to rearrange the characters might be interesting - one thought is to assign a prime number to each character (a=2, b=3, c=5, ...) and then multiplying each character together to get a "anagram sum". I'll want to test which of these approaches nets a faster operation.
4. Finally, there are n! combinations of the word possible (where {n} = number of characters). Once the list of anagrams reaches that number, let's exit.

Usage
*****

Find an anagram to 'great':

>>> python anagram.py --word great
✨🍰✨

Run tests:

>>> python test_anagram.py
