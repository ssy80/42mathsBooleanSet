def is_natural(n):
    """
    Natural number as start from 0
    """
    return isinstance(n, int) and n > -1


def is_int(n):
    """
    Return true is n is an integer
    """
    return isinstance(n, int)

def is_int_set(s: set[int]):
    """
    Check element in set is int
    """
    if not isinstance(s, set):
        raise ValueError("not a set")

    for i in s:
        if not isinstance(i, int):
            raise ValueError("not int set")

        