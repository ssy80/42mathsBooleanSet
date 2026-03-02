from natural_number_error import NaturalNumberError
from utils import is_natural
from adder import adder


def multiplier(a: int, b: int) -> int:
    """
    Multiply two natural numbers using bitwise operations.

    This function implements binary (shift-and-add) multiplication
    """
    if not is_natural(a) or not is_natural(b):
        raise NaturalNumberError("Both numbers must be natural numbers")
    
    result = 0

    while b != 0:
        if (b & 1) == 1:
            result = adder(result, a)
        
        a <<= 1
        b >>= 1

    return result


def main():
    """main"""

    try:

        print(multiplier(1, 2)) #2
        print(multiplier(0, 2)) #0
        print(multiplier(1, 0)) #0
        print(multiplier(99, 1)) #99
        print(multiplier(887, 1)) #887
        
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
