class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

import string

def infix2postfix(expression):
    prec = {'*': 3, '/': 3, '+':2, '-':2, '(': 1}
    
    operator_stack = Stack()
    result_list = []
    token_list = expression.split()
    
    for token in token_list:
        if token.isalpha() or token.isdigit():
            result_list.append(token)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            top_token = operator_stack.pop()
            while top_token != '(':
                result_list.append(top_token)
                top_token = operator_stack.pop()
        else: # regular operators
            while (not operator_stack.isEmpty()) and (prec[operator_stack.peek()] >= prec[token]):
                result_list.append(operator_stack.pop())
            operator_stack.push(token)
    
    while not operator_stack.isEmpty():
        result_list.append(operator_stack.pop())
        
    return " ".join(result_list)

print(infix2postfix("( 12 * 2 ) - 5 + ( 3 - 4 )"))

def postfix_eval(expression):
    operand_stack = Stack()
    token_list = expression.split()
    
    for token in token_list:
        if token.isdigit():
            operand_stack.push(int(token))
        else:
            rightOperand = operand_stack.pop()
            leftOperand = operand_stack.pop()
            operand_stack.push(do_math(token, leftOperand, rightOperand))
    
    return operand_stack.pop()

def do_math(operator, leftoperand, rightoperand):
    if operator == '+':
        return leftoperand + rightoperand
    elif operator == '-':
        return leftoperand - rightoperand
    elif operator == '*':
        return leftoperand * rightoperand
    else:
        return leftoperand / rightoperand

# print(postfix_eval("1 2 + 3 * 4 5 - 6 7 + * -"))