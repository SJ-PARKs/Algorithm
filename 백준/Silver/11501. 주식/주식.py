t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    maximum = 0
    answer = 0
    
    for i in range(n - 1, -1, -1):
        if arr[i] > maximum:
            maximum = arr[i]
        else:
            answer += (maximum - arr[i])
    
    print(answer)
