"""Reads through data and gives infix, postfix, and
answer to expressions"""
from stack import Stack
def main():
    """main loops through data and calls functions on them"""
    lyst = []
    file1 = open("D:\\UVU\\Code\\Fall2020\\Child-Stuff\\CS2420\\Mod4\\p4\\data.txt", 'r')
    lyst = file1.readlines()

    for expr in lyst:
        stripped_expr = expr.strip('\n')
        post = in2post(stripped_expr)
        answer = eval_postfix(str(post))
        print("Infix: " + stripped_expr)
        print("Postfix: " + post)
        print("Answer: " + str(answer))
        print()

def op_pop(stack):
    """Helper method test if stack is empty and raises syntax error if it is"""
    if stack.isEmpty():
        raise SyntaxError()
    return stack.pop()

def in2post(expr):
    """Turns a expression from infix to postfix epression"""
    if not isinstance(expr, str):
        raise ValueError()
    symb = {'*': 3, '/': 3, '+':2, '-':2, '(': 1}
    expression = expr.split(' ')
    op_stack = Stack()
    final_lyst = []

    for tok in expression:
        if tok.isalpha() or tok.isdigit():
            final_lyst.append(tok)
        elif tok == '(':
            op_stack.push(tok)
        elif tok == ')':
            top_token = op_pop(op_stack)
            while top_token != '(':
                final_lyst.append(top_token)
                top_token = op_pop(op_stack)
        else:
            while (not op_stack.isEmpty()) and (symb[op_stack.top()] >= symb[tok]):
                final_lyst.append(op_pop(op_stack))
            op_stack.push(tok)
    while not op_stack.isEmpty():
        final_lyst.append(op_pop(op_stack))
    return " ".join(final_lyst)


def eval_postfix(expr):
    """Evaluates a postfix expression"""
    if not isinstance(expr, str):
        raise ValueError()
    op_stack = Stack()
    expression = expr.strip().split(' ')

    for tok in expression:
        if tok.isdigit():
            op_stack.push(int(tok))
        else:
            right_op = op_pop(op_stack)
            left_op = op_pop(op_stack)
            op_stack.push(op_help(tok, left_op, right_op))
    return op_pop(op_stack)

def op_help(oper, left_op, right_op):
    """Helper method does math on operands and returns them"""
    if oper == '+':
        return left_op + right_op
    elif oper == '-':
        return left_op - right_op
    elif oper == '*':
        return left_op * right_op
    else:
        return left_op / right_op

if __name__ == "__main__":
    main()
