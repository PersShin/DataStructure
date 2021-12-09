import sys
from collections import deque
def BFS(x,y):
    queue=deque()
    queue.append((x,'',0))
    visited[x]=1
    while queue:
        tmp,order,count=queue.popleft()
        if tmp==0:
            if visited[9999]==-1 or count<visited[9999]-1:
                if y==9999:
                    return order+'S'
                visited[9999]=count+1
                queue.append((9999,order+'S',count+1))

        else:
            if visited[tmp-1]==-1 or count<visited[tmp-1]-1:
                if y==tmp-1:
                    return order+'S'
                visited[tmp-1]=count+1
                queue.append((tmp-1,order+'S',count+1))

        if visited[tmp*2%10000]==-1 or count<visited[tmp*2%10000]-1:
            if tmp*2%10000==y:
                return order+'D'
            visited[tmp*2%10000]=count+1
            queue.append((tmp*2%10000,order+'D',count+1))

        new_tmp=(tmp%1000)*10+tmp//1000
        if visited[new_tmp]==-1 or count<visited[new_tmp]-1:
            if new_tmp==y:
                return order+'L'
            visited[new_tmp]=count+1
            queue.append((new_tmp,order+'L',count+1))

        new_tmp=(tmp%10)*1000+tmp//10
        print(new_tmp)
        if visited[new_tmp]==-1 or count<visited[new_tmp]-1:
            if new_tmp==y:
                return order+'L'
            visited[new_tmp]=count+1
            queue.append((new_tmp,order+'R',count+1))

n=int(input())
visited=[-1]*10000
for i in range(n):
    num_x,num_y=list(map(int,sys.stdin.readline().split()))
    print(BFS(num_x,num_y))