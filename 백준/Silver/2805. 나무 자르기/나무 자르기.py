n,m=map(int,input().split())
tree=list(map(int,input().split()))

l=0
r=max(tree)+1
answer=0
while l<=r:
	mid=(l+r)//2
	hap=0
	for i in range(len(tree)):
		if tree[i]-mid>0:
			hap+=(tree[i]-mid)
	
	if hap>=m:
		answer=mid
		l=mid+1
	else:
		r=mid-1
	
print(answer)

