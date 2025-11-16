n, c = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

def can_place(d):
    count = 1        
    last = arr[0]
    for i in range(1, n):
        if arr[i] - last >= d:
            count += 1
            last = arr[i]
    return count >= c

l = 1
r = arr[-1] - arr[0]
answer = 0

while l <= r:
    mid = (l + r) // 2
    if can_place(mid):
        answer = mid
        l = mid + 1
    else:
        r = mid - 1

print(answer)