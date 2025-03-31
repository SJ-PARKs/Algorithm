from collections import deque

t=int(input())

for i in range(t):
	n,m=map(int,input().split())
	arr=list(map(int,input().split()))
	arr1=sorted(arr,reverse=True)
	q=[]
	for x in range(len(arr)):
		q.append((arr[x],x))
	q=deque(q)
	cnt=0
	while True:
		x=q.popleft()
		if x[0]==arr1[cnt]:
			if x[1]==m:
				cnt+=1
				print(cnt)
				break
			else:
				cnt+=1
		else:
			q.append(x)