import copy 

n,m,r=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]

for _ in range(r):
	for i in range(min(n,m)//2):
		temp=a[i][i]
		for j in range(i+1,m-i):
			a[i][j-1]=a[i][j]
		for j in range(i+1,n-i):
			a[j-1][m-1-i]=a[j][m-1-i]
		for j in range(m-i-2,i-1,-1):
			a[n-1-i][j+1]=a[n-1-i][j]
		for j in range(n-i-2,i,-1):
			a[j+1][i]=a[j][i]
		a[i+1][i]=temp
			  
for i in range(n):
	for j in range(m):
		print(a[i][j],end=' ')
	print()