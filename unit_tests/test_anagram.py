
import unittest
from bin.anagram import Anagrams
from bin.string_sorts import sort_string


class TestAnagrams(unittest.TestCase):

    def test_anagrams(self):
        anagrams = Anagrams()
        self.assertEqual(anagrams.get_anagrams('plates'), ['palest', 'pastel', 'petals', 'plates', 'staple'])
        self.assertEqual(anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])


class TestStringSorter(unittest.TestCase):

    def test_string_sorter(self):
        self.assertEqual(sort_string('Consume'), ['c', 'e', 'm', 'n', 'o', 's', 'u'])


if __name__ == '__main__':
    unittest.main()