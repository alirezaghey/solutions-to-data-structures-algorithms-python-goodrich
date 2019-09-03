# C-1.26 Write a short program that takes as input three integers, a, b, and c, from
# the console and determines if they can be used in a correct arithmetic
# formula (in the given order), like “a + b = c,” “a = b − c,” or “a ∗ b = c.”


def canBeUsed() -> str:
    a = int(input("Type in your first char: "))
    b = int(input("Type in your first char: "))
    c = int(input("Type in your first char: "))

    result = []
    if a + b == c:
        result.append("a + b = c")
    if a == b - c:
        result.append("a = b - c")
    if a * b == c:
        result.append("a * b = c")
    if result:
        print("\n".join(result))
    else:
        print("No match found!")


canBeUsed()
