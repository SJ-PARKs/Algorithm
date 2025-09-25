from collections import deque
import copy

R,C,M=map(int,input().split())
board=[[(0,0,0)]*C for _ in range(R)]

dx=[-1,1,0,0]
dy=[0,0,1,-1]
sharks=[]
for i in range(M):
	r,c,s,d,z=map(int,input().split())
	board[r-1][c-1]=(s,d,z)
	sharks.append((r-1,c-1,s,d,z))
answer=0

def move(x, y, s, direction):
    nx, ny = x, y
    ndx, ndy = dx[direction-1], dy[direction-1]

    # 1) 속도 모듈러 최적화 (주기)
    if ndx != 0:  # 세로 이동
        period = 0 if R == 1 else 2 * (R - 1)
    else:         # 가로 이동
        period = 0 if C == 1 else 2 * (C - 1)
    if period:    # period가 0이면(한 줄 격자) 생략
        s %= period

    # 2) 경계 처리: 다음 칸이 밖이면 먼저 반전 후 이동
    for _ in range(s):
        if not (0 <= nx + ndx < R):
            ndx = -ndx
        if not (0 <= ny + ndy < C):
            ndy = -ndy
        nx += ndx
        ny += ndy

    new_dir = 0
    for i in range(4):
        if ndx == dx[i] and ndy == dy[i]:
            new_dir = i + 1
            break
    return nx, ny, new_dir



for j in range(C):
	for i in range(R):
		if board[i][j][2]>0:
			answer+=board[i][j][2]
			board[i][j]=(0,0,0)
			break
	sharks=[]
	for k in range(R):
		for l in range(C):
			if board[k][l][2]>0:
				sharks.append((k,l,board[k][l][0],board[k][l][1],board[k][l][2]))
	
	new_board=[[(0,0,0)]*C for _ in range(R)]
	for nr,nc,ns,nd,nz in sharks:
		nnr,nnc,nnd=move(nr,nc,ns,nd)
		if nz>new_board[nnr][nnc][2]:
			new_board[nnr][nnc]=(ns,nnd,nz)
	board=copy.deepcopy(new_board)


print(answer)

