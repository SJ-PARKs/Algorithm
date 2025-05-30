import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville)==0:
            return -1
        x=heapq.heappop(scoville)
        if x >= K:
            return answer
        else:
            if len(scoville)==0:
                return -1
            y=heapq.heappop(scoville)
            heapq.heappush(scoville,x+2*y)
            answer+=1