def solution(land):
    answer = 0

    dp=[[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    for i in range(len(land[0])):
        dp[0][i]=land[0][i]
    
    for i in range(1,len(land)):
        for j in range(0,4):
            maximum=0
            for k in range(0,4):
                if k==j:
                    continue
                if dp[i-1][k]>maximum:
                    maximum=dp[i-1][k]
                    
            dp[i][j]=maximum+land[i][j]
                
    
    
    return max(dp[len(land)-1])