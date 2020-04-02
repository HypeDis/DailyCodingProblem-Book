'''
Implement an autocomplete system. That is, 
given a query string s and a set of all possible query strings, 
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], 
return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

# use a trie to hold all the words

dict = {
    'd': {
        'o': {
            'g': {
                'end': True
            }
        },
        'e': {
            'e': {
                'r': {
                    'end': True
                }
            },
            'a': {
                'l': {
                    'end': True
                }
            }
        }
    }
}


def autocomplete(partial):
    root = dict
    for char in partial:
        root = root[char]
    return getWords(root, partial, [])


def getWords(root, curStr, res):
    for char in root:
        if char == 'end':
            res.append(curStr)
        else:
            getWords(root[char], curStr + char, res)
    return res


print(autocomplete('de'))
