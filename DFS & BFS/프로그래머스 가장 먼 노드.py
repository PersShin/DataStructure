from collections import deque
def solution(n, edge):
    graph=[[] for _ in range(n+1)]
    visited=[0 for _ in range(n+1)]
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    queue=deque()
    queue.append((1,0))
    visited[1]=1
    while queue:
        tmp,cnt=queue.popleft()
        for i in graph[tmp]:
            if visited[i]==0 or visited[i]>cnt+1:
                queue.append((i,cnt+1))
                visited[i]=cnt+1
    return visited.count(max(visited))