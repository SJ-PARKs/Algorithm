def solution(n, times):
    answer = 0
    l=0
    r=max(times)*n
    while l<=r:
        mid=(l+r)//2
        people=0
        for time in times:
            people+=(mid//time)
        if people>=n:
            answer=mid
            r=mid-1
        else:
            l=mid+1
    return answer