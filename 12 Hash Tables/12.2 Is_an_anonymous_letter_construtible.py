import collections

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    char_freq_from_letter = collections.Counter(letter_text)

    for c in magazine_text:
        if c in char_freq_from_letter:
            char_freq_from_letter[c] -= 1
            if char_freq_from_letter[c] == 0:
                def char_freq_from_letter[c]
                if not char_freq_from_letter:
                    return True
    return True


def is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text):
    return (not collections.Counter(letter_text) - collections.Counter(magazine_text))