N = int(input())
arr = list(map(int, input().split()))
dp = [0] * 1001
ans = 0

for i in range(N):
    here = 0
    for j in range(i):
        if arr[i] > arr[j]:
            here = max(here, dp[j])
    dp[i] = here + 1
    ans = max(ans, dp[i])

print(ans)