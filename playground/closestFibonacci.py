def getClosestFib(num):
    fibArr = [1, 1]
    while (fibArr[len(fibArr) - 1] < num):
        fibArr.append(fibArr[len(fibArr) - 1] + fibArr[len(fibArr) - 2])
    print(fibArr)

    fibLeft = fibArr[len(fibArr) - 2]
    fibRight = fibArr[len(fibArr) - 1]

    return fibLeft if abs(fibLeft - num) < abs(fibRight - num) else fibRight


print(getClosestFib(123))

# do it recursively