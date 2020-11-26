import functools
import string
import random
import collections

def string_hash(s, modulus):
    MULT = 997
    return functools.reduce(lambda v, c: (v * MULT + ord(c)) % modulus, s, 0)



def random_string_iter(num, length):
    """
    :param num: num of strings in the iterable
    :param length: word length of strings
    :return: an iterable
    """
    str_arr = []
    letters = string.printable
    for _ in range(num):
        str_arr.append(''.join(random.choice(letters) for _ in range(length)))
    return (str_arr)

def find_anagrams(dictionary):
    sorted_string_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)

    return [group for group in sorted_string_to_anagrams.values() \
            if len(group) >= 2]



def find_anagrams_nm(dictionary):
    counter_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        key = frozenset(collections.Counter(s).items())
        counter_to_anagrams[key].append(s)
    return [group for group in counter_to_anagrams.values() \
            if len(group) >= 2]


if __name__ == "__main__":
    length = 10 # length of the string
    test_str = ''.join(random.choice(string.printable) for _ in range(length))
    result = string_hash(test_str, 10)
    print(result)

    print(string_hash('123', 10))
    print(string_hash(['1', '2', '3'], 10)

    print(find_anagrams_nm(dictionary))
