import heapq

n,e=map(int,input().split())

graph=[[] for _ in range(n+1)]

for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2=map(int,input().split())

dist=[float("inf") for _ in range(n+1)]
dist[1]=0
q=[]
heapq.heappush(q,(0,1))

while q:
    now=q[0][1]
    cost=q[0][0]
    heapq.heappop(q)
    if cost>dist[now]:
        continue
    for i in range(len(graph[now])):
        next=graph[now][i][0]
        nextDis=cost+graph[now][i][1]
        if dist[next]>nextDis:
            dist[next]=nextDis
            heapq.heappush(q,(nextDis,next))

dist1=[float("inf") for _ in range(n+1)]
dist1[v1]=0
q1=[]
heapq.heappush(q1,(0,v1))

while q1:
    now=q1[0][1]
    cost=q1[0][0]
    heapq.heappop(q1)
    if cost>dist1[now]:
        continue
    for i in range(len(graph[now])):
        next=graph[now][i][0]
        nextDis=cost+graph[now][i][1]
        if dist1[next]>nextDis:
            dist1[next]=nextDis
            heapq.heappush(q1,(nextDis,next))

dist2=[float("inf") for _ in range(n+1)]
dist2[v2]=0
q2=[]
heapq.heappush(q2,(0,v2))

while q2:
    now=q2[0][1]
    cost=q2[0][0]
    heapq.heappop(q2)
    if cost>dist2[now]:
        continue
    for i in range(len(graph[now])):
        next=graph[now][i][0]
        nextDis=cost+graph[now][i][1]
        if dist2[next]>nextDis:
            dist2[next]=nextDis
            heapq.heappush(q2,(nextDis,next))


x=min(dist[v1]+dist1[v2]+dist2[n],dist[v2]+dist2[v1]+dist1[n])
if x==float("inf"):
    print(-1)
else:
    print(x)