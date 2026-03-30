import heapq

n=int(input())
tasks=[
	list(map(int,input().split()))
	for _ in range(n)
]

tasks.sort(key=lambda x:(x[0],-x[1]))
q=[]
time=1
for i in range(len(tasks)):
	if tasks[i][0]>=time:
		heapq.heappush(q,tasks[i][1])
		time+=1
	else:
		if q[0]<tasks[i][1]:
			heapq.heappop(q)
			heapq.heappush(q,tasks[i][1])
			
print(sum(q))