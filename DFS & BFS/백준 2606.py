import sys
from collections import deque
def BFS():
    queue=deque()
    queue.append(1)
    visited[1]=1
    cnt=0
    while queue:
        tmp=queue.popleft()
        for i in graph[tmp]:
            if visited[i]==0:
                queue.append(i)
                cnt+=1
                visited[i]=1
    return cnt
n=int(input())
num=int(input())
graph=[[i] for i in range(n+1)]
visited=[0]*(n+1)
for i in range(num):
    num_from, num_to=map(int, sys.stdin.readline().split())
    graph[num_from].append(num_to)
    graph[num_to].append(num_from)
print(BFS())