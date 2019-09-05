# P-1.30 Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.


def timesToDivide(n: int) -> int:
    """
    We will repeatedly divide n by two until it is less than two

    Time complexity: O(log n)
    Space complexity: O(1)
    """
    if n <= 2:
        raise ValueError("Value must be greater than 2!")
    count = 0
    while n >= 2:
        n //= 2
        count += 1
    return count


def timesToDivideBinary(n: int) -> int:
    """
    Using the fact that integers are hold in binary form
    and that a binary right shift equals division by two
    we will right shift n until n is less than two (only its least significant bit is set)
    This approach is probably more efficient as bit operation are normally very easy to do
    for computers, but it needs to be tested to make sure.
    This algorithms time and space complexity does not change compared to the previous one.

    Time complexity: O(log n)
    Space complexity: O(1)
    """
    if n <= 2:
        raise ValueError("Value must be greater than 2!")
    count = 0
    while n | 1 != 1:
        n >>= 1
        count += 1
    return count


if __name__ == "__main__":
    print(timesToDivide(10), timesToDivideBinary(10))
    print(timesToDivide(15), timesToDivideBinary(15))
    print(timesToDivide(34567), timesToDivideBinary(34567))
    print(timesToDivide(32985469), timesToDivideBinary(32985469))
    print(timesToDivide(139453848345), timesToDivideBinary(139453848345))
