def solution(n, times):
    l=1
    r=max(times)*n
    
    while l<=r:
        people=0
        mid=(l+r)//2
        for time in times:
            people+=mid//time
            
            if people>=n:
                break
        if people>=n:
            answer=mid
            r=mid-1
        else:
            l=mid+1
    return answer