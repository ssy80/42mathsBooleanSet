from utils import is_int


def gray_code(n: int) -> int:
    """
    Convert an integer to its Gray code representation.
    Gray code is a way to represent an integer in binary so that two consecutive numbers differ by only one bit.
    Gray code is used to reduce errors when numbers change, especially in hardware like sensors and encoders.
    Gray code ensures only one bit changes between consecutive numbers, making transitions safer and more reliable
    Normal:
        3  = 011     # 3 bits changes
        4  = 100
    Gray code:       # 1 bit change
        3 = 010
        4 = 110
    Gray code is computed using:
        gray_code(n) = n ^ (n >> 1)
    """
    if not is_int(n):
        raise TypeError("number must be integer")
    
    return (n ^ (n >> 1))


def main():
    """main"""

    try:

        print(gray_code(0)) #0
        print(gray_code(1)) #1
        print(gray_code(2)) #3
        print(gray_code(3)) #2
        print(gray_code(4)) #6
        print(gray_code(5)) #7
        print(gray_code(6)) #5
        print(gray_code(7)) #4
        print(gray_code(8)) #12

        print(gray_code(-8)) # 4               
        
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
