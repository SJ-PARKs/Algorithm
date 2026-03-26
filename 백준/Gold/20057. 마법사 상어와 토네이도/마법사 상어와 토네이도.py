n=int(input())
r,c=n//2,n//2
dr,dc=[0,1,0,-1],[-1,0,1,0]
board=[list(map(int,input().split())) for _ in range(n)]
answer=0

def in_range(r,c):
	global n
	if 0<=r<n and 0<=c<n:
		return True
	else:
		return False

def move(x,y,Dir):
	global answer
	xdx=[[1,-1,2,-2,0,1,-1,1,-1],[-1,-1,0,0,2,0,0,1,1],[1,-1,2,-2,0,1,-1,1,-1],[1,1,0,0,-2,0,0,-1,-1]]
	ydy=[[1,1,0,0,-2,0,0,-1,-1],[1,-1,2,-2,0,1,-1,1,-1],[-1,-1,0,0,2,0,0,1,1],[1,-1,2,-2,0,1,-1,1,-1]]
	percent=[1,1,2,2,5,7,7,10,10]
	finalx=[0,1,0,-1]
	finaly=[-1,0,1,0]
	minus=0
	for i in range(9):
		nx=x+xdx[Dir][i]
		ny=y+ydy[Dir][i]
		tmp=(board[x][y]*percent[i])//100
		if in_range(nx,ny):
			board[nx][ny]+=tmp
			minus+=tmp
		else:
			answer+=tmp
			minus+=tmp
	if in_range(x+finalx[Dir],y+finaly[Dir]):
		board[x+finalx[Dir]][y+finaly[Dir]]+=(board[x][y]-minus)
		board[x][y]=0
	else:
		answer+=(board[x][y]-minus)
		board[x][y]=0
		
	
idx,distance=0,1

while True:
	if r==0 and c==0:
		break
	for i in range(distance):
		nr=r+dr[idx]
		nc=c+dc[idx]
		move(nr,nc,idx)
		r,c=nr,nc
		if r==0 and c==0:
			break
	idx=(idx+1)%4
	if r==0 and c==0:
		break
	for i in range(distance):
		nr=r+dr[idx]
		nc=c+dc[idx]
		move(nr,nc,idx)
		r,c=nr,nc
		if r==0 and c==0:
			break
	idx=(idx+1)%4
	distance+=1

print(answer)
	