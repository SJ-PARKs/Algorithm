from bisect import bisect_left

n=int(input())
arr=[]

for _ in range(n):
	a,b=map(int,input().split())
	arr.append((a,b))
	
arr.sort()

tails=[]
trace=[]

tails.append(arr[0][1])
trace.append((0,arr[0][0]))
for i in range(1,n):
	b_val=arr[i][1]
	a_val=arr[i][0]
	
	if b_val>tails[-1]:
		tails.append(b_val)
		trace.append((len(tails)-1,a_val))
	else:
		idx=bisect_left(tails,b_val)
		tails[idx]=b_val
		trace.append((idx,a_val))
		
print(n-len(tails))

lis_a_values=set()
target_idx=len(tails)-1

for i in range(len(trace)-1,-1,-1):
	if trace[i][0]==target_idx:
		lis_a_values.add(trace[i][1])
		target_idx-=1

removed_list=[]
for i in range(n):
	if arr[i][0] not in lis_a_values:
		removed_list.append(arr[i][0])
for val in removed_list:
	print(val)
		