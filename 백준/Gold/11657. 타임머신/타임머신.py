n,m=map(int,input().split())
graph=[]
for _ in range(m):
    graph.append(list(map(int,input().split())))

dist=[float("inf")]*(n+1)
dist[1]=0
for _ in range(n-1):
    for i in range(len(graph)):
        if dist[graph[i][0]]+graph[i][2]<dist[graph[i][1]]:
            dist[graph[i][1]]=dist[graph[i][0]]+graph[i][2]

flag=False
for i in range(len(graph)):
    if dist[graph[i][0]]+graph[i][2]<dist[graph[i][1]]:
        flag=True
        break
if flag==True:
    print(-1)
else:
    for i in range(2,n+1):
        if dist[i]==float('inf'):
            print(-1)
        else:
            print(dist[i])