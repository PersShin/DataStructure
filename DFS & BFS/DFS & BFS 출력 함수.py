from collections import deque
def DFS(n,graph,q):
    visited_DFS[q]=1
    print(q+1, end=' ')
    for i in range(0,n):
        if(visited_DFS[i]==0) and (graph[q][i]==1):
            DFS(n,graph,i)
def BFS(n,graph,q):
    queue=deque()
    queue.append(q)
    visited_BFS[q]=1
    while queue:
        tmp=queue.popleft()
        print(tmp+1, end=' ')
        for i in range(0,n):
            if(visited_BFS[i]==0) and (graph[tmp][i]==1):
                queue.append(i)
                visited_BFS[i]=1
n=4
q=0
graph=[[0]*(n+1) for _ in range(n+1)]
visited_DFS=[0]*n
visited_BFS=[0]*n
computers=[[1,2],[1,3],[1,4],[2,4],[3,4]]
for i in computers:
    graph[i[0]-1][i[1]-1]=graph[i[1]-1][i[0]-1]=1
print(graph)
DFS(n,graph,q)
print()
BFS(n,graph,q)