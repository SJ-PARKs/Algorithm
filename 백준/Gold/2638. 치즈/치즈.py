from collections import deque
import copy

def disappear(board):
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j]>0:
				return False
	return True

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def make_in_out(board):
	n,m=len(board),len(board[0])
	in_out=[[0 for _ in range(m)] for _ in range(n)]
	chk=[[0 for _ in range(m)] for _ in range(n)]
	
	q=deque()
	q.append((0,0))
	q.append((n-1,0))
	q.append((0,m-1))
	q.append((n-1,m-1))
	
	while q:
		x,y=q.popleft()
		for i in range(4):
			nx=x+dx[i]
			ny=y+dy[i]
			if 0<=nx<n and 0<=ny<m:
				if board[nx][ny]==0 and chk[nx][ny]==0:
					in_out[nx][ny]=1
					chk[nx][ny]=1
					q.append((nx,ny))
	return in_out

def melt(board,in_out):
	n,m=len(board),len(board[0])
	new_board=[[0 for _ in range(m)] for _ in range(n)]
	
	for i in range(n):
		for j in range(m):
			if board[i][j]==0:
				continue
			count=0
			for k in range(4):
				nx=i+dx[k]
				ny=j+dy[k]
				if 0<=nx<n and 0<=ny<m:
					if in_out[nx][ny]==1:
						count+=1
			if count>=2:
				new_board[i][j]=0
			else:
				new_board[i][j]=1
	return new_board

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]

answer=0
while True:
	if disappear(board):
		print(answer)
		break
	
	in_out=make_in_out(board)
	new_board=melt(board,in_out)
	board=copy.deepcopy(new_board)
	
	answer+=1

