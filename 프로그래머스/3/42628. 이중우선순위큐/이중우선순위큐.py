import heapq

def solution(operations):
    answer = []
    heap=[]
    for i in range(len(operations)):
        operation,num=operations[i].split(" ")
        if operation=="I":
            heapq.heappush(heap,int(num))
        if operation=="D" and num=="-1":
            if len(heap)==0:
                continue
            heapq.heappop(heap)
        if operation=="D" and num=="1":
            if len(heap)==0:
                continue
            heap=sorted(heap)
            heap.pop(-1)
            heapq.heapify(heap)
    
    if len(heap)==0:
        answer.append(0)
        answer.append(0)
    if len(heap)==1:
        answer.append(heap[0])
        answer.append(heap[0])
    if len(heap)>=2:
        answer.append(max(heap))
        answer.append(min(heap))
    return answer