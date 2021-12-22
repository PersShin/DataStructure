import sys
n=int(input())
num=[0]
num.extend(list(map(int,sys.stdin.readline().split())))
graph=[0 for _ in range(n+1)]
graph[1]=num[1]
#1은 이미 저장되어 있으므로 index 2부터 탐색을 한다.
for i in range(2,n+1):
    graph[i]=max(num[i],graph[i-1]+num[i])
print(max(graph[1:]))