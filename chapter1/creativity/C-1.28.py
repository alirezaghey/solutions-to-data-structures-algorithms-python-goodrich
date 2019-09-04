from typing import List


def norm(v: List[int], p: int = 2) -> int:
    """
    norm(v,p) returns the p-norm of v
    norm(v) returns the Euclidean norm of v
    Time complexity: O(n) where n == len(v)
    Space complexity: O(1)
    """
    result = 0
    for vector in v:
        result += vector ** p
    return result ** (1/p)


print(norm([4, 3]))
print(norm([4, 3], 2))
print(norm([1, 2, 3, 4], 3))
