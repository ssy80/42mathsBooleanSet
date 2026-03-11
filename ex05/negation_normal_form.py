from truth_table import build_tree
from node import Node


def to_rpn(node: Node) -> str:
    """
    Convert tree to RPN
    """

    if node is None:
        return ""

    if node.value == "!":
        return to_rpn(node.left) + "!"
    
    if node.value.isupper():
        return node.value

    #  if operator &,|
    return to_rpn(node.left) + to_rpn(node.right) + node.value


def eliminate_imp_eq(node: Node) -> Node:
    """
    Convert equivalence to simpler form - (A <=> B) <=> (A => B) ∧ (B => A)
    Convert implication to simpler form - (A => B) <=> (¬A V B)
    """

    # Literal Symbols(A-Z)
    if node.value.isupper():
        return node

    # Negation
    if node.value == "!":
        return Node("!", eliminate_imp_eq(node.left))

    # Equivalence - (A <=> B) <=> (A => B) ∧ (B => A)
    if node.value == "=":
        left = eliminate_imp_eq(node.left)
        right = eliminate_imp_eq(node.right)

        new_node = Node("&", Node(">", left, right), Node(">", right, left))

        return eliminate_imp_eq(new_node)

    # Implication - (A => B) <=> (¬A ∨ B)
    if node.value == ">":
        return Node("|", Node("!", eliminate_imp_eq(node.left)), eliminate_imp_eq(node.right))
    
    # &AND / |OR
    return Node(node.value, eliminate_imp_eq(node.left), eliminate_imp_eq(node.right))


def push_negations(node: Node) -> Node:
    """
    Eliminate double negations - (¬¬A) <=> A
    If start with negation check De Morgan's laws
        ¬(A V B) <=> (¬A ∧ ¬B)
        ¬(A ∧ B) <=> (¬A V ¬B)
    """

    # Literal Symbols
    if node.value.isupper():
        return node

    # Negation
    if node.value == "!":
        child = node.left

        # Double negation: ¬¬A <=> A
        if child.value == "!":
            return push_negations(child.left)

        # De Morgan &AND
        if child.value == "&":
            return Node("|", push_negations(Node("!", child.left)), push_negations(Node("!", child.right)))

        # De Morgan |OR
        if child.value == "|":
            return Node("&", push_negations(Node("!", child.left)), push_negations(Node("!", child.right)))

        return Node("!", push_negations(child))

    # &AND / |OR
    return Node(node.value, push_negations(node.left), push_negations(node.right))


def eliminate_xor(node: Node) -> Node:
    """
    Convert XOR to &, |, ! only.
    A ^ B <=> (A | B) & !(A & B)
    """
    if node.value.isupper():
        return node

    if node.value == "!":
        return Node("!", eliminate_xor(node.left))

    if node.value == "^":
        left = eliminate_xor(node.left)
        right = eliminate_xor(node.right)

        return Node(
            "&",
            Node("|", left, right),
            Node("!", Node("&", left, right)),
        )

    return Node(node.value, eliminate_xor(node.left), eliminate_xor(node.right))


'''
Negation normal form (NNF) 
only uses the operators:
∧ (AND)
V (OR)
¬ (NOT)
All NOTs are pushed all the way down to the literals
No negation is allowed to wrap a compound expression
'''
def negation_normal_form(formula: str)-> str:
    """
    Build tree
    Eliminate equivalence(<=>) from tree
    Eliminate implication(=>) from tree
    Convert tree to rpn
    """
    root = build_tree(formula)
    root = eliminate_imp_eq(root) # eliminate equivalence and implication
    root = eliminate_xor(root)
    root = push_negations(root)

    return to_rpn(root)
   

def main():
    """main"""

    try:

        print(negation_normal_form("AB&!"))   #A!B!|
        print(negation_normal_form("AB|!"))   #A!B!&
        print(negation_normal_form("AB>"))    #A!B|
        print(negation_normal_form("AB="))    #AB&A!B!&| or A!B|B!A|&
        print(negation_normal_form("AB|C&!")) #A!B!&C!|

        print(negation_normal_form("AB!!|C&!")) #A!B!&C!|

        print(negation_normal_form("AB!!^C&!")) #A!B!&AB&|C!|

    
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
