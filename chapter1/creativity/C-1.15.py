# C-1.15 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).

from typing import List


def areDistinct(data: List[int]) -> bool:
    # Using the property of sets that only unique values are hold
    # we are going to add all elements of data to the set
    # and compare the set's and data's length. If they're equal it means
    # that are the elements in data are distinct
    uniqueNums = {x for x in data}
    return len(uniqueNums) == len(data)


data = [3, 4, 6, 9, 5, 4]
print(areDistinct(data))
