from truth_table import extract_variables, build_tree
from negation_normal_form import push_negations, eliminate_imp_eq, to_rpn
from node import Node


'''
Distributivity
(A ∧ (B ∨ C)) ⇔ ((A ∧ B) ∨ (A ∧ C))
(A ∨ (B ∧ C)) ⇔ ((A ∨ B) ∧ (A ∨ C))
'''
def distributivity_to(node: Node) -> Node:
    """
    """

    # Literal or negated literal
    if node.value.isupper() or node.value == '!':
        return node

    # Recursively process children first
    left = distributivity_to(node.left)
    right = distributivity_to(node.right)

    # Apply distributivity only when node is OR
    if node.value == '|':
        
        # Case: A | (B & C)
        if right.value == '&':
            new_left = distributivity_to(
                Node('|', left, right.left)
            )
            new_right = distributivity_to(
                Node('|', left, right.right)
            )
            return Node('&', new_left, new_right)

        # Case: (A & B) | C
        if left.value == '&':
            new_left = distributivity_to(
                Node('|', left.left, right)
            )
            new_right = distributivity_to(
                Node('|', left.right, right)
            )
            return Node('&', new_left, new_right)

    # Otherwise return rebuilt node
    return Node(node.value, left, right)


'''
It is an AND of OR-clauses - (clause1) ^ (clause2) ^ (clause3), no negation to (clause) only to literals
e.g (A ∨ B), (¬A ∨ ¬C) ∧ (¬B ∨ ¬C), (A ∨ ¬B) ∧ (¬C ∨ D ∨ E)
'''
def conjunctive_normal_form(formula: &str) -> str:
    """
    """
    root = build_tree(formula)
    root = eliminate_imp_eq(root) # convert (A <=> B) <=> ((A => B) ∧ (B => A))
    root = eliminate_imp_eq(root) # convert (A => B) <=> (¬A ∨ B)
    root = push_negations(root)

    root = distributivity_to(root)

    return to_rpn(root)

def main():
    """main"""

    try:

        print(conjunctive_normal_form("AB&!"))    #A!B!|
        print(conjunctive_normal_form("AB|!"))    #A!B!&
        print(conjunctive_normal_form("AB|C&"))   #AB|C&
        print(conjunctive_normal_form("AB|C|D|")) #ABCD|||
        print(conjunctive_normal_form("AB&C&D&")) #ABCD&&&
        print(conjunctive_normal_form("AB&!C!|")) #A!B!C!||
        print(conjunctive_normal_form("AB|!C!&")) #A!B!C!&&

    
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
