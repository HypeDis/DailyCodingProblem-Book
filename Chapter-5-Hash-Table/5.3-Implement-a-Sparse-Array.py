"""
You have a large array, most of whose elements are zero.
Create a more space-efficient data structure, SparseArray, that implements the following interface:
  init(arr, size): initialize with the original large array and size. 
  set(i, val): update index at i to be val.
  get(i): get the value at index i 
"""


class SparseArray:
    def __init__(self, arr, size):
        self.size = size
        self._dict = {}
        for i, val in enumerate(arr):
            if val != 0:
                self._dict[i] = val

    # throws error if i is out of bounds of size
    def _check_bounds(self, i):
        if i < 0 or i >= self.size:
            raise IndexError('Out of bounds')

    def set(self, i, val):
        self._check_bounds(i)
        if val != 0:
            self._dict[i] = val
            return
        # delete the key if setting value to 0
        elif i in self._dict:
            del self._dict[i]

    def get(self, i):
        self._check_bounds
        # if key not in dict return 0
        return self._dict.get(i, 0)


mySparseArray = SparseArray([1, 2, 3, 4, 5, 6, 7], 25)

mySparseArray.set(22, 22)
print(mySparseArray.get(22))
# mySparseArray.set(28, 28) # out of bounds
print(mySparseArray.get(21))
print(mySparseArray.get(1))