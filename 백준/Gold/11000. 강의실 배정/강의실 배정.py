import heapq

n=int(input())
classes=[]
heap=[]
for i in range(n):
	s,e=map(int,input().split())
	classes.append((s,e))
classes.sort(key=lambda x:x[0])

s,e=classes[0]
answer=1
heapq.heappush(heap,e)
for i in range(1,n):
	if classes[i][0]<heap[0]:
		answer+=1
		heapq.heappush(heap,classes[i][1])
	else:
		heapq.heappop(heap)
		heapq.heappush(heap,classes[i][1])

	 
print(answer)