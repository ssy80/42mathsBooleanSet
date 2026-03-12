from utils import is_natural, is_u32


'''
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
'''


def multiplier(a: int, b: int) -> int:
    """
    Multiply two natural numbers (u32 int) using bitwise operations.
    0 <= a <= 4294967295
    0 <= b <= 4294967295
    """
    if not is_u32(a) or not is_u32(b):
        raise ValueError("input must be a u32 int between 0 and 4294967295")
    
    result = 0
    for i in range(32):           # fixed number of iterations for O(1) complexity
        if (b >> i) & 1:          # check i-th bit of b, if last bit 1
            result += a << i      # then add shifted a by i-th bit to result 
    return result


def main():
    """main"""

    try:

        print(multiplier(1, 2)) #2
        print(multiplier(0, 2)) #0
        print(multiplier(1, 0)) #0
        print(multiplier(99, 1)) #99
        print(multiplier(887, 1)) #887

        print(multiplier(4294967295, 4294967295))
        print(multiplier(-1,0))
        #print(multiplier(1, 4294967296))
        
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
