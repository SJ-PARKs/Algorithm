n, k = map(int, input().split())
line = [int(input()) for _ in range(n)]

l = 1  
r = max(line)  
answer = 0  

while l <= r:
    mid = (l + r) // 2 
    count = sum(x // mid for x in line)  

    if count < k:  
        r = mid - 1
    else:  
        answer = mid
        l = mid + 1

print(answer)
