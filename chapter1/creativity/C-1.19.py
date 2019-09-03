# C-1.19 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.

from typing import List


def englishAlphabet() -> List[str]:
    return [chr(i) for i in range(ord("a"), ord("a")+26)]


print(englishAlphabet())
