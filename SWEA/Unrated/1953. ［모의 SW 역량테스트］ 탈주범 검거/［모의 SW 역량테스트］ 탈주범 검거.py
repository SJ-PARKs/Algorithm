from collections import deque
pipe=dict()
pipe[1]=[[0,1],[1,0],[-1,0],[0,-1]]
pipe[2]=[[1,0],[-1,0]]
pipe[3]=[[0,1],[0,-1]]
pipe[4]=[[0,1],[-1,0]]
pipe[5]=[[0,1],[1,0]]
pipe[6]=[[1,0],[0,-1]]
pipe[7]=[[-1,0],[0,-1]]

t=int(input())
for tt in range(t):
    n,m,r,c,l=map(int,input().split())

    board=[]
    for i in range(n):
        board.append(list(map(int,input().split())))
    chk=[[0 for _ in range(m)] for _ in range(n)]

    q=deque()
    q.append((r,c))
    time=1
    chk[r][c]=1

    for i in range(1,l):
        new_q = deque()
        while q:
            x,y=q.popleft()
            for dx,dy in pipe[board[x][y]]:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<m:
                    if chk[nx][ny]==0 and board[nx][ny]>0:
                        flag=False
                        for dx1,dy1 in pipe[board[nx][ny]]:
                            if nx+dx1==x and ny+dy1==y:
                                flag=True
                                break
                        if flag==True:
                            new_q.append((nx,ny))
                            chk[nx][ny]=1
        q=new_q

    count=0
    for i in range(n):
        for j in range(m):
            if chk[i][j]==1:
                count+=1
    print("#"+str(tt+1)+" "+str(count))
