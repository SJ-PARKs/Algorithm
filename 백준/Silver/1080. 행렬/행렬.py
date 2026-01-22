n,m=map(int,input().split())

arr1=[]
arr2=[]
for i in range(n):
	arr1.append(list(map(int,input())))
for i in range(n):
	arr2.append(list(map(int,input())))
	
def turn(x,y):
	for i in range(3):
		for j in range(3):
			if arr1[x+i][y+j]==0:
				arr1[x+i][y+j]=1
			else:
				arr1[x+i][y+j]=0
count=0
for i in range(n-2):
	for j in range(m-2):
		if arr1[i][j]!=arr2[i][j]:
			turn(i,j)
			count+=1
if arr1!=arr2:
	print(-1)
else:
	print(count)