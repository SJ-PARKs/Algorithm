def solution(n, tops):
    answer = 0
    dp1=[0 for _ in range(n)]
    dp2=[0 for _ in range(n)]
    dp1[0]=1
    if tops[0]==0:
        dp2[0]=2
    elif tops[0]==1:
        dp2[0]=3
    for i in range(1,n):
        dp1[i]=(dp1[i-1]+dp2[i-1])%10007
        dp2[i]=(dp1[i-1]*(1+tops[i])+dp2[i-1]*(2+tops[i]))%10007
    
    answer=(dp1[n-1]+dp2[n-1])%10007
    return answer