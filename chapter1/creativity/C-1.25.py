# C-1.25 Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. For exam-
# ple, if given the string "Let's try, Mike.", this function would return
# "Lets try Mike".

import re


def removePunctuation(string: str) -> str:
    return "".join((char for char in string
                    if (char >= "A" and char <= "Z") or
                    (char >= "a" and char <= "z") or
                    (char >= "0" and char <= "9") or char == " "))


print(removePunctuation("This isn't a test about life and death."))
print(removePunctuation(
    "But, it is a test about whether you have a chance to succeed in your life!"))


def removePunctuationRegexVersion(string: str) -> str:
    return re.sub("[^a-zA-Z0-9 ]", "", string)


print(removePunctuationRegexVersion("This isn't a test about life and death."))
print(removePunctuationRegexVersion(
    "But, it is a test about whether you have a chance to succeed in your life!"))
