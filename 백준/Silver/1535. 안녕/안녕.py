import copy

n=int(input())

lost=list(map(int,input().split()))
joy=list(map(int,input().split()))

health=100

dp=[[0]*100 for _ in range(n+1)]

for i in range(1,n+1):
    dp[i]=copy.deepcopy(dp[i-1])
    for j in range(lost[i-1],100):
        dp[i][j]=max(dp[i-1][j-lost[i-1]]+joy[i-1],dp[i][j])

print(max(dp[n]))