import copy

n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]

dr,dc=[0,-1,-1,-1,0,1,1,1],[-1,-1,0,1,1,1,0,-1]

def range_in(r,c):
	if 0<=r<n and 0<=c<n:
		return True
	else:
		return False
cloud=[[n-1,0],[n-1,1],[n-2,0],[n-2,1]]
	
for _ in range(m):
	visited = [[False] * n for _ in range(n)]
	d,s=map(int,input().split())
	for i in range(len(cloud)):
		cloud[i][0]=(cloud[i][0]+dr[d-1]*s)%n
		cloud[i][1]=(cloud[i][1]+dc[d-1]*s)%n
		visited[cloud[i][0]][cloud[i][1]] = True
		a[cloud[i][0]][cloud[i][1]]+=1
	
	for i in range(len(cloud)):
		count=0
		for dx,dy in [(1,1),(1,-1),(-1,1),(-1,-1)]:
			if range_in(cloud[i][0]+dx,cloud[i][1]+dy):
				if a[cloud[i][0]+dx][cloud[i][1]+dy]>0:
					count+=1
		a[cloud[i][0]][cloud[i][1]]+=count
	
	new_cloud=[]
	for i in range(n):
		for j in range(n):
			if a[i][j]>=2 and not visited[i][j]:
				new_cloud.append([i,j])
				a[i][j]-=2
	cloud=new_cloud

answer=0
for i in range(n):
	for j in range(n):
		answer+=a[i][j]
print(answer)
		
	