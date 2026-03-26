import copy
from collections import deque

n,k=map(int,input().split())
board=[list(map(int,input().split())) for i in range(2**n)]

q=list(map(int,input().split()))

def rotate(r, c, size):
    # [개선 포인트] 전체 board가 아닌, 회전할 부분 격자만 슬라이싱하여 복사합니다.
    # 이렇게 하면 무거운 deepcopy 없이 아주 빠르게 부분 배열을 가져올 수 있습니다.
    tmp = [board[r+i][c:c+size] for i in range(size)]
    
    # [개선 포인트] 잘라낸 부분 격자(tmp)를 시계 방향으로 90도 회전하여 
    # 원본 board의 제자리에 바로 덮어씌웁니다.
    for i in range(size):
        for j in range(size):
            board[r+i][c+j] = tmp[size-1-j][i]
			
def in_range(r,c):
	global n
	if 0<=r<2**n and 0<=c<2**n:
		return True
	return False

def check(r,c):
	count=0
	dr,dc=[-1,0,1,0],[0,1,0,-1]
	for i in range(4):
		nr,nc=r+dr[i],c+dc[i]
		if in_range(nr,nc):
			if board[nr][nc]>0:
				count+=1
	return count

def count_ice():
	global n
	count=0
	for i in range(2**n):
		for j in range(2**n):
			count+=board[i][j]
	return count

def count_ice1():
	global n
	chk=[[0 for _ in range(2**n)] for _ in range(2**n)]
	dr,dc=[0,1,0,-1],[1,0,-1,0]
	q=deque()
	answer=0
	for r in range(2**n):
		for c in range(2**n):
			if chk[r][c]==0:
				if board[r][c]==0:
					chk[r][c]=1
				else:
					count=1
					q.append((r,c))
					chk[r][c]=1
					while q:
						rr,cc=q.popleft()
						for idx in range(4):
							nr,nc=rr+dr[idx],cc+dc[idx]
							if in_range(nr,nc):
								if chk[nr][nc]==0 and board[nr][nc]>0:
									count+=1
									chk[nr][nc]=1
									q.append((nr,nc))
					if count>answer:
						answer=count
	return answer

for i in range(len(q)):
	size=2**q[i]
	tmp_board=[[0 for _ in range(2**n)] for _ in range(2**n)]
	for r in range(0,2**n,size):
		for c in range(0,2**n,size):
			rotate(r,c,size)
	
	for r in range(2**n):
		for c in range(2**n):
			count=check(r,c)
			if count<3 and board[r][c]>0:
				tmp_board[r][c]=board[r][c]-1
				
			else:
				tmp_board[r][c]=board[r][c]
	board=copy.deepcopy(tmp_board)
	
print(count_ice())
print(count_ice1())
