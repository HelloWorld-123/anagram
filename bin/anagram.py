import threading
from bin.string_sorts import sorted_list_of_strings, sort_string


class Anagrams:

    def __init__(self):
        lock = threading.RLock()

        lock.acquire()
        try:
            words_file = open('data/words.txt', 'r')
            self.words = words_file.read().splitlines()
            words_file.close()
        finally:
            lock.release()

    def get_anagrams(self, word):
        lock = threading.RLock()

        lock.acquire()
        try:
            sorted_word = sort_string(word)
            sorted_list_of_words = sorted_list_of_strings(self.words)
            anagram_list = [word_tuple[0] for word_tuple in sorted_list_of_words if word_tuple[1] == sorted_word]
        finally:
            lock.release()

        return anagram_list