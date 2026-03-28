n=int(input())
matrix=[
	list(map(int,input().split()))
	for _ in range(n)
]

INF=1e9

dp=[[INF]*n for _ in range(n)]

for i in range(n):
	dp[i][i]=0
	
for size in range(1,n):
	for i in range(n-size):
		j=i+size
		for k in range(i,j):
			dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+(matrix[i][0]*matrix[k][1]*matrix[j][1]))

print(dp[0][n-1])