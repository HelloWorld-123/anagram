import unittest
from bin.string_sorts import sort_string, sorted_list_of_strings

class TestStringSorter(unittest.TestCase):

    def test_string_sorter(self):
        self.assertEqual(sort_string('Consume'), ['c', 'e', 'm', 'n', 'o', 's', 'u'])

    def test_sorted_list_of_strings(self):
        self.assertEqual(sorted_list_of_strings(['palest', 'pastel', 'petals', 'plates', 'staple']), {'aelpst': ['palest', 'pastel', 'petals', 'plates', 'staple']})

if __name__ == '__main__':
    unittest.main()