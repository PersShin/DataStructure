import sys
from collections import deque
def BFS():
    queue=deque()
    queue.append((result_a-1,0))
    visited[result_a-1]=1
    while queue:
        tmp,count=queue.popleft()
        if tmp==result_b-1:
            return count 
        for i in graph[tmp]:
            if visited[i]==0:
                queue.append((i,count+1))
                visited[i]=1
    return -1
num=int(input())
result_a,result_b=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(num)]
visited=[0 for _ in range(num)]
for _ in range(int(input())):
    tmp_a,tmp_b=map(int,sys.stdin.readline().split())
    graph[tmp_a-1].append(tmp_b-1)
    graph[tmp_b-1].append(tmp_a-1)
print(BFS())