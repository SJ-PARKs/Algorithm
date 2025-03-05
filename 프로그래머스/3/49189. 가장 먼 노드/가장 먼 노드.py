from collections import deque

def solution(n, edge):
    answer = 0
    edge=sorted(edge)
    graph=[[] for i in range(n+1)]
    chk=[[] for i in range(n+1)]
    distance=[0]*(n+1)
    for x in edge:
        graph[x[0]].append(x[1])
        graph[x[1]].append(x[0])
    
    queue=deque()
    cnt=1
    queue.append(1)
    distance[1]=1
    while len(queue)!=0:
        x=queue.popleft()
        for i in graph[x]:
            if distance[i]==0:
                queue.append(i)
                distance[i]=distance[x]+1
                
    maximum=max(distance)

    print(distance)
    for x in distance:
        if maximum==x:
            answer+=1
            
    return answer