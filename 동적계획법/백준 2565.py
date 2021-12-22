import sys
n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
graph=sorted(graph)
dp=[1 for _ in range(n)]
for i in range(1,n):
    for t in range(i):
        if graph[i][1]>graph[t][1]:
            dp[i]=max(dp[i],dp[t]+1)
print(n-max(dp))