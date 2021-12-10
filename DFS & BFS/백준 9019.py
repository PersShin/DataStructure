import sys
from collections import deque
def BFS(x,y):
    queue=deque()
    queue.append((x,''))
    visited=set()
    visited.add(x)
    while queue:
        tmp,order=queue.popleft()
        if tmp==y:
            return order
        _,p=divmod(tmp*2,10000)
        if p not in visited:
            visited.add(p)
            queue.append((p,order+'D'))
        _,p=divmod(tmp-1,10000)
        if p not in visited:
            visited.add(p)
            queue.append((p,order+'S'))
        p,q=divmod(tmp,1000)
        if p+q*10 not in visited:
            visited.add(p+q*10)
            queue.append((p+q*10,order+'L'))
        p,q=divmod(tmp,10)
        if p+q*1000 not in visited:
            visited.add(p+q*1000)
            queue.append((p+q*1000,order+'R'))
n=int(input())
for i in range(n):
    num_x,num_y=list(map(int,sys.stdin.readline().split()))
    print(BFS(num_x,num_y))