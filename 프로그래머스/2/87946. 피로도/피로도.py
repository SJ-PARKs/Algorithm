maximum=0
def solution(k, dungeons):
    answer = -1
    chk=[0 for _ in range(len(dungeons))]
    DFS(k,dungeons,chk,0)
    answer=maximum
    return answer

def DFS(k,dungeons,chk,times):
    global maximum
    if k>=0:
        if maximum<times:
            maximum=times
    else: 
        return 
    for i in range(len(dungeons)):
        if k>=dungeons[i][0] and chk[i]==0:
            chk[i]=1
            DFS(k-dungeons[i][1],dungeons,chk,times+1)
            chk[i]=0