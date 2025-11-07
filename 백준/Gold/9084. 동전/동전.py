t=int(input())
for _ in range(t):
	n=int(input())
	coin=list(map(int,input().split()))
	m=int(input())
	dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
	dp[0][0] = 1
	for i in range(1,n+1):
		for j in range(m+1):
			dp[i][j]=dp[i-1][j]
		for j in range(coin[i-1],m+1):
			dp[i][j]=dp[i-1][j]+dp[i][j-coin[i-1]]
	
	print(dp[n][m])
	
	
