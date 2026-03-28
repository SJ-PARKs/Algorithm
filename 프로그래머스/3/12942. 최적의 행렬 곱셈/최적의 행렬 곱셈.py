INF=1e9

def solution(matrix_sizes):
    answer = 0
    n=len(matrix_sizes)
    dp=[[INF]*n for _ in range(n)]
    for i in range(n):
        dp[i][i]=0
    
    for size in range(1,n):
        for i in range(n-size):
            j=i+size
            for k in range(i,j):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+(matrix_sizes[i][0]*matrix_sizes[k][1]*matrix_sizes[j][1]))
                
    answer=dp[0][n-1]
    return answer