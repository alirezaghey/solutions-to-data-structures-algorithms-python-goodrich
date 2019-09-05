# P-1.29 Write a Python program that outputs all possible strings
# formed by using the characters 'c' , 'a' , 't' , 'd' , 'o' , and 'g'
# exactly once.

from typing import Dict, List


def permutate(input: str) -> None:
    """
    prints out all permutations of input

    Taking a recursive approach the algorithm will
    use a frequency table that of the input string
    and methodically exhaust the decision space by
    removing character from it one by one and adding
    them to the result, always backtracking when the
    possibilities for a certain variation are done.

    This algorithm also works with repeating characters
    in the input and will output the result in lexicographically
    correct order.

    Time complexity: O(!n) where n == len(input); Note: if input has
    repeated characters, the time complexity will decrease, e.g. for input == "AABB"
    it'll be !4/(!2*!2)
    Space complexity: O(n) where n == len(input), since we're just
    printing the results and don't store them, otherwise it would be O(n*!n)
    """

    # Create a frequency table for the characters
    fTable = {}
    for c in input:
        if c in fTable:
            fTable[c] += 1
        else:
            fTable[c] = 1
    keys = sorted(fTable.keys())
    string = []
    count = []
    for key in keys:
        string.append(key)
        count.append(fTable[key])
    result = ["" for i in range(len(input))]

    permuteUtil(string, count, result, 0)


counter = 0


def permuteUtil(string: [str], count: [int], result: List[str], level: int) -> None:
    if level == len(result):
        global counter
        counter += 1
        print(counter, "".join(result))
        return
    for i in range(len(result)):
        if count[i] == 0:
            continue
        result[level] = string[i]
        count[i] -= 1
        permuteUtil(string, count, result, level+1)
        count[i] += 1


permutate("catdog")
