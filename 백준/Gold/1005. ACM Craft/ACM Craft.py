from collections import deque
import copy

t=int(input())

for _ in range(t):
	n,k=map(int,input().split())
	arr=list(map(int,input().split()))
	arr=[0]+arr
	dp=[0]*(n+1)
	cost=copy.deepcopy(arr)
	board_from=[[] for _ in range(n+1)]
	board_to=[[] for _ in range(n+1)]
	for i in range(k):
		x,y=map(int,input().split())
		dp[y]+=1
		board_to[x].append(y)
		board_from[y].append(x)
	start=0
	q=deque()
	for i in range(1,n+1):
		if dp[i]==0:
			q.append(i)
	
	while q:
		cur=q.popleft()
		for b_to in board_to[cur]:
			dp[b_to]-=1
			if dp[b_to]==0:
				temp=0
				for b_from in board_from[b_to]:
					temp=max(temp,cost[b_from])
				cost[b_to]=temp+arr[b_to]
				q.append(b_to)
	
	w=int(input())
	print(cost[w])
	