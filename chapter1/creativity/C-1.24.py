# C-1.24 Write a short Python function that counts the number of vowels in a given
# character string.


def countVowels(string: str) -> int:
    vowels = {"a", "e", "i", "o", "u"}
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count


print(countVowels("This is a test!"))
print(countVowels(""))
print(countVowels("ddkslc,nzx"))
print(countVowels("eeeaaa"))
