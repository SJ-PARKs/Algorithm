n=int(input())
arr=[]
dp=[]

for i in range(n):
	arr.append(list(map(int,input().split())))
	dp.append([0 for _ in range(i+1)])

dp[0][0]=arr[0][0]
	
for i in range(1,n):
	dp[i][0]=dp[i-1][0]+arr[i][0]
	dp[i][i]=dp[i-1][i-1]+arr[i][i]

for i in range(2,n):
	for j in range(1,i):
		dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+arr[i][j]

answer=0
for i in range(n):
	answer=max(answer,dp[n-1][i])
	
print(answer)
