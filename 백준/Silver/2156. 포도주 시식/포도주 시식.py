n=int(input())
arr=[]
dp=[0 for _ in range(n)]
for i in range(n):
	arr.append(int(input()))

if n==1:
	print(arr[0])
elif n==2:
	print(arr[0]+arr[1])
else:		
	dp[0]=arr[0]
	dp[1]=arr[0]+arr[1]			    
	dp[2]=max(max(arr[0]+arr[1],arr[1]+arr[2]),arr[0]+arr[2])

	for i in range(3,n):
		dp[i]=max(max(dp[i-3]+arr[i-1]+arr[i],dp[i-1]),dp[i-2]+arr[i])
	
	print(dp[n-1])