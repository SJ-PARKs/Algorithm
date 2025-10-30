import heapq

def solution(operations):
    answer = []
    q=[]
    heapq.heapify(q)    
    for i in range(len(operations)):
        command=operations[i].split(" ")[0]
        number=operations[i].split(" ")[1]
        if command=="I":
            heapq.heappush(q,int(number))
        if len(q)==0:
            continue
        if command=="D" and number=="-1":
            heapq.heappop(q)
        if command=="D" and number=="1":
            q=list(map(lambda x:-x,q))
            heapq.heapify(q)
            heapq.heappop(q)
            q=list(map(lambda x:-x,q))
            heapq.heapify(q)
        
        
    if len(q)==0:
        return [0,0]
    answer.append(max(q))
    answer.append(min(q))
    
    return answer