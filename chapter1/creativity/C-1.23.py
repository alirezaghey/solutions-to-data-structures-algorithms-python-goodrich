# C-1.23 Give an example of a Python code fragment that attempts to write an ele-
# ment to a list based on an index that may be out of bounds. If that index
# is out of bounds, the program should catch the exception that results, and
# print the following error message:
# “Don’t try buffer overflow attacks in Python!”

from typing import List


def throwsOutOfBoundsException(data: List):
    try:
        for i in range(len(data)+1):
            print(data[i])
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")


data = [1, 3, 4, 6, 7]
throwsOutOfBoundsException(data)
