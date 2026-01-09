from bisect import bisect_left

n=int(input())

arr=list(map(int,input().split()))

tails=[]
dp=[0]*n
tails.append(arr[0])

for i in range(1,n):
	idx=bisect_left(tails,arr[i])
	if idx==len(tails):
		tails.append(arr[i])
	elif arr[i]<tails[idx]:
		tails[idx]=arr[i]
	dp[i]=idx

	

maximum=max(dp)
print(maximum+1)
answer=[]
for i in range(len(dp)-1,-1,-1):
	if maximum==-1:
		break
	if dp[i]==maximum:
		answer.append(arr[i])
		maximum-=1

for i in range(len(answer)-1,-1,-1):
	print(answer[i],end=' ')