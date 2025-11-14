def solution(n, times):
    answer = 0
    l=0
    r= 1000000000000000001
    mid=0
    while l<=r:
        mid=(l+r)//2
        people=0
        for time in times:
            people+=mid//time

        if people<n:
            l=mid+1
        else:
            r=mid-1
  
    return l