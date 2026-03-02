from natural_number_error import NaturalNumberError
from utils import is_natural


def adder(a: int, b: int) -> int:
    """
    Add two natural numbers using bit operations
    """
    if not is_natural(a) or not is_natural(b):
        raise NaturalNumberError("Both numbers must be natural numbers")
    
    while b != 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry

    return a


def main():
    """main"""

    try:

        print(adder(1, 2)) #3
        print(adder(0, 2)) #2
        print(adder(1, 0)) #1
        print(adder(99, 1)) #100
        print(adder(887, 1)) #888
        
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
