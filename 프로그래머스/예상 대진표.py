import math
def solution(n,a,b):
    answer=int(math.log2(n))
    n=n/2
    for i in range(answer,0,-1):
        print(a,b,n)
        if(a>n and b<=n) or (a<=n and b>n):
            return answer
        elif(a>n and b>n):
            a-=n
            b-=n
            n=n/2
            print(n)
        else: n=n/2
        answer-=1

N=8
A=5
B=6
print(solution(N,A,B))