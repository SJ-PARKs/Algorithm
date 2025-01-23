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


# n,k=map(int,input().split())
# arr=list(map(int,input().split()))

# p1,p2=0,0
# answer=0
# count=dict()

# def add_count(x):
# 	if x not in count:
# 		count[x]=0
# 	count[x]+=1

# while p2<len(arr):
# 	if arr[p2] in count and count[arr[p2]]>=k:
# 		while count[arr[p1]]==k:
# 			count[arr[p1]]-=1
# 			p1+=1
# 	else:
# 		add_count(arr[p2])
# 		p2+=1
# 	if p2-p1>answer:
# 		answer=p2-p1

# print(answer)
