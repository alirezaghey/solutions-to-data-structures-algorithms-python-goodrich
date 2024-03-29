# Solutions to chapter one creativity exercises

**C-1.13** Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
[Solution](C-1.13.py)


**C-1.14** Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
[Solution](C-1.14.py)

**C-1.15** Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
[Solution](C-1.15.py)

**C-1.16** In our implementation of the scale function (page 25), the body of the loop
executes the command data[j] = factor. We have discussed that numeric
types are immutable, and that use of the = operator in this context causes
the creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes the
actual parameter sent by the caller?

**Answer:** The reason why the actual parameter sent by the function caller is changed is that the
parameter is a list (array) and that particular element of the array is assigned to a
new numeric object.

**C-1.17** Had we implemented the scale function (page 25) as follows, does it work
properly?
```py
def scale(data, factor):
    for val in data:
    val *= factor
```
Explain why or why not.

**Answer:** This wouldn't have worked. `val` is an alias to the actual element in `data` and assigning a new object to it will only change `val`'s value.

**C-1.18** Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
[Solution](C-1.18.py)

**C-1.19** Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.
[Solution](C-1.19.py)

**C-1.20** Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possi-
ble order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
[Solution](C-1.20.py)

**C-1.21** Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
[Solution](C-1.21.py)

**C-1.22** Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1.
[Solution](C-1.22.py)

**C-1.23** Give an example of a Python code fragment that attempts to write an ele-
ment to a list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:
“Don’t try buffer overflow attacks in Python!”
[Solution](C-1.23.py)

**C-1.24** Write a short Python function that counts the number of vowels in a given
character string.
[Solution](C-1.24.py)


**C-1.25** Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For exam-
ple, if given the string "Let s try, Mike.", this function would return
"Lets try Mike".
[Solution](C-1.25.py)

**C-1.26** Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a + b = c,” “a = b − c,” or “a ∗ b = c.”
[Solution](C-1.26.py)

**C-1.27** In Section 1.8, we provided three different implementations of a generator
that computes factors of a given integer. The third of those implementa-
tions, from page 41, was the most efficient, but we noted that it did not
yield the factors in increasing order. Modify the generator so that it reports
factors in increasing order, while maintaining its general performance ad-
vantages.
[Solution](C-1.27.py)


**C-1.28** The p-norm of a vector <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;v&space;=&space;(v_1,v_2,...,v_n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;v&space;=&space;(v_1,v_2,...,v_n)" title="v = (v_1,v_2,...,v_n)" /></a> in n-dimensional space is defined as

<a href="https://www.codecogs.com/eqnedit.php?latex=||v||=\sqrt[p]{v_1^p&plus;v_2^p&plus;...&plus;v_n^p}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?||v||=\sqrt[p]{v_1^p&plus;v_2^p&plus;...&plus;v_n^p}" title="||v||=\sqrt[p]{v_1^p+v_2^p+...+v_n^p}" /></a>

For the special case of p = 2, this results in the traditional Euclidean
norm, which represents the length of the vector. For example, the Euclidean norm of a two-dimensional
with coordinates (4, 3) has a Euclidean norm of <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\sqrt[]{4^2&space;&plus;&space;3^2}&space;=&space;\sqrt[]{16&space;&plus;&space;9}&space;=&space;\sqrt[]{25}&space;=&space;5" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\sqrt[]{4^2&space;&plus;&space;3^2}&space;=&space;\sqrt[]{16&space;&plus;&space;9}&space;=&space;\sqrt[]{25}&space;=&space;5" title="\sqrt[]{4^2 + 3^2} = \sqrt[]{16 + 9} = \sqrt[]{25} = 5" /></a>.
Give an implementation of a function named norm such that norm(v, p) returns the p-norm value of v and norm(v) returns the Euclidean norm of v. You may assume that v is a list of numbers.
[Solution](C-1.28.py)
