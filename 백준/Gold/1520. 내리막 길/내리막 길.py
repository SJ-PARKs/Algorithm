import sys
sys.setrecursionlimit(10**6) 

n,m = map(int, sys.stdin.readline().split())
board=[]
for i in range(n):
	board.append(list(map(int,input().split())))
dp=[[-1 for _ in range(m)] for _ in range(n)]
directions=[(1,0),(0,1),(0,-1),(-1,0)]	
dp[0][0]=1	
h=0	
def DFS(x,y):
	global h
	if x==0 and y==0:
		return 1
	if dp[x][y]!=-1:
		return dp[x][y]
	else:
		dp[x][y]=0
		for dx,dy in directions: 
			nx=x+dx
			ny=y+dy
			if 0<=nx<n and 0<=ny<m:
				if board[x][y]<board[nx][ny]:
					dp[x][y]+=DFS(nx,ny)
					
		return dp[x][y]
	
print(DFS(n-1,m-1))
