from collections import deque
def solution(n, computers):
    answer = 0
    visited=[False for i in range(n)]
    for i in range(n):
        if(visited[i]==False):
            BFS(n,computers,i,visited) 
            answer+=1
    return answer
def BFS(n,computers,i,visited):
    queue=deque()
    queue.append(i)
    while len(queue)!=0:
        i=queue.popleft()
        visited[i]=True
        for connect in range(n):
            if(connect!=i) and (computers[i][connect]==1):
                if(visited[connect]==False):
                    queue.append(connect)
n=3
computers=[[1,1,0],[1,1,0],[0,0,1]]
print(solution(n,computers))