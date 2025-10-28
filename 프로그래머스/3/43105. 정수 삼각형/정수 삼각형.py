def solution(triangle):
    answer = 0
    dp=[[] for _ in range(len(triangle))]
    for i in range(len(triangle)):
        for j in range(i+1):
            dp[i].append(0)

    dp[0][0]=triangle[0][0]        
    for i in range(1,len(triangle)):
        dp[i][0]=dp[i-1][0]+triangle[i][0]

    for i in range(1,len(triangle)):
        dp[i][i]+=dp[i-1][i-1]+triangle[i][i]
    
    for i in range(2,len(triangle)):
        for j in range(1,i):
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
    
    answer=max(dp[-1])
    return answer