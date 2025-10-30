import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0]<K:
        if len(scoville)<=1:
            return -1
        x1=heapq.heappop(scoville)
        x2=heapq.heappop(scoville)
        
        heapq.heappush(scoville,x1+x2*2)
        answer+=1
        
    return answer