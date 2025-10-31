n,m=map(int,input().split())
arr=list(map(int,input().split()))
dp=[0]
hap=0
for i in range(len(arr)):
	hap+=arr[i]
	dp.append(hap)
	
answer=100000000000
idx1=0
idx2=1
while idx1 < n and idx2 <= n:	
	if idx2==idx1:
		idx2+=1
		continue
	if idx2==n and dp[idx2]-dp[idx1]<m:
		break
	
	if dp[idx2]-dp[idx1]<m:
		idx2+=1
	else:
		if answer>idx2-idx1:
			answer=idx2-idx1
		idx1+=1
if answer == 100000000000:
	print(0)
else:
	print(answer)