import copy

n,m=map(int,input().split())

memory=list(map(int,input().split()))
cost=list(map(int,input().split()))

dp=[[0]*10001 for _ in range(n+1)]

for i in range(1,n+1):
    dp[i]=copy.deepcopy(dp[i-1])
    for j in range(cost[i-1],10001):
        dp[i][j]=max(dp[i-1][j-cost[i-1]]+memory[i-1],dp[i][j])

for i in range(0,10001):
    if dp[n][i]>=m:
        print(i)
        break
