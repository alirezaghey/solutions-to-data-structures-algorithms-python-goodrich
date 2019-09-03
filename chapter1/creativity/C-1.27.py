# C-1.27 In Section 1.8, we provided three different implementations of a generator
# that computes factors of a given integer. The third of those implementa-
# tions, from page 41, was the most efficient, but we noted that it did not
# yield the factors in increasing order. Modify the generator so that it reports
# factors in increasing order, while maintaining its general performance ad-
# vantages.

from typing import List


def factors(n: int) -> List[int]:
    """
    Returns the factors of a number
    Time complexity: O(sqrt(n))
    Space complexity: O(1)
    """
    k = 1
    while k**2 < n:
        if n % k == 0:
            yield k
        k += 1

    k = int(n**(1/2))
    while k > 0:
        if n % k == 0:
            yield n // k
        k -= 1


print(list(factors(9)))
