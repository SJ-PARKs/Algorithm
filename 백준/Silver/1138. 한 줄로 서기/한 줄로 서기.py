from collections import deque

n=int(input())
arr=list(map(int,input().split()))
q=deque()
q.append(n)
for i in range(n-2,-1,-1):
	if arr[i]==0:
		q.appendleft(i+1)
	else:
		idx=arr[i]
		new_q=[]
		for j in range(idx):
			new_q.append(q[j])
		new_q.append(i+1)
		for j in range(idx,len(q)):
			new_q.append(q[j])
		q=deque(new_q)
	
		
for i in range(len(q)):
	print(q[i],end=" ")