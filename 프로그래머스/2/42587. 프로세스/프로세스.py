from collections import deque

def solution(priorities, location):
    order=sorted(priorities)
    hq=deque()
    for i in range(len(priorities)):
        hq.append((priorities[i],i))
    
    answer = 1

    while True:
        x=hq.popleft()
        if x[0]==order[-1]:
            order.pop()
            answer+=1
            if x[1]==location:
                break
        else:
            hq.append(x)
        
    return answer-1