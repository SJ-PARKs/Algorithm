def solution(k, dungeons):
    global answer
    answer=-1
    chk=[0 for _ in range(len(dungeons))]
    DFS(k,dungeons,chk,0)
    return answer
def DFS(k,dungeons,chk,cnt):
    global answer
    if cnt>answer:
        answer=cnt
    for i in range(len(dungeons)):
        if k>=dungeons[i][0] and chk[i]==0:
            k-=dungeons[i][1]
            chk[i]=1
            DFS(k,dungeons,chk,cnt+1)
            chk[i]=0
            k+=dungeons[i][1]
    
    