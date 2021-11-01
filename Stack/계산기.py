OPERATORS = set(['+', '-', '*', '/', '^'])  # set of operators
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3}
def Infix2Postfix(expression):
    stacker=[]
    token=''
    expression=expression.replace(' ','')
    for i in expression:
        if(i=='('):
            stacker+=i
        elif(i==')'):
            while stacker and stacker[-1]!='(':
                token+=stacker.pop(-1)
            stacker.pop(-1)
        elif(i not in OPERATORS):
            token+=i
        else:
            while stacker and stacker[-1]!='(' and PRIORITY[i]<=PRIORITY[stacker[-1]]:
                token+=stacker.pop(-1)
            stacker.append(i)
    while stacker and stacker[-1]!='(':
        token+=stacker.pop(-1)
    print(token)
expression='(A+(C+D*F+T*A)*B/C)'
Infix2Postfix(expression)