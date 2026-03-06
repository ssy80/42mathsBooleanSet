from node import Node


def print_tree(node: Node, indent=0):
    if node is not None:
        print_tree(node.right, indent + 4)
        print(" " * indent + node.value)
        print_tree(node.left, indent + 4)


'''
If node is literal (base case) -> return value
If unary -> evaluate child -> apply operator ! (negate)
If binary -> evaluate left & right -> apply operator to the left and right result
'''
def evaluate_tree(node: Node) -> bool:
    """
    Recursively evaluate the tree.
    """

    # Base case: literal (0, 1)
    if node.value == "0":
        return False
    if node.value == "1":
        return True

    # Unary operator (negation)
    if node.value == "!":
        return not evaluate_tree(node.left)    # negate the result from eval

    # Binary operators (&,|,^,=,>)
    left_val = evaluate_tree(node.left)
    right_val = evaluate_tree(node.right)

    if node.value == "&":                       # and
        return left_val and right_val

    if node.value == "|":                       # or - True if any one is True or all is True - (0,1),(1,0),(1,1)
        return left_val or right_val

    if node.value == "^":                       # xor - True if exactly one is True - (1,1 = 0), (1,0 = 1), (0,1 =1)
        return left_val ^ right_val

    if node.value == ">":                       # implication - A > B  ≡  ¬A ∨ B = ((not A) or B) "If it rains(A), then the ground is wet(B)."
        return (not left_val) or right_val

    if node.value == "=":                       # equivalence
        return left_val == right_val

    raise ValueError(f"unknown operator: {node.value}")


'''
RPN parsing rule:
Literal(0, 1) → push node
Unary(!) → pop 1, build node, push
Binary(&,|,^,>,=) → pop 2, build node, push
'''
def build_tree(formula: str) -> Node:
    """
    Build an expression tree from a propositional formula
    written in Reverse Polish Notation (RPN).
    """
    binary_opr = {"&", "|", "^", ">", "="}
    stack = []

    for token in formula:

        if token in ("0", "1"):                             # Literal 0, 1
            stack.append(Node(token))

        elif token == "!":                                  # unary operator
            if len(stack) == 0:                             # invalid, because "!" needs to stick to one node of literal, !0, !1
                raise ValueError("Invalid formula")

            child = stack.pop()
            stack.append(Node(token, left=child))

        elif token in binary_opr:                           # binary operators
            if len(stack) < 2:                              # must have at least 2 node in stack
                raise ValueError("Invalid formula")

            right = stack.pop()
            left = stack.pop()
            stack.append(Node(token, left, right))
        
        else:
            raise ValueError(f"Unknown token: {token}")

    if len(stack) != 1:
        raise ValueError("Invalid formula")

    return stack[0]


def eval_formula(formula: str) -> bool:
    """
    Build the expression tree (AST)
    Evaluate the tree
    """

    root_node = build_tree(formula)
    result = evaluate_tree(root_node)
    
    return result


def main():
    """main"""

    try:

        print(eval_formula("10&")) # false
        print(eval_formula("10|")) # true
        print(eval_formula("11>")) # true
        print(eval_formula("10=")) # false
        print(eval_formula("1011||=")) # true
        
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
