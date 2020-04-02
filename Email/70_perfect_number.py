"""  
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28. 
"""

# 19, 28, 37, 46, 55, 64, 73, 82, 91
# 109, 118, 127, 136, 145, 154, 163, 172, 181, 190


def getPerfectNumber(n):
    count = 0
    curNum = 19
    while True:
        if sumDigits(curNum) == 10:
            count += 1
        if count == n:
            return curNum
        curNum += 1


def sumDigits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum


print(getPerfectNumber(1000))