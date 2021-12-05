import sys
from collections import deque
def finder(starter):
    queue=deque()
    queue.append(starter)
    visited[starter]=1
    while queue:
        tmp=queue.popleft()
        for n in graph[tmp]:
            if visited[n]==0:
                queue.append(n)
                visited[n]=1
        
cnt=0
num_x,num_y=map(int,sys.stdin.readline().split())
graph=[[] for i in range(num_x)]
visited=[0]*num_x
for i in range(num_y):
    temp_x,temp_y=map(int,sys.stdin.readline().split())
    graph[temp_x-1].append(temp_y-1)
    graph[temp_y-1].append(temp_x-1)
for starter in range(len(visited)):
    if visited[starter]==0:
        finder(starter)
        cnt+=1
print(cnt)