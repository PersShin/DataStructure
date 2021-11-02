OPERATORS = set(['+', '-', '*', '/'])  # set of operators
PRIORITY = {'+':1, '-':1, '*':2, '/':2}
def answer(token):
    stacker=[]
    for i in token:
        if(i not in OPERATORS):
            stacker.append(i)
        else:
            try:
                tmp=int(stacker.pop())
                temp=int(stacker.pop())
            except: print('계산식이 잘못 되었습니다!')
            if(i=='+'):
                stacker.append(tmp+temp)
            elif(i=='-'):
                stacker.append(temp-tmp)
            elif(i=='*'):
                stacker.append(temp*tmp)
            else:
                stacker.append(temp/tmp)
    print(stacker.pop())
def Infix2Postfix(expression):
    stacker=[]
    token=''
    expression=expression.replace(' ','')
    for i in expression:
        if(i=='('):
            stacker+=i
        elif(i==')'):
            while stacker and stacker[-1]!='(':
                token+=stacker.pop()
            stacker.pop()
        elif(i not in OPERATORS):
            token+=i
        else:
            while stacker and stacker[-1]!='(' and PRIORITY[i]<=PRIORITY[stacker[-1]]:
                token+=stacker.pop()
            stacker.append(i)
    while stacker and stacker[-1]!='(':
        token+=stacker.pop()
    print(token)
    answer(token)
expression='(1+(2*(3+4)*7))'
Infix2Postfix(expression)