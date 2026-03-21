import copy

n,m=map(int,input().split())
mid_r,mid_c=n//2,n//2

grid=[
	list(map(int,input().split()))
	for _ in range(n)
]
answer=dict()
answer[1]=0
answer[2]=0
answer[3]=0

def in_range(r,c):
	if 0<=r<n and 0<=c<n:
		return True
	else:
		return False

def blizzard(grid,d,s):
	dr,dc=[-1,1,0,0],[0,0,-1,1]
	nr,nc=mid_r,mid_c
	for _ in range(s):
		nr+=dr[d-1]
		nc+=dc[d-1]
		if in_range(nr,nc)==False:
			break
		grid[nr][nc]=0
			
def find_not_zero(grid,r,c):
	nr,nc=r,c
	while True:
		if nr>mid_r and 2*mid_r-nr<=nc<nr:
			nr,nc=nr,nc+1
		elif nr<mid_r and nr<nc<=2*mid_r-nr:
			nr,nc=nr,nc-1
		elif nc<mid_c and nc<nr<2*mid_c-nc:
			nr,nc=nr+1,nc
		elif nc>mid_c and 2*mid_c-nc<nr<=nc:
			nr,nc=nr-1,nc
		elif nr==nc:
			nr,nc=nr,nc-1

		if grid[nr][nc]!=0:
			return nr,nc
		if nr==0 and nc==0:
			return -1,-1

def move(grid):
	nr,nc=mid_r,mid_c-1

	while True:
		if nr==0 and nc==0:
			break
		
		if grid[nr][nc]==0:
			nnr,nnc=find_not_zero(grid,nr,nc)
			if nnr==-1 and nnc==-1:
				break
			grid[nr][nc]=grid[nnr][nnc]
			grid[nnr][nnc]=0
		
		if nr>mid_r and 2*mid_r-nr<=nc<nr:
			nr,nc=nr,nc+1
		elif nr<mid_r and nr<nc<=2*mid_r-nr:
			nr,nc=nr,nc-1
		elif nc<mid_c and nc<nr<2*mid_c-nc:
			nr,nc=nr+1,nc
		elif nc>mid_c and 2*mid_c-nc<nr<=nc:
			nr,nc=nr-1,nc
		elif nr==nc:
			nr,nc=nr,nc-1
	
def find_broken(grid):
	nr,nc=mid_r,mid_c-1
	sequence=[(nr,nc)]
	arr=[]	
	while True:
		if nr==0 and nc==0:
			arr.append(sequence)
			return arr
		tmp=grid[nr][nc]	
		if nr>mid_r and 2*mid_r-nr<=nc<nr:
			nr,nc=nr,nc+1
		elif nr<mid_r and nr<nc<=2*mid_r-nr:
			nr,nc=nr,nc-1
		elif nc<mid_c and nc<nr<2*mid_c-nc:
			nr,nc=nr+1,nc
		elif nc>mid_c and 2*mid_c-nc<nr<=nc:
			nr,nc=nr-1,nc
		elif nr==nc:
			nr,nc=nr,nc-1
		
		if tmp==grid[nr][nc]:
			sequence.append((nr,nc))
		else:
			arr.append(sequence)
			sequence=[(nr,nc)]
				
def broken(grid):
	flag=False
	while True:
		arr=find_broken(grid)
		del_arr=[]
		for i in range(len(arr)):
			if len(arr[i])>=4:
				if grid[arr[i][0][0]][arr[i][0][1]]!=0:
					del_arr.append(arr[i])
		if len(del_arr)==0:
			break
		else:
			flag=True
			for i in range(len(del_arr)):
				for j in range(len(del_arr[i])):
					answer[grid[del_arr[i][j][0]][del_arr[i][j][1]]]+=1
					grid[del_arr[i][j][0]][del_arr[i][j][1]]=0
					
	return flag

def change(grid):
	nr,nc=mid_r,mid_c-1
	sequence=[(nr,nc)]
	arr=[]	
	while True:
		if nr==0 and nc==0:
			arr.append(sequence)
			break
		tmp=grid[nr][nc]	
		if nr>mid_r and 2*mid_r-nr<=nc<nr:
			nr,nc=nr,nc+1
		elif nr<mid_r and nr<nc<=2*mid_r-nr:
			nr,nc=nr,nc-1
		elif nc<mid_c and nc<nr<2*mid_c-nc:
			nr,nc=nr+1,nc
		elif nc>mid_c and 2*mid_c-nc<nr<=nc:
			nr,nc=nr-1,nc
		elif nr==nc:
			nr,nc=nr,nc-1
		
		if tmp==grid[nr][nc]:
			sequence.append((nr,nc))
		else:
			arr.append(sequence)
			sequence=[(nr,nc)]
			
	new_grid=[[0 for _ in range(n)] for _ in range(n)]
	nr,nc=mid_r,mid_c-1
	
	if grid[arr[0][0][0]][arr[0][0][1]] == 0:
		return new_grid
	
	new_grid[nr][nc]=len(arr[0])
	nr,nc=nr+1,nc
	new_grid[nr][nc]=grid[arr[0][0][0]][arr[0][0][1]]
	for i in range(1,len(arr)):
		if grid[arr[i][0][0]][arr[i][0][1]]==0:
			break
		if nr>mid_r and 2*mid_r-nr<=nc<nr:
			nr,nc=nr,nc+1
		elif nr<mid_r and nr<nc<=2*mid_r-nr:
			nr,nc=nr,nc-1
		elif nc<mid_c and nc<nr<2*mid_c-nc:
			nr,nc=nr+1,nc
		elif nc>mid_c and 2*mid_c-nc<nr<=nc:
			nr,nc=nr-1,nc
		elif nr==nc:
			nr,nc=nr,nc-1
			
		new_grid[nr][nc]=len(arr[i])	
		if nr==0 and nc==0:
			break
		
		if nr>mid_r and 2*mid_r-nr<=nc<nr:
			nr,nc=nr,nc+1
		elif nr<mid_r and nr<nc<=2*mid_r-nr:
			nr,nc=nr,nc-1
		elif nc<mid_c and nc<nr<2*mid_c-nc:
			nr,nc=nr+1,nc
		elif nc>mid_c and 2*mid_c-nc<nr<=nc:
			nr,nc=nr-1,nc
		elif nr==nc:
			nr,nc=nr,nc-1
	
		new_grid[nr][nc]=grid[arr[i][0][0]][arr[i][0][1]]	
		if nr==0 and nc==0:
			break
	return new_grid
	
	
for _ in range(m):
	d,s=map(int,input().split())
	blizzard(grid,d,s)

	move(grid)
	while True:
		flag=broken(grid)
		if flag==False:
			break
		move(grid)
	grid=copy.deepcopy(change(grid))
	
print(answer[1]+2*answer[2]+3*answer[3])