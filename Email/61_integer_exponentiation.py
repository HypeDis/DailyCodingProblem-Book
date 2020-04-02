"""  
Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024. 
"""


def power(num, power):
    res = num
    doublings = power // 2
    for i in range(doublings):
        res *= res
    if power % 2 == 1:
        res *= num
    return res


print(power(10, 6))
print(power(2, 5))