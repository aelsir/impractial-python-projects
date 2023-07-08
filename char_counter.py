"""Display the count of characters in sentence"""

import pprint


def main():
    """Count the characters in sentence"""
    sentence = "I love sudanese songs because they're one of the best things you can every listen to"
    char_counter = {}
    for letter in sentence:
        letter = letter.lower()
        if letter not in (" ", "'"):
            if letter not in char_counter:
                char_counter[letter] = [letter]
            else:
                char_counter[letter] += [letter]

    pprint.pprint(char_counter)
if __name__ == '__main__':
    main()
        