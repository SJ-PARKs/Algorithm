def solution(distance, rocks, n):
    answer = 0
    num=len(rocks)
    
    rocks.sort()
    
    l,r=0,1000000000
    
    while l<=r:
        mid=(l+r)//2
        remove_num=remove_rocks(rocks,mid,distance)
        if remove_num<=n:
            answer=mid
            l=mid+1
        else:
            r=mid-1
    
    return answer

def remove_rocks(rocks,shortest_len,distance):
    before=0
    count=0
    end=distance
    for i in range(len(rocks)):
        if shortest_len>rocks[i]-before:
            count+=1
        else:
            before=rocks[i]
    if end-before<shortest_len: count+=1
    
    return count