from collections import deque
import sys

def BFS():
    queue=deque()
    queue.append((0,0,0))
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited[0][0] = 2
    cnt=0
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x, y, break_wall = queue.popleft()
            if x == n-1 and y == m-1:
                return cnt
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx >= n or nx < 0 or ny >= m or ny < 0:
                    continue
                if not break_wall:
                    if not graph[nx][ny]:
                        if visited[nx][ny] in [0, -1]:
                            visited[nx][ny] = 2
                            queue.append((nx, ny, break_wall))
                    else:
                        queue.append((nx, ny, break_wall + 1))
                else:
                    if not graph[nx][ny] and not v[nx][ny]:
                        visited[nx][ny] = -1
                        queue.append((nx, ny, break_wall))
    return -1

n,m=map(int, sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
visited=[[0 for _ in range(m)] for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
print(BFS())