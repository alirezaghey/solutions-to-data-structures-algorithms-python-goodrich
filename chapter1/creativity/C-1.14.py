# C-1.14 Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.

from typing import List


def isProductOdd(data: List[int]) -> (int, int):
    # Determines if a pairs product is odd and returns that pair
    # Multiplies every integer with the rest and tests the result
    # Time complexity: O(n^2) where n == len(data). It's actually (n-1+n-2+n-3+...2+1) => n * (n+1) / 2 => O(n^2)
    # Space complexity: O(1)
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if (data[i] != data[j]) and ((data[i] * data[j]) % 2 == 1):
                return data[i], data[j]
    return False


def isProductOddOptimized(data: List[int]) -> (int, int):
    # Determines if a pairs product is odd and returns that pair
    # For a product to be odd, both the factors need to be odd
    # Using this fact, we are going to check for two distinct odd elements and return them if found
    # Time complexity: O(n) where n == len(data)
    # Space complexity: O(1)
    oddElements = {x for x in data if x % 2 == 1}
    if len(oddElements) > 1:
        return oddElements.pop(), oddElements.pop()
    return False


data = [4, 8, 10, 1]

print(isProductOdd(data))
print(isProductOddOptimized(data))
