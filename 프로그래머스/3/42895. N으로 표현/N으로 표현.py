def solution(N, number):
    answer = -1
    dp=[set() for _ in range(10)]

    for i in range(1,10):
        dp[i].add(int(str(N)*i))
    
    for count in range(2,10):
        for left_count in range(1,count):
            right_count=count-left_count
            for i in dp[left_count]:
                for j in dp[right_count]:
                    dp[count].add(i+j)
                    dp[count].add(i-j)
                    dp[count].add(i*j)
                    if j!=0:
                        dp[count].add(i//j)
    
    for i in range(1,10):
        if number in dp[i]:
            answer=i
            break
            
    return answer