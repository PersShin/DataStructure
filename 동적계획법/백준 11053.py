import sys
n=int(input())
num=list(map(int,sys.stdin.readline().split()))
dp=[1 for _ in range(n)]
for i in range(1,n):
    for t in range(i):
        if num[i]>num[t]:
            dp[i]=max(dp[i],dp[t]+1)
print(max(dp))