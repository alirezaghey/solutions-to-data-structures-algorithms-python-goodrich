# C-1.13 Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.


def myReverse(data):
    # returning a new reversed list
    return [data[i] for i in range(len(data)-1, -1, -1)]


def myReverseGen(data):
    # returning a reversed generator
    for i in range(len(data)-1, -1, -1):
        yield data[i]


def myReverseGenWithComprehension(data):
    # returning a reversed generator
    return (data[i] for i in range(len(data)-1, -1, -1))
