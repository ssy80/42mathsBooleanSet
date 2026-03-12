from truth_table import extract_variables, build_tree
from negation_normal_form import push_negations, eliminate_imp_eq, to_rpn, eliminate_xor
from node import Node


'''
Distributivity to NNF to get CNF
(A ∧ (B V C)) <=> ((A ∧ B) V (A ∧ C))
(A V (B ∧ C)) <=> ((A V B) ∧ (A V C))
# e.g
# A ∧ ((B v C) ∧ (B V D))
# A ∧ ((B V C) ∧ (B V D))   ->  ABC|BD|&&
'''
def distributivity_to(node: Node) -> Node:
    """
    Apply distributivity rules to NNF to get CNF
    """

    # Literal / negated literal
    if node.value.isupper() or node.value == "!":
        return node

    # Recursively process children first
    left = distributivity_to(node.left)
    right = distributivity_to(node.right)

    # Apply distributivity only when node is |OR
    if node.value == "|":

        # A | (B & C)
        if right.value == "&":
            new_left = distributivity_to(
                Node("|", left, right.left)
            )
            new_right = distributivity_to(
                Node("|", left, right.right)
            )
            return Node("&", new_left, new_right)

        # (A & B) | C
        if left.value == "&":
            new_left = distributivity_to(
                Node("|", left.left, right)
            )
            new_right = distributivity_to(
                Node("|", left.right, right)
            )
            return Node("&", new_left, new_right)

    return Node(node.value, left, right)


'''
It is an AND of OR-clauses - (clause1) ^ (clause2) ^ (clause3), no negation to (clause) only to literals
e.g (A V B), (¬A V ¬C) ∧ (¬B V ¬C), (A V ¬B) ∧ (¬C V D V E), (A V B V C)
'''
def conjunctive_normal_form(formula: str) -> str:
    """
    """
    root = build_tree(formula)
    root = eliminate_imp_eq(root) # eliminate equivalence and implication
    root = eliminate_xor(root)
    root = push_negations(root)
    root = distributivity_to(root)

    return to_rpn(root)


def main():
    """main"""

    try:

        print(conjunctive_normal_form("AB&!"))    #A!B!|
        print(conjunctive_normal_form("AB|!"))    #A!B!&
        print(conjunctive_normal_form("AB|C&"))   #AB|C&
        print(conjunctive_normal_form("AB|C|D|")) #ABCD|||, AB|C|D|
        print(conjunctive_normal_form("AB&C&D&")) #ABCD&&&, AB&C&D&
        print(conjunctive_normal_form("AB&!C!|")) #A!B!C!||, A!B!|C!|
        print(conjunctive_normal_form("AB|!C!&")) #A!B!C!&&, A!B!&C!&

        print(conjunctive_normal_form("ABCD&|&")) #ABC|BD|&&

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
