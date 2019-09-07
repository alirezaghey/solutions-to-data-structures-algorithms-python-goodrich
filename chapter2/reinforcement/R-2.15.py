# R-2.15 The Vector class of Section 2.3.3 provides a constructor that takes an in-
# teger d, and produces a d-dimensional vector with all coordinates equal to
# 0. Another convenient form for creating a new vector would be to send the
# constructor a parameter that is some iterable type representing a sequence
# of numbers, and to create a vector with dimension equal to the length of
# that sequence and coordinates equal to the sequence values. For example,
# Vector([4, 7, 5]) would produce a three-dimensional vector with coordi-
# nates <4, 7, 5>. Modify the constructor so that either of these forms is
# acceptable; that is, if a single integer is sent, it produces a vector of that
# dimension with all zeros, but if a sequence of numbers is provided, it pro-
# duces a vector with coordinates based on that sequence.

import collections


class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """
        If d is a number creates a d-dimensional vector of zeros.
        Else if d is a sequence of numbers, creates a lend(d)-dimensional
        vector with the values of d.
        """
        if not isinstance(d, (int, float, collections.Sequence)):
            raise TypeError("d must be a number or a sequence type")
        if isinstance(d, (int, float)):
            self._coords = [0]*d
        else:
            self._coords = []
            for i in range(len(d)):
                if not isinstance(d[i], (int, float)):
                    raise TypeError(
                        "elements of the sequence must be a number")
                self._coords.append(d[i])

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, i):
        """Return jth coordinate of vector."""
        return self._coords[i]

    def __setitem__(self, i, val):
        """Set jth coordinate of vector to given value."""
        self._coords[i] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            # relies on len method
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result

    def __radd__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result

    def __sub__(self, other):
        """Return self - other's result of two vectors."""
        if len(self) != len(other):
            # relies on len method
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] - other[i]
        return result

    def __mul__(self, x):
        """
        If x is a number returns a new Vector where each element is multiplied by x
        else if x is a Vector returns the dot product of the two Vectors
        """
        if not isinstance(x, (int, float, Vector)):
            raise TypeError("x must be a number or a Vector")
        if isinstance(x, (int, float)):
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i] * x
        else:
            if len(self) != len(x):
                raise ValueError("dimensions must agree")
            result = sum((self[i] * x[i] for i in range(len(self))))
        return result

    def __rmul__(self, scale):
        """Returns a new Vector where each element is multiplied by scale"""
        if not isinstance(scale, (int, float)):
            raise TypeError("scale must be a number")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] * scale
        return result

    def __neg__(self):
        """Returns a new Vector with all its values negated."""
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] * -1
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other        # rely on existing eq definition

    def __str__(self):
        """Produce string representation of vector."""
        # adapt list representation
        return f"<{str(self._coords)[1:-1]}>"


if __name__ == '__main__':
    # the following demonstrates usage of a few methods
    v = Vector(5)              # construct five-dimensional <0, 0, 0, 0, 0>
    v[1] = 23                  # <0, 23, 0, 0, 0> (based on use of __setitem__)
    v[-1] = 45                 # <0, 23, 0, 0, 45> (also via __setitem__)
    print(v[4])                # print 45 (via __getitem__)
    u = v + v                  # <0, 46, 0, 0, 90> (via __add__)
    print(u)                   # print <0, 46, 0, 0, 90>
    total = 0
    for entry in v:            # implicit iteration via __len__ and __getitem__
        total += entry

    g = u - v                  # tests __sub__
    print(g)
    print(v)
    print(g == v)

    negatedg = -g              # test __neg__
    print(negatedg)
    print(g)

    # test __add__ with simple list as right-hand operand
    newVector = g + [1, 2, 3, 4, 5]
    print(newVector)

    # test __radd__ with simple list as left-hand operand
    moreNewVector = [1, 2, 3, 4, 5] + g
    print(moreNewVector)

    # test __mul__
    multipliedVector = g * 3
    print(g)
    print(multipliedVector)

    # test __rmul__
    anotherMultipliedVector = 3 * g
    print(g)
    print(anotherMultipliedVector)

    # test dot product of __mul__
    print(u)
    print(g)
    print(g * u)

    # test constructor with a list
    lVector = Vector([1, 2, 3.2, 4])
    print(lVector)

    # test constructor with tuple
    tVector = Vector((1, 2.5, 3, 4))
    print(tVector)

    # test with a string raises error
    # sVector = Vector("hello")
    # print(sVector)
