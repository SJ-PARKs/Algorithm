import heapq

n,m=map(int,input().split())
arr=list(map(int,input().split()))

heapq.heapify(arr)


for i in range(m):
	x1=heapq.heappop(arr)
	x2=heapq.heappop(arr)
	heapq.heappush(arr,x1+x2)
	heapq.heappush(arr,x1+x2)
	
print(sum(arr))