def is_natural(n):
    """
    Natural number as start from 0
    """
    return isinstance(n, int) and n > -1


def is_u32(n: int) -> bool:
    """
    check if a number fits inside an unsigned 32-bit integer range.
    0 <= n <= 4294967295 (0xFFFFFFFF)
    """
    return 0 <= n <= 0xFFFFFFFF
