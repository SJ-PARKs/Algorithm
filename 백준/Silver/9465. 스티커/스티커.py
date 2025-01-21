k=int(input())
for _ in range(k):
    n=int(input())
    table=[]
    for _ in range(2):
        table.append(list(map(int,input().split())))
        
    dp=[]
    for _ in range(2):
        dp.append([0]*n)

    dp[0][0]=table[0][0]
    dp[1][0]=table[1][0]
	
    if n>=2:
        dp[0][1]=table[0][1]+dp[1][0]
        dp[1][1]=table[1][1]+dp[0][0]
    if n==1:
        print(max(table[0][0],table[1][0]))
    if n==2:
        print(max(table[0][0]+table[1][1],table[1][0]+table[0][1]))
    if n>2:
        for i in range(2,n):    
            dp[0][i]=max(dp[1][i-1],dp[0][i-2],dp[1][i-2])+table[0][i]
            dp[1][i]=max(dp[0][i-1],dp[1][i-2],dp[0][i-2])+table[1][i]
        print(max(dp[0][n-1],dp[1][n-1]))