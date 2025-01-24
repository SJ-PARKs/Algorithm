n=int(input())

arr=[]

for _ in range(n):
	arr.append(list(map(int,input().split())))

dp_max=[0,0,0] 
dp_min=[0,0,0]

dp_max[0],dp_max[1],dp_max[2]=arr[0][0],arr[0][1],arr[0][2]
dp_min[0],dp_min[1],dp_min[2]=arr[0][0],arr[0][1],arr[0][2]
tmp_max=[0,0,0]
tmp_min=[0,0,0]
for i in range(1,n):
	tmp_max[0]=max(dp_max[0],dp_max[1])+arr[i][0]
	tmp_min[0]=min(dp_min[0],dp_min[1])+arr[i][0]
			  
	tmp_max[1]=max(max(dp_max[0],dp_max[1]),dp_max[2])+arr[i][1]
	tmp_min[1]=min(min(dp_min[0],dp_min[1]),dp_min[2])+arr[i][1]

	tmp_max[2]=max(dp_max[2],dp_max[1])+arr[i][2]
	tmp_min[2]=min(dp_min[2],dp_min[1])+arr[i][2]
	
	dp_max[0],dp_max[1],dp_max[2]=tmp_max[0],tmp_max[1],tmp_max[2]
	dp_min[0],dp_min[1],dp_min[2]=tmp_min[0],tmp_min[1],tmp_min[2]
	
print(max(max(dp_max[0],dp_max[1]),dp_max[2]),end=' ')
print(min(min(dp_min[0],dp_min[1]),dp_min[2]),end=' ')
			   