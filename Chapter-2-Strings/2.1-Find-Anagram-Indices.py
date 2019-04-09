""" 
Given a word w and a string s, find all indices in s which are the starting locations of anagrams of w. For example, given w is 'ab' and s is 'abxaba', return [0, 3, 4] 
"""

from collections import defaultdict


w = "cab"
s = "cabaabca"

# sliding window technique
# take away used values from the hash map
# add values back once the window slides
# remove all keys that have 0 frequency
# empty object means anagram has been found

from collections import defaultdict

pass


def delIfZero(dict, char):
    if dict[char] == 0:
        del dict[char]


def anagramIndices(word, string):
    result = []
    freq = defaultdict(int)
    # load up the hash map with characters from the word
    for char in word:
        freq[char] += 1

    #  preload the map with the first window
    for char in string[: len(word)]:
        freq[char] -= 1
        delIfZero(freq, char)
    if not freq:
        result.append(0)

    # for-loop to iterate through rest of the window, beginning with index 1
    for i in range(1, len(string) - len(word) + 1):
        # add the previous value back in
        prevChar, newChar = string[i - 1], string[i + len(word) - 1]

        freq[prevChar] += 1
        delIfZero(freq, prevChar)

        # take away new char from freq table
        freq[newChar] -= 1
        delIfZero(freq, newChar)

        # add index if freq table is empty
        if not freq:
            result.append(i)

    return result


print(anagramIndices(w, s))
