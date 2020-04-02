"""  
Implement a URL shortener with the following methods:

    shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
    restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.

Hint: What if we enter the same URL twice? 
"""
import string
from random import randint

# imagine this is a db or something
shortenedTable = {}
originalTable = {}


def initRandomString(length):
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    alphaNum = letters + numbers

    def generateRandomString():
        randStr = ''
        for i in range(length):
            randNum = randint(0, len(alphaNum) - 1)
            randStr += alphaNum[randNum]
        return randStr

    return generateRandomString


getRandom6 = initRandomString(6)


def shortenUrl(url):
    if url in originalTable:
        raise ValueError('url has already been shortened', originalTable[url])

    shortened = getRandom6()
    if shortened not in shortenedTable:
        shortenedTable[shortened] = url
        originalTable[url] = shortened
    else:
        print('shortened url already in use, making a new one')
        shortenUrl(url)


shortenUrl('google/cutepuppies')
shortenUrl('yahoo/helloworld')
shortenUrl('bing/coronavirus')
print(shortenedTable)