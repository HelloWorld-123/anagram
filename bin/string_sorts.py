def sort_string(string):
    """
    :param string:
    :return: A lowercase list of the letters in the given string, sorted by alphabetical order
    """
    return sorted(string.lower())


def sorted_list_of_strings(list_of_strings):
    """
    :param list_of_strings:
    :return: A list of tuples (original string, split alphabetised string)
    """
    return [(string, sort_string(string)) for string in list_of_strings]