global zero, one

dp=[[] for _ in range(41)]
dp[0]=[1,0]
dp[1]=[0,1]

for i in range(2,41):
	a,b=dp[i-1]
	c,d=dp[i-2]
	dp[i]=[a+c,b+d]

t=int(input())

for i in range(t):
	n=int(input())
	print(dp[n][0],dp[n][1])


		