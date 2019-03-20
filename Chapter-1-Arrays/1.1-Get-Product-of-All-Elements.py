""" Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array excxept the one at i.

For example, if our input was [1,2,3,4,5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2,3,6]. 

Follow-up: What if you can't use division? """

from functools import reduce


def getProductOfAllOtherElements(arr):
    product = reduce((lambda x, y: x * y), arr)
    newArr = []

    for num in arr:
        newArr.append(product // num)

    return newArr


# without using division
# generate list of prefix products and suffix products
# each index in the returned array will be a product of a prefix and suffix product.
# utilize the concept of precomputed tables
def getProductsNoDivision(arr):
    prefixArr = getPrefixes(arr)
    suffixArr = getSuffixes(arr)
    productArr = []

    for i in range(len(arr)):
        currentPrefix = prefixArr[i - 1] if i > 0 else 1
        currentSuffix = suffixArr[i + 1] if i < len(arr) - 1 else 1
        productArr.append(currentPrefix * currentSuffix)

    return productArr


def getPrefixes(arr):
    prefixes = []
    # # calling reduce on each element is very slow.
    # for i in range(len(arr)):
    #     prefixes.append(reduce((lambda x, y: x * y), arr[0 : i + 1]))
    for num in arr:
        if prefixes:
            prefixes.append(prefixes[-1] * num)
        else:
            prefixes.append(num)
    return prefixes


def getSuffixes(arr):
    suffixes = []
    # # calling reduce on each element is very slow.
    # for i in range(len(arr))[::-1]:
    #     suffixes.insert(0, reduce((lambda x, y: x * y), arr[i::]))

    # for num in arr[::-1]:
    #     if suffixes:
    #         suffixes.insert(0, suffixes[0] * num)
    #     else:
    #         suffixes.append(num)

    # reverse is faster than insert.
    for num in arr[::-1]:
        if suffixes:
            suffixes.append(suffixes[-1] * num)
        else:
            suffixes.append(num)
    return list(reversed(suffixes))


someArr = [1, 2, 3, 4, 5]

print(getProductsNoDivision(someArr))

