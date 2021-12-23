import sys
from collections import deque
def BFS(x,y):
    queue=deque()
    queue.append((x,y))
    color=graph[x][y]
    cnt=1
    visited=[(x,y)]
    while queue:
        tmp_x,tmp_y=queue.popleft()
        for i in range(4):
            dxt=dx[i]+tmp_x
            dyt=dy[i]+tmp_y
            if 0<=dxt<6 and 0<=dyt<12:
                if graph[dxt][dyt]==color and (dxt,dyt) not in visited:
                    queue.append((dxt,dyt))
                    visited.append((dxt,dyt))
                    cnt+=1
    #같은 색의 블록의 개수가 4개 이상일 경우
    if cnt>=4:
        for i in visited:
            graph[i[0]][i[1]]='.'
        return 1
    else: return 0

def makemap(graphs):
    for i in range(6):
        cnt=0
        place=[]
        for n in range(12):
            if graphs[i][n]!='.':
                #list에 color를 저장한다.
                place.append(graphs[i][n])
            else:
                cnt+=1
        if cnt!=0:
            graphs[i]=['.' for _ in range(cnt)]+place
    return graphs 
graph=[list(sys.stdin.readline().rstrip()) for _ in range(12)]
#그래프를 transpose한다. 그래야 중력으로 떨어지는 값들에 대한 접근이 쉬워지기 떄문이다.
graph=list(map(list,zip(*graph)))
dx=[1,-1,0,0]
dy=[0,0,1,-1]
answer=0
while True:
    tmp=0
    #한 라운드에서 같이 터질경우 하나의 연쇄가 된다.
    #즉, 1라운드에서 2개가 같이 터져도 1연쇄 1개가 터져도 1연쇄이다.
    for i in range(6):
        for n in range(11,0,-1):
            if graph[i][n]!='.':
                tmp+=BFS(i,n)
    #tmp==0이라면 연쇄가 끝난 것이므로 무한루프를 탈출한다.
    if not tmp:
        break
    #아닐 경우 연쇄를 1 늘려주고 중력으로 인해 밑으로 내려가는 블록을 갱신한다.
    else:
        answer+=1
        graph=makemap(graph)
print(answer)