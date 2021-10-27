def printer(a):
    print('<',end=' ')
    for i in a:
        print(i,end=' ')
    print('>')
def boolean(n,a,np=True):
    if(n==0):
        printer(a)
        a=[]
    else:
        a.append(np)
        boolean(n-1,a,np)
        np=not np
        a.pop(-1)
        a.append(np)
        boolean(n-1,a,np)
        a.pop(-1)
