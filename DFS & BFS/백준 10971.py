import sys
def dfs_backtracking(start,end,value,visited):
    global min_value
    if len(visited)==num:
        if maze[end][start]!=0:
            min_value=min(min_value,value+maze[end][start])
        return
    for i in range(num):
        if maze[end][i]!=0 and i not in visited and value<min_value:
            visited.append(i)
            dfs_backtracking(start,i,value+maze[end][i],visited)
            visited.pop()
num=int(input())
maze=[]
min_value=sys.maxsize
for i in range(num):
    maze.append(list(map(int,sys.stdin.readline().split())))
for i in range(num):
    dfs_backtracking(i,i,0,[i])
print(min_value)