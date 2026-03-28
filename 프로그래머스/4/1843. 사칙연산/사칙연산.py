INF = 1e9

def solution(arr):
    numbers=[int(arr[i]) for i in range(0,len(arr),2)]
    operators=[arr[i] for i in range(1,len(arr)-1,2)]
    
    n=len(numbers)
    
    max_dp=[[-INF]*n for _ in range(n)] 
    min_dp=[[INF]*n for _ in range(n)]
    
    for i in range(n):
        max_dp[i][i]=min_dp[i][i]=numbers[i]
    
    for size in range(1,n):
        for i in range(n-size):
            j=i+size
            for k in range(i,j):
                if operators[k]=="+":
                    max_dp[i][j]=max(max_dp[i][j],max_dp[i][k]+max_dp[k+1][j])
                    min_dp[i][j]=min(min_dp[i][j],min_dp[i][k]+min_dp[k+1][j])
                elif operators[k]=="-":
                    max_dp[i][j]=max(max_dp[i][j],max_dp[i][k]-min_dp[k+1][j])
                    min_dp[i][j]=min(min_dp[i][j],min_dp[i][k]-max_dp[k+1][j])
                    
    
    return max_dp[0][n-1]