from truth_table import build_tree
from node import Node


def is_int_set(sets: list[set]) -> bool:
    """
    Check item in sets are int value
    """
    result = all(isinstance(x, int) for s in sets for x in s)
    if not result:
        raise TypeError("number in set must be integer")


def extract_variables_non_sort(formula: str)-> list[str]:
    """
    Extract unique variables name(symbol) from formula non sorted
    """
    variable_set = []

    for c in formula:
        if c.isupper() and c not in variable_set:
            variable_set.append(c)

    return variable_set


def  match_symbol_to_sets(variables: list[str], sets: list[set[int]])-> dict:
    """
    Return a dict matching symbols to input sets
    """
    result_dict = {a: b for a,b in zip(variables, sets)}
    return result_dict


'''
Universe_set is needed because some logical operations require knowing what elements are outside a set.
    negate ¬
    implication >
    equivalence = 
    e.g ¬A = (U - A) - returns whats outside of A (universe_set - A)
'''
def evaluate_tree(node: Node, values: dict[str, set[int]], universe: set[int]) -> set[int]:
    """
    Universe should only contain elements appearing in the input sets
    Recursively evaluate the tree with sets operations
    """

    # Symbols
    if node.value.isupper():
        return values[node.value]

    # Negation
    if node.value == "!":                       # negation - !A = (U - A)
        return universe - evaluate_tree(node.left, values, universe)

    # operators (&,|,^,=,>)
    left_val = evaluate_tree(node.left, values, universe)
    right_val = evaluate_tree(node.right, values, universe)

    if node.value == "&":                       # intersection - (A n B) elements in A or B but not in both, intercepted part
        return left_val & right_val            
        
    if node.value == "|":                       # union - (A u B) elements that are in A or in B or in both, all of A,B
        return left_val | right_val

    if node.value == "^":                       # xor # symmetric difference - elements in A or B but not both, exclude intercepted part
        return left_val ^ right_val 

    if node.value == ">":                       # implication - A > B = ¬A u B = (U-A) u B
        return (universe - left_val) | right_val

    if node.value == "=":                       # equivalence - A <=> B = (A ∩ B) ∪ (¬A ∩ ¬B) - it is either in both sets or in neither set
        return (left_val & right_val) | ((universe - left_val) & (universe - right_val))
        
    raise ValueError(f"unknown operator: {node.value}")


def eval_set(formula: str, sets: list[set[int]]) -> set[int]:
    """
    Validate formula and list of sets has correct type and length
    Generate Universe Set
    Build tree
    Evaluate tree
    """
    is_int_set(sets)
    variables = extract_variables_non_sort(formula)
    if len(sets) != len(variables):
        raise ValueError("invalid list of sets")
    symbol_set_dict = match_symbol_to_sets(variables, sets)
    universe_set = set().union(*sets) # create a universe set from union of the list of sets - (empty set) u ({1,2,3}) u ({3,4,5})

    root = build_tree(formula)

    return evaluate_tree(root, symbol_set_dict, universe_set)


def main():
    """main"""

    try:
        
        print(eval_set("AB&", [{0, 1, 2},{0, 3, 4}])) # [0]
        print(eval_set("AB|", [{0, 1, 2},{3, 4, 5}])) # [0, 1, 2, 3, 4, 5]
        print(eval_set("A!", [{0, 1, 2}])) # []
        
        print(eval_set("CBBD!|&&", [{0, 1, 200}, {0, 1, 0}, {0, 1, 2}]))

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
