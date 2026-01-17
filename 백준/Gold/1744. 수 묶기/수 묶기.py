n=int(input())
arr=[]
for i in range(n):
	arr.append(int(input()))
	
arr.sort()
dp=[0]*n

dp[0]=arr[0]
if n>1:
	dp[1]=max(dp[0]+arr[1],arr[0]*arr[1])
	for i in range(2,n):
		dp[i]=max(dp[i-2]+arr[i-1]*arr[i],dp[i-1]+arr[i])

print(dp[n-1])