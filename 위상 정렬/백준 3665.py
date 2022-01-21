import sys
from collections import deque
def align():
    answer=[]
    len_answer=0
    queue=deque()
    for i in range(1,len(visists)):
        if visists[i]==0:
            queue.append(i)

    while queue:
        #1개의 팀이 아니라 여러 팀이 들어오면 상대적인 순위가 없는 경우이므로 impossible이다.
        if len(queue)>1:
            len_answer=1
        tmp=queue.popleft()
        answer.append(tmp)

        for i in graph[tmp]:
            visists[i]-=1
            if visists[i]==0:
                queue.append(i)
    #모든 팀을 못 담은 경우, 순위가 애매한 경우이다.
    if len(answer)!=player or len_answer!=0:
        return 'IMPOSSIBLE'
    return ' '.join(map(str,answer))
N=int(input())
for _ in range(N):
    player=int(input())
    graph=[[] for _ in range(player+1)]
    visists=[0]*(player+1)
    rank=list(map(int,sys.stdin.readline().split()))

    #상대적인 순위를 표시하는 코드이다.
    for i in range(player-1):
        for n in range(i+1,player):
            graph[rank[i]].append(rank[n])

    #올해 순위로 인해 변동되는 것을 반영한 코드이다.
    for i in range(int(input())):
        x,y=map(int,sys.stdin.readline().split())
        if x in graph[y]:
            graph[y].remove(x)
            graph[x].append(y)
        else:
            graph[x].remove(y)
            graph[y].append(x)

    #그것에 따른 연결 순위를 나타낸 코드이다.
    for i in range(1,player+1):
        visists[i]=player-1-len(graph[i])
        
    print(align())  