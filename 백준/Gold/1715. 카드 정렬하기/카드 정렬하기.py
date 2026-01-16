import heapq

n=int(input())
arr=[]
for i in range(n):
	heapq.heappush(arr,int(input()))
answer=0
if n==1:
	print(0)
else:
	while len(arr)>1:
		a=heapq.heappop(arr)
		b=heapq.heappop(arr)
		answer+=(a+b)
		heapq.heappush(arr,a+b)

	print(answer)