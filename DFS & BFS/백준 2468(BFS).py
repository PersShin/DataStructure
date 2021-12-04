import sys
from collections import deque
def BFS(limit,start_x,start_y):
    queue=deque()
    queue.append((start_x,start_y))
    visited[start_x][start_y]=1
    while queue:
        temp_x,temp_y=queue.popleft()
        for i in range(4):
            x=temp_x+dx[i]
            y=temp_y+dy[i]
            if(x<0) or (y<0) or (x>=len(maze)) or (y>=len(maze[0])):
                continue
            elif maze[x][y]>limit and not visited[x][y]:
                queue.append((x,y))
                visited[x][y]=1
num=int(input())
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(num)]
answers=[]
num_max = max(map(max, maze))
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for i in range(num_max):#limit range
    visited = [[0 for _ in range(num)] for _ in range(num)]
    answer_temp=[]
    for q in range(num):
        for p in range(num):
            if maze[q][p]>i and not visited[q][p]:
                BFS(i,q,p)
                answer_temp.append(1)
    answers.append(len(answer_temp))
print(max(answers))