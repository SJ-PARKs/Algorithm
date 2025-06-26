n=int(input())
piano=list(map(int,input().split()))

dp=[0 for _ in range(n)]

for i in range(1,n):
	if piano[i-1]>piano[i]:
		dp[i]=dp[i-1]+1
	else:
		dp[i]=dp[i-1]
		
q=int(input())
for _ in range(q):
	x,y=map(int,input().split())
	print(dp[y-1]-dp[x-1])
