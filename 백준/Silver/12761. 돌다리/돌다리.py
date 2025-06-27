from collections import deque

a,b,n,m=map(int,input().split())

chk=[0 for _ in range(100001)]

q=deque()
q.append((n,0))
chk[n]=1

while len(q)!=0:
	x,count=q.popleft()
	if x==m:
		print(count)
		break
	nx=[]
	nx.append(x-1)
	nx.append(x+1)
	nx.append(x+a)
	nx.append(x-a)
	nx.append(x*a)
	nx.append(x+b)
	nx.append(x-b)
	nx.append(x*b)
	for i in range(len(nx)):
		if 0<=nx[i]<=100000 and chk[nx[i]]==0:
			chk[nx[i]]=1
			q.append((nx[i],count+1))
			

	