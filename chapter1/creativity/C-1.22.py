# C-1.22 Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it returns
# an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1.

from typing import List


def dotProduct(a: List[int], b: List[int]) -> List[int]:
    '''
    Returns a generator of ints containing the dot product of the input lists
    '''
    if len(a) != len(b):
        print("Both parameters need to be of the same length!")
        raise ValueError()
    for i in range(len(a)):
        yield a[i]*b[i]


def dotProductList(a: List[int], b: List[int]) -> List[int]:
    '''
    Returns a list of ints containing the dot product of the input lists
    '''
    if len(a) != len(b):
        print("Both parameters need to be of the same lenght!")
        raise ValueError()
    return [a[i]*b[i] for i in range(len(a))]


a = [1, 2, 3]
b = [4, 5, 6]

print(list(dotProduct(a, b)))
print(dotProductList(a, b))
