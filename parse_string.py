from collections import defaultdict
 
 
def check_parentheses(expression):
    
    open_parentheses = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    close_parentheses = {v: k for k, v in open_parentheses.items()}
    
    parentheses_stacks = []
    
    result = True
    for c in expression:
        if c in open_parentheses.keys():
            parentheses_stacks.append(c)
        elif c in close_parentheses.keys():
            try:
                closed_par = parentheses_stacks.pop()
                if closed_par != close_parentheses[c]:
                    result = False
                    break
            except IndexError:
                result = False
                break
    return result and len(parentheses_stacks) == 0
