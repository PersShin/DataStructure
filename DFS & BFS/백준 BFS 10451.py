import sys
from collections import deque
total=int(input())
for i in range(total):
    n=int(input())
    data=list(map(int, sys.stdin.readline().split()))
    num=1
    answer=0
    starter=0
    visited=[False]*n
    queue=deque()
    while num!=n and starter<n:
        if len(queue)==0 and visited[starter]==False:
            answer+=1
            queue.append(data[starter])
            visited[starter]=True
        elif len(queue)==0:
            starter+=1
        else:
            tmp=queue.popleft()
            if visited[tmp-1]==False:
                queue.append(data[tmp-1])
                num+=1
                visited[tmp-1]=True
    print(answer, end='\n')