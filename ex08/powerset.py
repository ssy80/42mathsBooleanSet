from itertools import chain, combinations


def powerset(s: set[int]) -> list[set[int]]:
    """
    Loop subset len
    Get tuple of every combinations of the subset for each
    """
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
        
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
