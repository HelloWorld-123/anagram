import unittest
from bin.anagram import Anagrams
from bin.string_sorts import sort_string, sorted_list_of_strings


class TestAnagrams(unittest.TestCase):

    def test_anagram(self):
        file = 'words.txt'
        anagrams = Anagrams(file)
        anagrams.load_dictionary()
        self.assertEqual(anagrams.get_anagrams('stop'), ['opts','post','pots','spot','stop','tops'])
        self.assertEqual(anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])


class TestStringSorter(unittest.TestCase):

    def test_string_sorter(self):
        self.assertEqual(sort_string('Consume'), ['c', 'e', 'm', 'n', 'o', 's', 'u'])

    def test_sorted_list_of_strings(self):
        self.assertEqual(sorted_list_of_strings(['palest', 'pastel', 'petals', 'plates', 'staple']), {'aelpst': ['palest', 'pastel', 'petals', 'plates', 'staple']})

if __name__ == '__main__':
    unittest.main()