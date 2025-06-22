n,k=map(int,input().split())
s=list(map(int,input().split()))
d=list(map(int,input().split()))


for i in range(k):
	arr=[0 for _ in range(n)]
	for j in range(n):
		arr[d[j]-1]=s[j]
	s=arr

for i in range(n):
	print(s[i],end=' ')