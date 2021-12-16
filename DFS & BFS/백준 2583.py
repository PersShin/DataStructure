import sys
from collections import deque
def BFS(starter):
    queue=deque()
    queue.append(starter)
    graph[starter[0]][starter[1]]=1
    counter=1
    while queue:
        tmp_x,tmp_y=queue.popleft()
        for i in range(4):
            dxt=dx[i]+tmp_x
            dyt=dy[i]+tmp_y
            if 0<=dxt<len(graph) and 0<=dyt<len(graph[0]):
                if graph[dxt][dyt]==0:
                    graph[dxt][dyt]=1
                    queue.append((dxt,dyt))
                    counter+=1
    return counter
M,N,K=map(int,sys.stdin.readline().split())
graph=[[0 for _ in range(N)] for _ in range(M)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for _ in range(K):
    start_y,start_x,end_y,end_x=map(int, sys.stdin.readline().split())
    for i in range(start_x,end_x):
        for n in range(start_y,end_y):
            graph[i][n]=1
answer=[]
for i in range(M):  
    for n in range(N):
        if graph[i][n]==0:
            answer.append(BFS((i,n)))
print(len(answer))
answer=sorted(answer)
for i in answer:
    print(i, end=' ')
print()