from collections import deque
import itertools

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue=[0] * bridge_length
    truck_weights=deque(truck_weights)
    hap=0
    while len(truck_weights)!=0:
        hap-=queue[0]
        queue=queue[1:]
        queue.append(0)
        if hap+truck_weights[0]<=weight:
            x=truck_weights.popleft()
            queue[-1]=x
            hap+=x
        answer+=1
    check=0
    for i in range(bridge_length-1,-1,-1):
        if queue[i]!=0:
            check=i
            break
    answer+=check
    return answer+1
    