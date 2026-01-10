n,k=map(int,input().split())

dp=[[0]*(n+1) for _ in range(k+1)]

for i in range(n+1):
	dp[1][i]=1
	
if k>=2:
	for i in range(2,k+1):
		hap=0
		for j in range(n+1):
			hap+=dp[i-1][j]
			dp[i][j]=(hap%1000000000)
print(dp[k][n])