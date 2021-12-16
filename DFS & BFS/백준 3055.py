import sys
from collections import deque
def BFS():
    global waterfall
    queue=deque()
    queue.append((starter[0],starter[1],0))
    counts=-1
    while queue:
        tmp_x,tmp_y,counter=queue.popleft()
        if counter>counts:
            counts=counter
            tmp=[]
            for i in range(4):
                for n in waterfall:
                    dtx=n[0]+dx[i]
                    dty=n[1]+dy[i]
                    if 0<=dtx<len(graph) and 0<=dty<len(graph[0]) and graph[dtx][dty]!='D' and graph[dtx][dty]!='X':
                        graph[dtx][dty]='X'
                        tmp.append((dtx,dty))
            waterfall=tmp
        for i in range(4):
            dtx=tmp_x+dx[i]
            dty=tmp_y+dy[i]
            if 0<=dtx<len(graph) and 0<=dty<len(graph[0]):
                if graph[dtx][dty]!='X' and graph[dtx][dty]=='.':
                    queue.append((dtx,dty,counter+1))
                    graph[dtx][dty]=1
                if graph[dtx][dty]=='D':
                    return counter+1
    return 'KAKTUS'
num_y,num_x=map(int,sys.stdin.readline().split())
graph = [list(input().strip()) for _ in range(num_y)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
waterfall=[]
for i in range(num_y):
    if '*' in graph[i]:
        waterfall.append((i,graph[i].index('*')))
        graph[i][graph[i].index('*')]='X'
    if 'S' in graph[i]:
        starter=(i,graph[i].index('S'))
print(BFS())