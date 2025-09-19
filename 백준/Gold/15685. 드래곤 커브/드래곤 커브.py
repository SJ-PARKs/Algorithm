dx=[1,0,-1,0]
dy=[0,-1,0,1]

n=int(input())
board = [[0]*101 for _ in range(101)]

for _ in range(n):
	x,y,d,g=map(int,input().split())
	dirs=[d]

	for _ in range(g):
		for t in reversed(dirs):
			dirs.append((t+1)%4)
			
	board[y][x]=1
	cx,cy=x,y
	for t in dirs:
		nx,ny=cx+dx[t], cy+dy[t]
		if 0<=nx<=100 and 0<=ny<=100:
			board[ny][nx]=1
			cx,cy=nx,ny
			
ans = 0
for r in range(100):
    for c in range(100):
        if board[r][c] and board[r][c+1] and board[r+1][c] and board[r+1][c+1]:
            ans += 1
print(ans)