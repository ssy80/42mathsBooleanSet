import string
from node import Node
from itertools import product


def extract_variables(formula: str):
    """
    Extract unique variables name(symbol) from formula
    """
    variable_set = set()

    for c in formula:
        if c.isupper():
            variable_set.add(c)

    return sorted(variable_set)


def evaluate_tree(node: Node, values: dict) -> bool:
    """
    Recursively evaluate the tree.
    """

    # Base case: symbols truth value
    if node.value.isupper():
        return values[node.value]

    # Unary operator (negation)
    if node.value == "!":
        return not evaluate_tree(node.left, values)    # negate the result from eval

    # Binary operators (&,|,^,=,>)
    left_val = evaluate_tree(node.left, values)
    right_val = evaluate_tree(node.right, values)

    if node.value == "&":
        return left_val and right_val

    if node.value == "|":                       # or - True if any one is True or all is True - (0,1),(1,0),(1,1)
        return left_val or right_val

    if node.value == "^":                       # xor - True if exactly one is True - (1,1 = 0), (1,0 = 1), (0,1 =1)
        return left_val ^ right_val

    if node.value == ">":                       # implication - A > B  ≡  ¬A ∨ B = ((not A) or B) "If it rains(A), then the ground is wet(B)."
        return (not left_val) or right_val

    if node.value == "=":
        return left_val == right_val

    raise ValueError(f"unknown operator: {node.value}")


def build_tree(formula: str) -> Node:
    """
    Build an expression tree from a propositional formula
    written in Reverse Polish Notation (RPN).
    """
    symbols = list(string.ascii_uppercase)
    binary_opr = {"&", "|", "^", ">", "="}                  #set
    stack = []

    for token in formula:

        if token in (symbols):                             # symbols A-Z
            stack.append(Node(token))

        elif token == "!":                                  # unary operator
            if len(stack) == 0:                             # invalid, because "!" needs to stick to one node of literal, !0, !1
                raise ValueError("invalid formula")

            child = stack.pop()
            stack.append(Node(token, left=child))

        elif token in binary_opr:                           # binary operators
            if len(stack) < 2:                              # must have at least 2 node in stack
                raise ValueError("invalid formula")

            right = stack.pop()
            left = stack.pop()
            stack.append(Node(token, left, right))

        else:                                               
            raise ValueError(f"unknown token: {token}")

    if len(stack) != 1:
        raise ValueError("invalid formula")

    return stack[0]


def print_truth_table(formula: str):
    """
    Extract unique symbols from formula
    Build the expression tree
    Generate all combinations for the symbols 2^n
    Evaluate tree for all combinations to get each result
    Print the truth table
    """
    variables = extract_variables(formula)
    root = build_tree(formula)

    # Header
    print(" | ".join(variables) + " | =")
    print("-" * (4 * len(variables) + 2))

    # Generate all combinations
    for values_tuple in product([False, True], repeat=len(variables)):  # get all combinations of True, False for all variables z^len(variables)
        values = dict(zip(variables, values_tuple))                     # for each combinations(values_tuple), evaluate against the expression tree
        result = evaluate_tree(root, values)                            # to get result for all combinations.

        row = " | ".join(str(int(values[v])) for v in variables)
        print(f"{row} | {int(result)}")


def main():
    """main"""

    try:

        print_truth_table("AB&C|")
        
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
