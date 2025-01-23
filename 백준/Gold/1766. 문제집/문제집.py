import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
heap = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    now = heapq.heappop(heap)
    result.append(now)
    for next_node in graph[now]:
        degree[next_node] -= 1
        if degree[next_node] == 0:
            heapq.heappush(heap, next_node)

print(" ".join(map(str, result)))

# from queue import PriorityQueue

# n,m=map(int,input().split())
# graph=[[0]*(n+1) for _ in range(n+1)]
# degree=[0]*(n+1)
# queue = PriorityQueue()

# for i in range(m):
# 	a,b=map(int,input().split())
# 	graph[a][b]=1
# 	degree[b]+=1
# for i in range(1,n+1):
# 	if degree[i]==0:
# 		queue.put(i)

# while queue.empty() is False:
# 	now=queue.get()
# 	print(now,end=' ')
# 	for i in range(1,n+1):
# 		if graph[now][i]==1:
# 			degree[i]-=1
# 			if degree[i]==0:
# 				queue.put(i)