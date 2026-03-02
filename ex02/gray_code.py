from utils import is_int


def gray_code(n: int) -> int:
    """
    Convert an integer to its Gray code representation.

    Gray code is computed using:
        gray_code(n) = n ^ (n >> 1)

    """
    if not is_int(n):
        raise TypeError("number must be integer")
    
    if n < 0:
        raise ValueError("positive integers only")

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
        
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
