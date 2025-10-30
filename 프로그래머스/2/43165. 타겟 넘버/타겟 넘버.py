def solution(numbers, target):
    global answer
    answer = 0
    DFS(numbers,0,target,0,len(numbers))
    return answer

def DFS(numbers,hap,target,cur,end):
    global answer
    if cur==end:
        if hap==target:
            answer+=1
        return
    
    DFS(numbers,hap+numbers[cur],target,cur+1,end)
    DFS(numbers,hap-numbers[cur],target,cur+1,end)