# R-2.11 In Section 2.3.3, we note that our Vector class supports a syntax such as
# v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
# a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
# Explain how the Vector class definition can be revised so that this syntax
# generates a new vector.


class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0]*d

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
