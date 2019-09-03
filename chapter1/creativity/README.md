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

The reason why the actual parameter sent by the function caller is changed is that the
parameter is a list (array) and that particular element of the array is assigned to a
new numeric object.

