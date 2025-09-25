import copy
n=int(input())

board=[list(map(int,input().split())) for _ in range(n)]

answer=-1
def maximum_num(board):
	maximum=-1
	for i in range(n):
		for j in range(n):
			if board[i][j]>maximum:
				maximum=board[i][j]
			
	return maximum

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def move(board,direction,n):
	new_board=copy.deepcopy(board)
	if direction==0:
		for i in range(n):
			chk=[[0]*n for _ in range(n)]
			for j in range(1,n):
				if new_board[i][j]>0:
					k=j
					while k>=1 and new_board[i][k-1]==0:
						new_board[i][k-1]=new_board[i][k]
						new_board[i][k]=0
						k-=1
					if k>=1 and new_board[i][k-1]==new_board[i][k] and chk[i][k-1]==0:
						new_board[i][k-1]=2*new_board[i][k-1]
						new_board[i][k]=0
						chk[i][k-1]=1
				
	if direction==1:
		for i in range(n):
			chk=[[0]*n for _ in range(n)]
			for j in range(n-2,-1,-1):
				if new_board[i][j]>0:
					k=j
					while k<=n-2 and new_board[i][k+1]==0:
						new_board[i][k+1]=new_board[i][k]
						new_board[i][k]=0
						k+=1
					if k<=n-2 and new_board[i][k+1]==new_board[i][k] and chk[i][k+1]==0:
						new_board[i][k+1]=2*new_board[i][k+1]
						new_board[i][k]=0
						chk[i][k+1]=1
				
	if direction==2:
		for j in range(n):
			chk=[[0]*n for _ in range(n)]
			for i in range(1,n):
				if new_board[i][j]>0:
					k=i
					while k>=1 and new_board[k-1][j]==0:
						new_board[k-1][j]=new_board[k][j]
						new_board[k][j]=0
						k-=1
					if k>=1 and new_board[k-1][j]==new_board[k][j] and chk[k-1][j]==0:
						new_board[k-1][j]=2*new_board[k-1][j]
						new_board[k][j]=0
						chk[k-1][j]=1
				
	if direction==3:
		for j in range(n):
			chk=[[0]*n for _ in range(n)]
			for i in range(n-2,-1,-1):
				if new_board[i][j]>0:
					k=i
					while k<=n-2 and new_board[k+1][j]==0:
						new_board[k+1][j]=new_board[k][j]
						new_board[k][j]=0
						k+=1

					if k<=n-2 and new_board[k+1][j]==new_board[k][j] and chk[k+1][j]==0:
						new_board[k+1][j]=2*new_board[k+1][j]
						new_board[k][j]=0
						chk[k+1][j]=1
	return new_board			
					

	
def DFS(board,x):
	global answer
	if x==5:
		max_num=maximum_num(board)	
		if answer<max_num:
			answer=max_num
		return
	for i in range(4):
		new_board=move(board,i,n)
		DFS(new_board,x+1)

DFS(board,0)
print(answer)
		