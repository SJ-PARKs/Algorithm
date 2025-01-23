import sys
input = sys.stdin.readline 

n,k=map(int,input().split())
arr=list(map(int,input().split()))

chk=[0]*(1000001)
e,s=0,0
result=0
maximum=0
while s<len(arr):
	if chk[arr[s]]<k:
		chk[arr[s]]+=1
		s+=1
	else:
		chk[arr[e]]-=1
		e+=1
	if s-e>maximum:
		maximum=s-e
print(maximum)

		
