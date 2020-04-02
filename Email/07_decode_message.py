""" 
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
count the number of ways it can be decoded.

For example, the message '111' would give 3, 
since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. 
For example, '001' is not allowed
"""
from collections import deque
import string
i = 0

alphaDict = {str(n + 1): ch for n, ch in enumerate(string.ascii_lowercase)}


def decodeMessage(encoded):
    messages = deque([{'str': '', 'idx': 0}])
    res = []
    for i in range(len(encoded)):
        charcode1 = encoded[i]
        charcode2 = None
        if int(charcode1) < 3 and i < len(encoded) - 1 and int(
                encoded[i + 1]) < 7:
            charcode2 = charcode1 + encoded[i + 1]

        msgLen = len(messages)

        for j in range(msgLen):
            curMsg = messages.popleft()

            copy = curMsg.copy()
            if (copy['idx'] == i):
                copy['str'] += alphaDict[charcode1]
                copy['idx'] += 1

            if copy['idx'] > len(encoded) - 1:
                res.append(copy)
            else:
                messages.append(copy)

            if charcode2 and curMsg['idx'] == i:
                copy2 = curMsg.copy()
                copy2['str'] += alphaDict[charcode2]
                copy2['idx'] += 2
                if copy2['idx'] > len(encoded) - 1:
                    res.append(copy2)
                else:
                    messages.append(copy2)

    return [x['str'] for x in res]
