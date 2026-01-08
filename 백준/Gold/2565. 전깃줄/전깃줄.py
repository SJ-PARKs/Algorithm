from bisect import bisect_left

n=int(input())
arr=[]
for i in range(n):
	a,b=map(int,input().split())
	arr.append((a,b))
arr=sorted(arr)
arr1=[]
for i in range(n):
	arr1.append(arr[i][1])

tails=[]
tails.append(arr1[0])

for i in range(1,len(arr1)):
	idx=bisect_left(tails,arr1[i])
	if idx==len(tails):
		tails.append(arr1[i])
	elif arr1[i]<tails[idx]:
		tails[idx]=arr1[i]
	
print(len(arr)-len(tails))