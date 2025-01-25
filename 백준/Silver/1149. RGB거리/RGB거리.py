n=int(input())

dp=(list(map(int,input().split())))
tmp=[0,0,0]
for i in range(1,n):
	tmp[0],tmp[1],tmp[2]=list(map(int,input().split()))
	tmp[0]+=min(dp[1],dp[2])
	tmp[1]+=min(dp[0],dp[2])
	tmp[2]+=min(dp[1],dp[0])
	dp[0],dp[1],dp[2]=tmp[0],tmp[1],tmp[2]
			
print(min(min(dp[0],dp[1]),dp[2]))	
