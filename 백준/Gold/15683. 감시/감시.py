n,m=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(n)]
location=[]
for i in range(n):
	for j in range(m):
		if 0<board[i][j]<6:
			location.append((i,j,board[i][j]))

			
minimum=float("inf")			
def DFS(num):
	global minimum
	if num==len(location):
		count=0
		for i in range(n):
			for j in range(m):
				if board[i][j]==0:
					count+=1
					
		if count<minimum:
			minimum=count
	
		return
	
	x,y,d=location[num]
	if d==1:
		visit=[]
		for j in range(y+1,m):
			if board[x][j]==6:
				break
			if board[x][j]!=0:
				continue
			board[x][j]=-1
			visit.append(j)
		DFS(num+1)
		for j in range(len(visit)):
			board[x][visit[j]]=0
		visit=[]
		for j in range(y,-1,-1):
			if board[x][j]==6:
				break
			if board[x][j]!=0:
				continue
			board[x][j]=-1
			visit.append(j)
		DFS(num+1)
		for j in range(len(visit)):
			board[x][visit[j]]=0
		visit=[]
		for i in range(x+1,n):
			if board[i][y]==6:
				break
			if board[i][y]!=0:
				continue
			board[i][y]=-1
			visit.append(i)
		DFS(num+1)
		for i in range(len(visit)):
			board[visit[i]][y]=0
		visit=[]
		for i in range(x,-1,-1):
			if board[i][y]==6:
				break
			if board[i][y]!=0:
				continue
			board[i][y]=-1
			visit.append(i)
		DFS(num+1)
		for i in range(len(visit)):
			board[visit[i]][y]=0
			
	if d==2:
		visit=[]
		for i in range(x,n):
			if board[i][y]==6:
				break
			if board[i][y]!=0:
				continue
			board[i][y]=-1
			visit.append(i)
		for i in range(x,-1,-1):
			if board[i][y]==6:
				break
			if board[i][y]!=0:
				continue
			board[i][y]=-1
			visit.append(i)	
		DFS(num+1)
		for i in range(len(visit)):
			board[visit[i]][y]=0
		visit=[]
		for i in range(y,m):
			if board[x][i]==6:
				break
			if board[x][i]!=0:
				continue
			board[x][i]=-1
			visit.append(i)
		for i in range(y,-1,-1):
			if board[x][i]==6:
				break
			if board[x][i]!=0:
				continue
			board[x][i]=-1
			visit.append(i)
		DFS(num+1)
		for i in range(len(visit)):
			board[x][visit[i]]=0
	
	if d==3:
		visitX=[]
		visitY=[]
		for j in range(y,m):
			if board[x][j]==6:
				break
			if board[x][j]!=0:
				continue
			board[x][j]=-1
			visitY.append(j)
		for i in range(x,n):
			if board[i][y]==6:
				break
			if board[i][y]!=0:
				continue
			board[i][y]=-1
			visitX.append(i)
		DFS(num+1)
		for i in range(len(visitX)):
			board[visitX[i]][y]=0
		for j in range(len(visitY)):
			board[x][visitY[j]]=0
		
		visitX=[]
		visitY=[]
		for j in range(y,m):
			if board[x][j]==6:
				break
			if board[x][j]!=0:
				continue
			board[x][j]=-1
			visitY.append(j)
		for i in range(x,-1,-1):
			if board[i][y]==6:
				break
			if board[i][y]!=0:
				continue
			board[i][y]=-1
			visitX.append(i)
		DFS(num+1)
		for i in range(len(visitX)):
			board[visitX[i]][y]=0
		for j in range(len(visitY)):
			board[x][visitY[j]]=0
			
		visitX=[]
		visitY=[]
		for j in range(y,-1,-1):
			if board[x][j]==6:
				break
			if board[x][j]!=0:
				continue
			board[x][j]=-1
			visitY.append(j)
		for i in range(x,n):
			if board[i][y]==6:
				break
			if board[i][y]!=0:
				continue
			board[i][y]=-1
			visitX.append(i)
		DFS(num+1)
		for i in range(len(visitX)):
			board[visitX[i]][y]=0
		for j in range(len(visitY)):
			board[x][visitY[j]]=0
			
		visitX=[]
		visitY=[]
		for j in range(y,-1,-1):
			if board[x][j]==6:
				break
			if board[x][j]!=0:
				continue
			board[x][j]=-1
			visitY.append(j)
		for i in range(x,-1,-1):
			if board[i][y]==6:
				break
			if board[i][y]!=0:
				continue
			board[i][y]=-1
			visitX.append(i)
		DFS(num+1)
		for i in range(len(visitX)):
			board[visitX[i]][y]=0
		for j in range(len(visitY)):
			board[x][visitY[j]]=0
			
	if d==4:
		visitX=[]
		visitY=[]
		for j in range(y,m):
			if board[x][j]==6:
				break
			if board[x][j]!=0:
				continue
			board[x][j]=-1
			visitY.append(j)
		for j in range(y,-1,-1):
			if board[x][j]==6:
				break
			if board[x][j]!=0:
				continue
			board[x][j]=-1
			visitY.append(j)
		for i in range(x,n):
			if board[i][y]==6:
				break
			if board[i][y]!=0:
				continue
			board[i][y]=-1
			visitX.append(i)
		DFS(num+1)
		for i in range(len(visitX)):
			board[visitX[i]][y]=0
		for j in range(len(visitY)):
			board[x][visitY[j]]=0
		
		visitX=[]
		visitY=[]
		for j in range(y,-1,-1):
			if board[x][j]==6:
				break
			if board[x][j]!=0:
				continue
			board[x][j]=-1
			visitY.append(j)
		for j in range(y,m):
			if board[x][j]==6:
				break
			if board[x][j]!=0:
				continue
			board[x][j]=-1
			visitY.append(j)
		for i in range(x,-1,-1):
			if board[i][y]==6:
				break
			if board[i][y]!=0:
				continue
			board[i][y]=-1
			visitX.append(i)
		
		DFS(num+1)
		for i in range(len(visitX)):
			board[visitX[i]][y]=0
		for j in range(len(visitY)):
			board[x][visitY[j]]=0
		
		visitX=[]
		visitY=[]
		for j in range(y,m):
			if board[x][j]==6:
				break
			if board[x][j]!=0:
				continue
			board[x][j]=-1
			visitY.append(j)
		for i in range(x,-1,-1):
			if board[i][y]==6:
				break
			if board[i][y]!=0:
				continue
			board[i][y]=-1
			visitX.append(i)
		for i in range(x,n):
			if board[i][y]==6:
				break
			if board[i][y]!=0:
				continue
			board[i][y]=-1
			visitX.append(i)
		DFS(num+1)
		for i in range(len(visitX)):
			board[visitX[i]][y]=0
		for j in range(len(visitY)):
			board[x][visitY[j]]=0
			
		visitX=[]
		visitY=[]
		for j in range(y-1,-1,-1):
			if board[x][j]==6:
				break
			if board[x][j]!=0:
				continue
			board[x][j]=-1
			visitY.append(j)
		for i in range(x-1,-1,-1):
			if board[i][y]==6:
				break
			if board[i][y]!=0:
				continue
			board[i][y]=-1
			visitX.append(i)
		for i in range(x,n):
			if board[i][y]==6:
				break
			if board[i][y]!=0:
				continue
			board[i][y]=-1
			visitX.append(i)
		DFS(num+1)
		for i in range(len(visitX)):
			board[visitX[i]][y]=0
		for j in range(len(visitY)):
			board[x][visitY[j]]=0
		
	if d==5:
		visitX=[]
		visitY=[]
		for j in range(y,m):
			if board[x][j]==6:
				break
			if board[x][j]!=0:
				continue
			board[x][j]=-1
			visitY.append(j)
		for j in range(y-1,-1,-1):
			if board[x][j]==6:
				break
			if board[x][j]!=0:
				continue
			board[x][j]=-1
			visitY.append(j)
		for i in range(x,n):
			if board[i][y]==6:
				break
			if board[i][y]!=0:
				continue
			board[i][y]=-1
			visitX.append(i)
		for i in range(x-1,-1,-1):
			if board[i][y]==6:
				break
			if board[i][y]!=0:
				continue
			board[i][y]=-1
			visitX.append(i)
		DFS(num+1)
		for i in range(len(visitX)):
			board[visitX[i]][y]=0
		for j in range(len(visitY)):
			board[x][visitY[j]]=0
		
DFS(0)
print(minimum)