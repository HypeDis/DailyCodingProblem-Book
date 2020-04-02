""" 
Given an array of strictly the characters 'R', 'G', and 'B', 
segregate the values of the array so that all the Rs come first, 
the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""


def sortRGB(arr):
    rPointer = 0
    bPointer = len(arr) - 1
    i = 0
    while i <= bPointer and rPointer < bPointer:
        if arr[i] == 'R':
            arr[rPointer], arr[i] = arr[i], arr[rPointer]
            rPointer += 1
        if arr[i] == 'B':
            arr[bPointer], arr[i] = arr[i], arr[bPointer]
            bPointer -= 1
        if arr[i] == 'G' or arr[i] == arr[rPointer] == 'R':
            i += 1


unsorted = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
unsorted2 = ['R', 'R', 'R']
unsorted3 = ['G', 'G', 'G']
unsorted4 = ['B', 'B', 'B']
unsorted5 = ['B', 'G', 'R']
unsorted6 = ['B', 'R', 'R', 'G', 'R']

sortRGB(unsorted)
sortRGB(unsorted2)
sortRGB(unsorted3)
sortRGB(unsorted4)
sortRGB(unsorted5)
sortRGB(unsorted6)

assert unsorted == ['R', 'R', 'R', 'G', 'G', 'B', 'B'], unsorted
assert unsorted2 == ['R', 'R', 'R'], unsorted2
assert unsorted3 == ['G', 'G', 'G'], unsorted3
assert unsorted4 == ['B', 'B', 'B'], unsorted4
assert unsorted5 == ['R', 'G', 'B'], unsorted5
assert unsorted6 == ['R', 'R', 'R', 'G', 'B'], unsorted6
