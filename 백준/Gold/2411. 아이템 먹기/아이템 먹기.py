n,m,a,b=map(int,input().split())

chk=[[0 for _ in range(m)] for _ in range(n)]
items=[(0,0),(n-1,m-1)]

for i in range(a):
	x,y=map(int,input().split())
	items.append((x-1,y-1))
	
for i in range(b):
	x,y=map(int,input().split())
	chk[x-1][y-1]=1
	
items=sorted(items)

def calculate(x1,y1,x2,y2):
	board=[[0 for _ in range(m)] for _ in range(n)]
	if chk[x1][y1]==0:
		board[x1][y1]=1
	for i in range(x1+1,x2+1):
		if chk[i][y1]==1:
			break
		board[i][y1]=board[i-1][y1]
	for i in range(y1+1,y2+1):
		if chk[x1][i]:
			break
		board[x1][i]=board[x1][i-1]
	
	for i in range(x1+1,x2+1):
		for j in range(y1+1,y2+1):
			if chk[i][j]==1:
				continue
			board[i][j]=board[i-1][j]+board[i][j-1]
			
	return board[x2][y2]

answer=1

for i in range(1,len(items)):
	answer*=calculate(items[i-1][0],items[i-1][1],items[i][0],items[i][1])
	
print(answer)
			
		
	
