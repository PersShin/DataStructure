import sys
string_1 = ' ' + sys.stdin.readline().rstrip()
string_2 = ' ' + sys.stdin.readline().rstrip()
dp=[[0 for _ in range(len(string_2))] for _ in range(len(string_1))]
for i in range(1,len(string_1)):
    for t in range(1,len(string_2)):
        if string_1[i]==string_2[t]:
            dp[i][t]=dp[i-1][t-1]+1
        else:
            dp[i][t]=max(dp[i-1][t],dp[i][t-1])
print(dp[-1][-1])