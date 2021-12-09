import sys
from collections import deque
sys.setrecursionlimit(10**8)
dx=[1,-1,0,0]
dy=[0,0,1,-1]
dx_horse=[-1, -2, -2, -1, 1, 2, 2, 1]
dy_horse=[-2, -1, 1, 2, 2, 1, -1, -2]
def BFS():
    queue=deque()
    queue.append((0,0,0,num))
    while queue:
        tmp_x,tmp_y,cost,k_num=queue.popleft()
        if k_num>0:
            for i in range(8):
                x,y=tmp_x+dx_horse[i], tmp_y+dy_horse[i]
                if 0<=x<num_y and 0<=y<num_x and maze[x][y]==0:
                    if visited[x][y]==-1 or visited[x][y]<k_num-1:
                        if x==num_y-1 and y== num_x-1:
                            return cost+1
                        visited[x][y]=k_num-1
                        queue.append((x,y,cost+1,k_num-1))
        for i in range(4):
            x,y=tmp_x+dx[i],tmp_y+dy[i]
            if 0<=x<num_y and 0<=y<num_x and maze[x][y]==0:
                if visited[x][y]==-1 or visited[x][y]<k_num:
                    if x==num_y-1 and y== num_x-1:
                        return cost+1
                    visited[x][y]=k_num
                    queue.append((x,y,cost+1,k_num))
    return -1
num=int(sys.stdin.readline())
num_x,num_y=map(int,sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(num_y)]
visited=[[-1]*num_x for _ in range(num_y)]
if num_x==1 and num_y==1:
    print(0)
else:
    print(BFS())