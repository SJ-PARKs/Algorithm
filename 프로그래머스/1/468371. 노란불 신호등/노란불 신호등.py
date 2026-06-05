def solution(signals):
    answer = 0
    n=len(signals)
    maxTime=1
    for i in range(n):
        c=signals[i][0]+signals[i][1]+signals[i][2]
        maxTime=lcm(maxTime,c)
        
    for t in range(1,maxTime+1):
        isAllYellow=True
        for i in range(n):
            g=signals[i][0]
            y=signals[i][1]
            r=signals[i][2]
            c=g+y+r
        
            remain=(t-1)%c
    
            if (g<=remain and remain<g+y) is False:
                isAllYellow=False
                break
    
        if isAllYellow:
            return t
    
    return -1
    
def lcm(a,b):
    return a//gcd(a,b)*b

def gcd(a,b):
    while b>0:
        r=a%b
        a=b
        b=r
    return a