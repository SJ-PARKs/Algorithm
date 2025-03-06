def solution(begin, target, words):
    global answer
    answer = 0
    chk=[0 for _ in range(len(words))]
    DFS(begin,words,target,chk,0)
    return answer

def DFS(x,words,target,chk,cnt):
    global answer
    if x==target:
        answer=cnt
        return
        
    for i in range(len(words)):
        count=0
        for j in range(len(words[i])):
            if words[i][j]!=x[j]:
                continue
            count+=1
        if count==len(x)-1 and chk[i]==0:
            chk[i]=1
            DFS(words[i],words,target,chk,cnt+1)
            chk[i]=0
    
            
            
            
