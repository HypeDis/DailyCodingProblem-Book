"""  
Given a array of numbers representing the stock prices of a company in chronological order, 
write a function that calculates the maximum profit you could have made 
from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, 
since you could buy the stock at 5 dollars and sell it at 10 dollars. 
"""


def getBestTrade(prices):
    #  naive solution is 2 for loops n^2 runtime
    maxSeen = prices[-1]
    maxTrade = 0
    for i in range(len(prices) - 2, -1, -1):
        maxSeen = max(maxSeen, prices[i])
        maxTrade = max(maxTrade, maxSeen - prices[i])
    return maxTrade


print(getBestTrade([4, 2, 7, 20, 10, 25]))  # 23
