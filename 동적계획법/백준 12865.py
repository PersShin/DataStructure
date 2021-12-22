import sys
N,K=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp=[[0]*(K+1) for _ in range(N+1)]
for i in range(1,N+1):
    for t in range(1,K+1):
        weight,value=map(int,graph[i-1])
        if weight<=t:
            dp[i][t]=max(dp[i-1][t],dp[i-1][t-weight]+value)
        else:
            dp[i][t]=dp[i-1][t]
print(dp[N][K])