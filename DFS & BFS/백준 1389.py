import sys
from collections import deque
def BFS(starter):
    visited=[0 for _ in range(num)]
    queue=deque()
    queue.append((starter,0))
    visited[starter]=-1
    while queue:
        tmp,count=queue.popleft()
        for n in graph[tmp]:
            if visited[n]==0:
                queue.append((n,count+1))
                visited[n]=count+1
    return sum(visited)+1
num,lines=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(num)]
for _ in range(lines):
    tmp_a,tmp_b=map(int, sys.stdin.readline().split())
    graph[tmp_a-1].append(tmp_b-1)
    graph[tmp_b-1].append(tmp_a-1)
answer=[]
for i in range(num):
    answer.append(BFS(i))
print(answer.index(min(answer))+1)