C,n=map(int,input().split())
dp=[float("inf")]*1001
dp[0]=0

for i in range(n):
    c,v=map(int,input().split())
    for j in range(1,v+1):
        dp[j]=min(dp[j],c)
    for j in range(v,1001):
        dp[j]=min(dp[j-v]+c,dp[j])

print(dp[C])