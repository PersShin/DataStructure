import sys
def finder():
    tmp=0
    for i in range(m-1,-1,-1):
        if wheel[tmp]!='?' and wheel[tmp]!=alpha[i]:
            return False
        if alpha[i] in wheel and wheel[tmp]!=alpha[i]:
            return False
        wheel[tmp]=alpha[i]
        tmp=(tmp+int(num_move[i]))%n
        print(wheel)
    return True
n,m=map(int,sys.stdin.readline().split())
wheel=['?' for _ in range(n)]
num_move=[0 for _ in range(m)]
alpha=[0 for _ in range(m)]
for i in range(m):
    num_move[i], alpha[i] = sys.stdin.readline().split()
if finder():
    for i in wheel:
        print(i,end='')
else:
    print('!')