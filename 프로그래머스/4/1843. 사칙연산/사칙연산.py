def solution(arr):
    answer = -1
    numbers=[int(arr[i]) for i in range(0,len(arr),2)]
    operators=[arr[i] for i in range(1,len(arr),2)]
    
    max_dp=[[-float('inf') for _ in range(len(numbers))] for _ in range(len(numbers))]
    min_dp=[[float('inf') for _ in range(len(numbers))] for _ in range(len(numbers))]
    
    n=len(numbers)
    
    for i in range(n):
        max_dp[i][i]=numbers[i]
        min_dp[i][i]=numbers[i]

    print(max_dp)
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
                    
    answer=max_dp[0][-1]            
    
    return answer