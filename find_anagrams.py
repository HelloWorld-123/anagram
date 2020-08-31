import datetime
import sys
from bin.anagram import Anagrams


def start_time_method():
    return datetime.datetime.now()


def execution_time_method(start_time):
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000
    return round(execution_time, 2)


def loading_dictionary():
    start_time = start_time_method()
    file = sys.argv[-1]
    anagram_object = Anagrams(file)
    anagram_object.load_dictionary()
    execution_time = execution_time_method(start_time)
    print("Initialized in {} ms\n".format(execution_time))
    return anagram_object


def _get_anagrams(anagram_object, word):
    start_time = start_time_method()
    anagram_list = anagram_object.get_anagrams(word)
    anagram_list_len = len(anagram_list)
    execution_time = execution_time_method(start_time)
    if anagram_list_len > 0:
        print("{} Anagrams found for {} in {}ms".format(anagram_list_len, word, execution_time))
        print(','.join(anagram_list)+'\n')
    else:
        print("No Anagrams found for {} in {}ms\n".format(word, execution_time))


def main():
    print("Welcome to the Anagram Finder\n-----------------------------")
    anagram_object = loading_dictionary()
    while True:
        word = input("AnagramFinder>")
        if word.lower() == 'exit':
            break
        _get_anagrams(anagram_object, word)


if __name__ == '__main__':
    main()
