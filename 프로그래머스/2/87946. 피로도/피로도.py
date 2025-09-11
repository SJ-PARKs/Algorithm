answer =-1
def solution(k, dungeons):
    chk=[0 for _ in range(len(dungeons))]
    for i in range(len(dungeons)):
        if dungeons[i][0]<=k and k-dungeons[i][1]>=0:
            DFS(i,1,k-dungeons[i][1],chk,dungeons)
    return answer


def DFS(x,count,health,chk,dungeons):
    global answer
    if count>answer:
        answer=count
    chk[x]=1
    for i in range(len(dungeons)):
        if chk[i]==1:
            continue
        if health-dungeons[i][1]>=0 and dungeons[i][0]<=health:
            DFS(i,count+1,health-dungeons[i][1],chk,dungeons)
    chk[x]=0
        