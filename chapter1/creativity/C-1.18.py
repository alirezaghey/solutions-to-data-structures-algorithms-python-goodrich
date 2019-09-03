# C-1.18 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

# The pronic numbers are the product of two consecutive numbers


def pronicNumbers(n: int) -> int:
    # returns n pronic numbers
    # Time complexity: O(n)
    # Space complexity: O(n)
    return [x*(x+1) for x in range(n)]


print(pronicNumbers(10))
