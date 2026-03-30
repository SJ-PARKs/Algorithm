def solution(distance, rocks, n):
    answer = 0
    left,right=0,distance
    rocks.sort()
    while left<=right:
        mid=(left+right)//2
        if check(mid,rocks,distance)>n:
            right=mid-1
        else:
            answer=mid
            left=mid+1
            
            
        
    return answer

def check(mid,rocks,distance):
    before=0
    count=0
    for i in range(len(rocks)):
        if rocks[i]-before<mid:
            count+=1
            continue
        before=rocks[i]
    
    if distance-before<mid:
        count+=1
    
    return count
        
    
        
            
    
    