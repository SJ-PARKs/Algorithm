import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 1. 마주 보는 면 중 작은 값들 미리 계산 (A-F, B-E, C-D)
s = []
s.append(min(arr[0], arr[5]))
s.append(min(arr[1], arr[4]))
s.append(min(arr[2], arr[3]))
s.sort()

# 2. N=1일 때 처리
if n == 1:
    arr.sort()
    # 가장 큰 면 하나를 바닥에 두고 나머지 5면 합
    print(sum(arr) - arr[-1])

# 3. N >= 2일 때 처리 (일반화된 공식)
else:
    # 3면이 보이는 주사위 (꼭짓점): 항상 4개
    n3 = 4
    
    # 2면이 보이는 주사위 (모서리): 8N - 12개
    n2 = 8 * n - 12
    
    # 1면이 보이는 주사위 (면 내부): 5N^2 - 16N + 12개
    n1 = 5 * n**2 - 16 * n + 12
    
    # s[0]: 제일 작은 수 (1면 노출용)
    # s[0]+s[1]: 두 번째로 작은 조합 (2면 노출용)
    # s[0]+s[1]+s[2]: 세 면 합 (3면 노출용)
    answer = 0
    answer += n1 * s[0]
    answer += n2 * (s[0] + s[1])
    answer += n3 * (s[0] + s[1] + s[2])
    
    print(answer)