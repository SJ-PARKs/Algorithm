import heapq

n = int(input())
m = int(input())

city = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    city[a].append((b, c))

a, b = map(int, input().split())

dist = [float("inf")] * (n + 1)
dist[a] = 0

pq = []
heapq.heappush(pq, (0, a))  

while pq:
    cost, now = heapq.heappop(pq)

    if cost > dist[now]:
        continue

    for nxt, nxt_cost in city[now]:
        nxt_dis = cost + nxt_cost
        if dist[nxt] > nxt_dis:
            dist[nxt] = nxt_dis
            heapq.heappush(pq, (nxt_dis, nxt))

print(dist[b])

# from queue import PriorityQueue

# n=int(input())
# m=int(input())

# city=[[] for _ in range(n+1)]

# for _ in range(m):
# 	a,b,c=map(int,input().split())
# 	city[a].append((b,c))
	

# a,b=map(int,input().split())
# pq=PriorityQueue()

# dist=[float("inf") for _ in range(n+1)]
# dist[a]=0
# pq.put((a,0))
# while pq.empty() is not True:
# 	x=pq.get()
# 	now=x[0]
# 	cost=x[1]
# 	if cost>dist[now]:
# 		continue
# 	for i in range(len(city[now])):
# 		nxt=city[now][i][0]
# 		nxtDis=cost+city[now][i][1]
# 		if dist[nxt]>nxtDis:
# 			dist[nxt]=nxtDis
# 			pq.put((nxt,nxtDis))
				
# print(dist[b])    