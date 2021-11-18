from collections import deque
def BFS(map):
    queue=deque()
    queue.append((0,0))
    #방향 설정
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    while queue:
        tmp_x,tmp_y=queue.popleft()
        for i in range(0,4):
            nx=tmp_x+dx[i]
            ny=tmp_y+dy[i]
            if(nx<0) or (ny<0) or (nx>=len(map)) or (ny>=len(map[0])):
                continue
            elif(map[nx][ny]==0):
                continue
            elif(map[nx][ny]==1):
                map[nx][ny]=map[tmp_x][tmp_y]+1
                queue.append((nx,ny))
    return map[len(map)-1][len(map[0])-1]
map=[[1,0,1,1,1,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,1,1,0,1,1]]
print(len(map), len(map[0]))
print(BFS(map))