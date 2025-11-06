t, w = map(int, input().split())

arr = []
for i in range(t):
    arr.append(int(input()))

dp = [[[0 for _ in range(w+1)] for _ in range(2)] for _ in range(t)]

if arr[0] == 1:
    dp[0][0][0] = 1
if arr[0] == 2:
    if w >= 1:
        dp[0][1][1] = 1

for i in range(1, t):
    for j in range(0, w+1):
        if arr[i] == 1:
            if j == 0:
                dp[i][0][j] = dp[i-1][0][j] + 1
                dp[i][1][j] = dp[i-1][1][j]
            else:
                dp[i][0][j] = max(dp[i-1][0][j], dp[i-1][1][j-1]) + 1
                dp[i][1][j] = max(dp[i-1][0][j-1], dp[i-1][1][j])
        if arr[i] == 2:
            if j == 0:
                dp[i][0][j] = dp[i-1][0][j]
                dp[i][1][j] = dp[i-1][1][j] + 1
            else:
                dp[i][0][j] = max(dp[i-1][0][j], dp[i-1][1][j-1])
                dp[i][1][j] = max(dp[i-1][1][j], dp[i-1][0][j-1]) + 1

res = -1
for i in range(w+1):
    res = max(max(res, dp[t-1][0][i]), dp[t-1][1][i])

print(res)
