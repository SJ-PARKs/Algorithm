from collections import deque

n,m=map(int,input().split())
board=[list(input().strip()) for _ in range(n)]
visited=set()
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def getPos():
	for i in range(n):
		for j in range(m):
			if board[i][j]=='R':
				rx,ry=i,j
			if board[i][j]=='B':
				bx,by=i,j
	return rx,ry,bx,by

def move(x,y,dx,dy):
	cnt=0
	while board[x+dx][y+dy]!='#' and board[x][y]!='O':
		x+=dx
		y+=dy
		cnt+=1
	return x,y,cnt

def BFS():
	rx,ry,bx,by=getPos()
	
	q=deque()
	q.append((rx,ry,bx,by,1))
	visited.add((rx,ry,bx,by))
	while len(q)!=0:
		rx,ry,bx,by,result=q.popleft()
		if result>10:
				print(-1)
				return 
		
		for i in range(4):
			nrx,nry,rcnt=move(rx,ry,dx[i],dy[i])
			nbx,nby,bcnt=move(bx,by,dx[i],dy[i])
			
			if board[nbx][nby]=='O':
				continue
			if board[nrx][nry]=='O':
				print(result)
				return
			
			if nrx==nbx and nry==nby:
				if rcnt>bcnt:
					nrx-=dx[i]
					nry-=dy[i]
				else:
					nbx-=dx[i]
					nby-=dy[i]
			if (nrx,nry,nbx,nby) not in visited:
				visited.add((nrx,nry,nbx,nby))
				q.append((nrx,nry,nbx,nby,result+1))
	print(-1)

BFS()
			
			