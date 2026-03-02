

def eval_formula(formula: str) -> bool:
    """
    
    """
    
    #return 


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
