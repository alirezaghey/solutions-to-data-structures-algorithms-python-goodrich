# C-1.24 Write a short Python function that counts the number of vowels in a given
# character string.

import re


def countVowels(string: str) -> int:
    vowels = {"a", "e", "i", "o", "u"}
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count


def countVowelsUsingRegex(string: str) -> int:
    return len(re.findall("[aeiou]", string))


print(countVowels("This is a test!"))
print(countVowels(""))
print(countVowels("ddkslc,nzx"))
print(countVowels("eeeaaa"))

print(countVowelsUsingRegex("This is a test!"))
print(countVowelsUsingRegex(""))
print(countVowelsUsingRegex("ddkslc,nzx"))
print(countVowelsUsingRegex("eeeaaa"))
