from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    board=[[-1 for _ in range(102)] for _ in range(102)]
    chk=[[0 for _ in range(102)] for _ in range(102)]
    new_rectangle=[]
    
    for i in range(len(rectangle)):
        new_rectangle.append(list(map(lambda x:x*2,rectangle[i])))
    
    for n in range(len(new_rectangle)):
        for i in range(new_rectangle[n][0],new_rectangle[n][2]+1):
            for j in range(new_rectangle[n][1],new_rectangle[n][3]+1):
                if (i==new_rectangle[n][0] or i==new_rectangle[n][2] or j==new_rectangle[n][1] or j==new_rectangle[n][3]) and (board[i][j]==-1 or board[i][j]==1):
                    board[i][j]=1
                else:
                    board[i][j]=0
    
    start_x,start_y,end_x,end_y=characterX*2,characterY*2,itemX*2,itemY*2
    q=deque()
    q.append((start_x,start_y,0))
    
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    
    while q:
        x,y,d=q.popleft()
        if x==end_x and y==end_y:
            return d//2
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<=101 and 0<=ny<=101:
                if board[nx][ny]==1 and chk[nx][ny]==0:
                    chk[nx][ny]=1
                    q.append((nx,ny,d+1))
                    
    
                
    return answer