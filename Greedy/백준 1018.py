import sys
def counter(value):
    cnt=0
    for n,i in enumerate(graph):
        if n%2==0:
            for q in range(len(i)):
                if q%2==0 and i[q]!=alpha[value]:
                    cnt+=1
                elif q%2==1 and i[q]==alpha[value]:
                    cnt+=1
        else:
            for q in range(len(i)):
                if q%2==0 and i[q]==alpha[value]:
                    cnt+=1
                elif q%2==1 and i[q]!=alpha[value]:
                    cnt+=1           
    return cnt
n,m=map(int,sys.stdin.readline().split())
graphs=[list(sys.stdin.readline().rstrip()) for _ in range(n)]
alpha=['W','B']
min_value=1e9
for i in range(m-7):
    for q in range(n-7):
        graph=[row[i:i+8] for row in graphs[q:q+8]]
        tmp=min(counter(0),counter(1))
        min_value=min(tmp,min_value)
print(min_value)