import sys
from collections import deque
def alignment():
    result=[]
    queue=deque()
    for i in range(1,N+1):
        if visited[i]==0:
            queue.append(i)

    while queue:
        tmp=queue.popleft()
        result.append(tmp)
        for i in graph[tmp]:
            visited[i]-=1
            if visited[i]==0:
                queue.append(i)

    return ' '.join(map(str,result))
    
N,M=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
visited=[0 for _ in range(N+1)]
for _ in range(M):
    tmp_x,tmp_y=map(int,sys.stdin.readline().split())
    graph[tmp_x].append(tmp_y)
    visited[tmp_y]+=1
print(alignment())