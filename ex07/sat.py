
from truth_table import extract_variables, build_tree, evaluate_tree
from negation_normal_form import push_negations, eliminate_imp_eq
from node import Node
from conjunctive_normal_form import distributivity_to
from itertools import product


def sat(formula: str) -> bool:
    """
    Return True if the formula is satisfiable.
    """
    root = build_tree(formula)
    root = eliminate_imp_eq(root) # eliminate equivalence and implication
    root = push_negations(root)    #NNF
    root = distributivity_to(root) #CNF

    variables = extract_variables(formula)
    for values_tuple in product([False, True], repeat=len(variables)):  # get all combinations of True, False for all variables z^len(variables)
        values = dict(zip(variables, values_tuple))                     # for each combinations(values_tuple), evaluate against the expression tree
    
        result = evaluate_tree(root, values)                            # to get result for all combinations.
        if result:
            return True

    return False


def main():
    """main"""

    try:

        print(sat("AB|"))  #true
        print(sat("AB&"))  #true
        print(sat("AA!&")) #false
        print(sat("AA^"))  #false
        
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
