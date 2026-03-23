r,c,k=map(int,input().split())
a=[
	list(map(int,input().split()))
	for _ in range(3)
]

def R():
	global a
	new_arr=[]
	maximum=0
	for i in range(len(a)):
		count=dict()
		arr=[]
		arrs=[]
		for j in range(len(a[i])):
			if a[i][j]==0:
				continue
			if a[i][j] not in count:
				count[a[i][j]]=0
			count[a[i][j]]+=1
		for k,v in count.items():
			arr.append((k,v))
		arr.sort(key=lambda x:x[0])
		arr.sort(key=lambda x:x[1])
		for k in range(len(arr)):
			arrs.append(arr[k][0])
			arrs.append(arr[k][1])
		new_arr.append(arrs)
		if len(arrs)>=maximum:
			maximum=len(arrs)
			
	for i in range(len(new_arr)):
		if len(new_arr[i])<maximum:
			for j in range(maximum-len(new_arr[i])):
				new_arr[i].append(0)
	a=new_arr
		
def C():
	global a
	tmp_arr=[]
	new_arr=[]
	maximum=0
	for i in range(len(a[0])):
		count=dict()
		arr=[]
		arrs=[]
		for j in range(len(a)):
			if a[j][i]==0:
				continue
			if a[j][i] not in count:
				count[a[j][i]]=0
			count[a[j][i]]+=1
		for k,v in count.items():
			arr.append((k,v))
		arr.sort(key=lambda x:x[0])
		arr.sort(key=lambda x:x[1])
		for k in range(len(arr)):
			arrs.append(arr[k][0])
			arrs.append(arr[k][1])
		tmp_arr.append(arrs)	
		if len(arrs)>=maximum:
			maximum=len(arrs)
		
	for i in range(len(tmp_arr)):			
		for j in range(maximum-len(tmp_arr[i])):
			tmp_arr[i].append(0)
	for i in range(len(tmp_arr[0])):
		tmp_arr1=[]
		for j in range(len(tmp_arr)):
			tmp_arr1.append(tmp_arr[j][i])
		new_arr.append(tmp_arr1)
	a=new_arr		

idx=0
while True:
	if 0<=r-1<len(a) and 0<=c-1<len(a[0]): 
		if a[r-1][c-1]==k:
			print(idx)
			break	
	if len(a)>=len(a[0]):
		R()
	else:
		C()
	idx+=1
	if idx==101:
		print(-1)
		break

