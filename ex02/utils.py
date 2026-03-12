def is_natural(n):
    """
    Natural number as start from 0
    """
    return type(n) is int and n > -1


def is_int(n):
    """
    Return true is n is an integer
    """
    return type(n) is int


def is_u32(n: int) -> bool:
    """
    check if a number fits inside an unsigned 32-bit integer range.
    0 <= n <= 4294967295 (0xFFFFFFFF)
    """
    return type(n) is int and 0 <= n <= 0xFFFFFFFF


def is_int_set(s: set[int]):
    """
    Check element in set is int
    """
    if not isinstance(s, set):
        raise ValueError("not a set")

    for i in s:
        if type(i) is not int:
            raise ValueError("number in set must be int")


def is_int_sets(sets: list[set[int]]) -> None:
    """
    Check every item is a set of integers.
    """
    if not all(isinstance(s, set) for s in sets):
        raise TypeError("each item in sets must be a set")
    if not all(type(x) is int for s in sets for x in s):
        raise TypeError("number in set must be int")
