import unittest
import datetime
from find_anagrams import start_time_method, execution_time_method

class TestStringSorter(unittest.TestCase):

    def test_string_sorter(self):
        self.assertLessEqual(start_time_method(), datetime.datetime.now())

    def test_sorted_list_of_strings(self):
        self.assertGreaterEqual(execution_time_method(datetime.datetime.now()), 0)

if __name__ == '__main__':
    unittest.main()