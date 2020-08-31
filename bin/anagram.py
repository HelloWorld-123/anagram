import threading
from bin.string_sorts import sorted_list_of_strings, sort_string
import sys

class Anagrams:

    def __init__(self, file):
        lock = threading.RLock()
        lock.acquire()
        try:
            words_file = open('./'+file, 'r')
            self.words = words_file.read().splitlines()
            words_file.close()
        except IOError:
            print("Error: File does not appear to exist.")
            sys.exit()
        finally:
            lock.release()

    def load_dictionary(self):
        self.sorted_list_of_words = sorted_list_of_strings(self.words)

    def get_anagrams(self, word):
        lock = threading.RLock()
        lock.acquire()
        try:
            sorted_word = ''.join(sort_string(word))
            anagram_list=self.sorted_list_of_words[sorted_word]
        finally:
            lock.release()
        return anagram_list
