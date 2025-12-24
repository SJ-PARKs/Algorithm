n = int(input())
dp = [1] * 10

for _ in range(1, n):
    new_dp = [0] * 10
    for j in range(10):
        for k in range(j + 1):
            new_dp[j] += dp[k]
        new_dp[j] %= 10007
    dp = new_dp

print(sum(dp) % 10007)
