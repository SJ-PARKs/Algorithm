from collections import deque
import copy

n,m,k=map(int,input().split())
grid=[[deque() for _ in range(n)] for _ in range(n)]
fireball=[]
dr,dc=[-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]

for _ in range(m):
	r,c,m,s,d=map(int,input().split())
	grid[r-1][c-1].append([m,s,d])

for _ in range(k):
	new_grid=[[deque() for _ in range(n)] for _ in range(n)]
	for r in range(n):
		for c in range(n):
			if len(grid[r][c])>0:
				for i in range(len(grid[r][c])):
					fireball=grid[r][c][i]
					nr,nc=(r+fireball[1]*dr[fireball[2]])%n,(c+fireball[1]*dc[fireball[2]])%n
					new_grid[nr][nc].append(fireball)

	for r in range(n):
		for c in range(n):
			if len(new_grid[r][c])>=2:
				arr=new_grid[r][c]
				weight,speed,odd,even=0,0,0,0
				for i in range(len(arr)):
					weight+=arr[i][0]
					speed+=arr[i][1]
					if arr[i][2]%2==0:
						even+=1
					else:
						odd+=1
				new_arr=[]
				if weight//5>0:
					if even==len(arr) or odd==len(arr):
						for i in range(4):				
							new_arr.append([weight//5,speed//len(arr),2*i])
					else:
						for i in range(4):
							new_arr.append([weight//5,speed//len(arr),2*i+1])
				new_grid[r][c]=deque(new_arr)
				
	grid=new_grid	

	
answer=0
for i in range(n):
	for j in range(n):
		for k in range(len(grid[i][j])):
			answer+=grid[i][j][k][0]
	

print(answer)