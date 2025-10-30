def solution(n, computers):
    global graph,chk
    answer = 0
    chk=[0 for _ in range(n+1)]
    graph=[[] for _ in range(n+1)]
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i==j:
                continue
            if computers[i][j]==1:
                graph[i+1].append(j+1)
 
    for i in range(1,n+1):
        if chk[i]==0:
            answer+=1
            DFS(i)
    
    return answer

def DFS(n):
    global graph,chk

    if chk[n]==1:
        return
    chk[n]=1
    for i in range(len(graph[n])):
        if chk[graph[n][i]]==0:
            DFS(graph[n][i])
        