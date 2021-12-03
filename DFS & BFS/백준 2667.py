from collections import deque
def BFS(start_x,start_y):
    queue=deque()
    queue.append((start_x,start_y))
    visited[start_x][start_y]=1
    answer_temp=1
    while queue:
        tmp_x,tmp_y=queue.popleft()
        for i in range(4):
            x=tmp_x+dx[i]
            y=tmp_y+dy[i]
            if(x<0) or (y<0) or (x>=len(maze)) or (y>=len(maze[0])):
                continue
            elif maze[x][y]==1 and not visited[x][y]:
                maze[x][y]+=maze[tmp_x][tmp_y]
                queue.append((x,y))
                answer_temp+=1
                visited[x][y]=1
    return answer_temp
n=int(input())
maze = [list(map(int, input())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
answer=[]
for i in range(n):
    for q in range(n):
        if maze[i][q]==1 and not visited[i][q]:
            answer.append(BFS(i,q))
print(len(answer))
for i in sorted(answer):
    print(i)