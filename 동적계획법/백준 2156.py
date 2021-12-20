n=int(input())
graph=[0]
for i in range(n):
    graph.append(int(input()))
if n>=3:
    dp=[0 for _ in range(n+1)]
    dp[1]=graph[1]
    dp[2]=max(dp[1]+graph[2],graph[2])
    for i in range(3,n+1):
        dp[i]=max(dp[i-2],max(dp[:i-2])+graph[i-1])+graph[i]
    print(max(dp))
if n<=2:
    print(sum(graph))