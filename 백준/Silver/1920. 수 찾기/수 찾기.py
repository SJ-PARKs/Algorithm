n=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr)
m=int(input())
search=list(map(int,input().split()))


def binary_search(arr,k):
	l,r,answer=0,len(arr)-1,len(arr)
	while l<=r:
		mid=(l+r)//2
		if arr[mid]<k:
			l=mid+1
		elif arr[mid]>k:
			r=mid-1
		else:
			answer=mid
			break
	if answer==len(arr):
		return -1
	else:
		return answer

for i in range(len(search)):
	ans=binary_search(arr,search[i])
	if ans==-1:
		print(0)
	else:
		print(1)