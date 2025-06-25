n,m=map(int,input().split())
MAP = [list(input()) for _ in range(n)]
chk = [[[i,j] for j in range(m)] for i in range(n)]

def Find(x, y):
    if chk[x][y] != [x, y]:
        chk[x][y] = list(Find(chk[x][y][0], chk[x][y][1]))
    return chk[x][y]

def Union(x1,y1,x2,y2):
	a=Find(x1,y1)
	b=Find(x2,y2)
	if a != b:
		chk[a[0]][a[1]] = [b[0], b[1]]
		
for i in range(n):
	for j in range(m):
		if MAP[i][j]=="D":
			if i+1<n:
				Union(i,j,i+1,j)
		elif MAP[i][j]=="L":
			if j-1>=0:
				Union(i,j,i,j-1)
		elif MAP[i][j]=="R":
			if j+1<m:
				Union(i,j,i,j+1)
		else:
			if i-1>=0:
				Union(i,j,i-1,j)

roots = set()
for i in range(n):
    for j in range(m):
        roots.add(tuple(Find(i, j)))

print(len(roots))
	
	