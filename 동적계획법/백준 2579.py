n=int(input())
stairs=[0]
for _ in range(n):
    stairs.append(int(input()))
if n>=3:
    dp=[0 for _ in range(n+2)]
    dp[1]=stairs[1]
    dp[2]=max(stairs[2]+dp[1],stairs[2])
    for i in range(3,n+1):
        dp[i]=max(dp[i-2],dp[i-3]+stairs[i-1])+stairs[i]
    print(dp[n])
elif n==1:
    print(stairs[n])
else:
    print(max(stairs[n],stairs[n-1]+stairs[n]))