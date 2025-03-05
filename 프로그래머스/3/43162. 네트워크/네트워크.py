def solution(n, computers):
    answer = 0
    network=[[] for _ in range(n+1)]
    global chk
    chk=[0 for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if computers[i][j]==1:
                network[i+1].append(j+1)
    
    print(network)
    for i in range(len(network)):
        if chk[i]==0:
            DFS(i,network) 
            answer+=1

    return answer-1

def DFS(x,network):
    global chk
    if chk[x]==1:
        return
    chk[x]=1
    for computer in network[x]:
        DFS(computer,network)
        
        