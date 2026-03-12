from itertools import combinations
from utils import is_int_set


def powerset(s: set[int]) -> list[set[int]]:
    """
    Loop subset len.
    Get tuple of every combinations of the subset for each.
    Generates all possible groups of size r chosen from s, without repetition.
    """
    is_int_set(s)
    return [set(c) for r in range(len(s)+1) for c in combinations(s,r)]

'''
same as above list comprehension [set(c) for r in range(len(s)+1) for c in combinations(s,r)]
result = []

    for r in range(len(s) + 1):
        for c in combinations(s, r):
            result.append(set(c))
'''


def main():
    """main"""

    try:

        print(powerset({1, 2, 3}))
        print(powerset({1, 2, 3, 4}))
        print(powerset({0}))
        print(powerset(set()))          # set() = empty set

        print(powerset({"a"})) #error
        #print(powerset({1.99})) #error

        
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
