import sys
from collections import deque

def align(num):
    queue=deque()
    DP=[0 for _ in range(N+1)]

    for i in range(1,len(visited)):
        if visited[i]==0:
            queue.append(i)
            DP[i]=weight[i]

    while queue:
        tmp=queue.popleft()

        for i in graph[tmp]:
            visited[i]-=1
            #들어오는 간선에서 최대값만 저장을 한다.
            DP[i]=max(DP[tmp]+weight[i],DP[i])

            if visited[i]==0:
                queue.append(i)

    return DP[num] 
          
for _ in range(int(input())):
    N,k=map(int,sys.stdin.readline().split())
    graph=[[] for _ in range(N+1)]
    weight=[0]
    visited=[0]*(N+1)
    weight.extend(list(map(int,sys.stdin.readline().split())))
    for _ in range(k):
        x,y=map(int,sys.stdin.readline().split())
        graph[x].append(y)
        visited[y]+=1
    print(align(int(input())))