def solution(numbers, target):
    answer = 0
    global count
    count=0
    DFS(numbers,0,target,0)
    return count

def DFS(numbers,x,target,hap):
    global count
    if x==len(numbers):
        if hap==target:
            count+=1
        return 
    a=hap+numbers[x]
    b=hap-numbers[x]
    DFS(numbers,x+1,target,a)
    DFS(numbers,x+1,target,b)    