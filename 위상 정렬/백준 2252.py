import sys
from collections import deque
def alignment():
    result=[]
    queue=deque()

    #그래프의 시작점을 찾는 코드
    for i in range(1,N+1):
        if visited[i]==0:
            queue.append(i)

    while queue:
        tmp=queue.popleft()
        result.append(tmp)
        for i in graph[tmp]:
            visited[i]-=1
            #위에 연결되는 노드가 더 이상 없을 떄 queue에 저장
            if visited[i]==0:
                queue.append(i)

    return ' '.join(map(str,result))
    
N,M=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
visited=[0 for _ in range(N+1)]
for _ in range(M):
    tmp_x,tmp_y=map(int,sys.stdin.readline().split())
    graph[tmp_x].append(tmp_y)
    #위에 연결되는 노드가 있으므로 visited 배열에 추가 한다.
    visited[tmp_y]+=1
print(alignment())