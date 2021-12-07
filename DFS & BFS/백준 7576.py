import sys
from collections import deque
def BFS():
    queue=deque()
    for i in sum_1:
        queue.append(i)
    while queue:
        tmp_x,tmp_y=queue.popleft()
        for i in range(4):
            dxs=tmp_x+dx[i]
            dys=tmp_y+dy[i]
            if (dxs>=0) and (dys>=0) and (dxs<len(maze)) and (dys<len(maze[0])):
                if maze[dxs][dys]==0:
                    maze[dxs][dys]+=maze[tmp_x][tmp_y]+1
                    queue.append((dxs,dys))
    max_count=0
    for i in range(len(maze)):
        if maze[i].count(0)>0:
            return -1
        max_count=max(max_count,max(maze[i]))
    return max_count-1

    
x_input, y_input=map(int,sys.stdin.readline().split())
maze=[]
#maze에 미로의 모양을 집어넣는 과정
sum_1=[]
for i in range(y_input):
    maze.append(list(map(int, sys.stdin.readline().split())))
#위, 아래, 오른쪽, 왼쪽
dx=[1,-1,0,0]
dy=[0,0,-1,1]
for i in range(len(maze)):
    if maze[i].count(1)==1:
        sum_1.append((i,maze[i].index(1)))
    elif maze[i].count(1)>1:
        for n in range(len(maze[i])):
            if maze[i][n]==1:
                sum_1.append((i,n))
print(BFS())