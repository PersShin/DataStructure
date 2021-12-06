import sys
from collections import deque
def BFS():
    queue=deque()
    queue.append(start)
    cnt=1
    result=0
    while queue:
        tmp=queue.popleft()
        if tmp==end:
            return visited[tmp]
        for i in (tmp-1,tmp+1,tmp*2):
            if 0<=i<=MAX and not visited[i]:
                visited[i]=visited[tmp]+1 #층의 높이를 알 수 있는 배열
                queue.append(i)
MAX= 10**5
visited=[0]*(MAX+1)
start,end=map(int, sys.stdin.readline().split())
print(BFS())