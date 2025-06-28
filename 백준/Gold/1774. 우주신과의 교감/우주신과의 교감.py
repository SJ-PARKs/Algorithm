import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

n,m=map(int,input().split())

arr=[]
for i in range(n):
	x,y=map(int,input().split())
	arr.append((x,y))
	
distance=[]

for i in range(n-1):
	for j in range(i+1,n):
		distance.append((i,j,calculate_distance(arr[i][0],arr[i][1],arr[j][0],arr[j][1])))
		
distance = sorted(distance, key=lambda x: x[2])

tree=[i for i in range(n)]

def find(num):
	if tree[num]==num:
		return num
	else:
		tree[num]=find(tree[num])
		return tree[num]

def union(num1,num2):
	x1=find(num1)
	x2=find(num2)
	if x1!=x2:
		tree[x1]=x2
		
for i in range(m):
	x,y=map(int,input().split())
	union(x-1,y-1)
	
answer=0
for i in range(len(distance)):
	x1=find(distance[i][0])
	x2=find(distance[i][1])
	if x1!=x2:
		union(x1,x2)
		answer+=distance[i][2]
		
print(f"{answer:.2f}")
	