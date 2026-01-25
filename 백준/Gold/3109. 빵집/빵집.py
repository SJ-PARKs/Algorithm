import copy
r,c=map(int,input().split())
board=[]
for i in range(r):
	board.append(list(input()))

dx=[-1,0,1]
def DFS(x,y):
	global c
	if y==c-1:
		return True
	for i in range(3):
		nx=x+dx[i]
		ny=y+1
		if 0<=nx<r and 0<=ny<c:
			if board[nx][ny]==".":
				board[nx][ny]='x'
				if DFS(nx, ny):
					return True
	
	return False

answer=0
								
for i in range(r):
	flag=DFS(i,0)
	if flag==True:
		answer+=1
print(answer)