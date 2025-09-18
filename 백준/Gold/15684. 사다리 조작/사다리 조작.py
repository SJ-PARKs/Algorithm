n, h, m = map(int, input().split())

ladder = [[0 for _ in range(n-1)] for _ in range(m)]

for i in range(h):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1

def check():
    for i in range(n):
        go = i
        for j in range(m):
            if go < n-1 and ladder[j][go] == 1:
                go += 1
            elif go > 0 and ladder[j][go-1] == 1:
                go -= 1
        if go != i:
            return False
    return True

def can_place(row, col):
    # 현재 위치에 가로막을 놓을 수 있는지 확인
    if ladder[row][col] == 1:
        return False
    if col > 0 and ladder[row][col-1] == 1:
        return False
    if col < n-2 and ladder[row][col+1] == 1:
        return False
    return True

def dfs(row, col, cnt, target):
    if cnt == target:
        return check()
    
    if row >= m:
        return False
    
    # 현재 위치부터 끝까지 놓을 수 있는 최대 가로막 수 계산 (가지치기)
    remaining = 0
    for i in range(row, m):
        for j in range(n-1):
            if can_place(i, j):
                remaining += 1
    
    if remaining < target - cnt:
        return False
    
    # 다음 위치 계산
    next_row, next_col = (row, col + 1) if col + 1 < n - 1 else (row + 1, 0)
    
    # 현재 위치에 가로막을 놓지 않는 경우
    if dfs(next_row, next_col, cnt, target):
        return True
    
    # 현재 위치에 가로막을 놓는 경우
    if can_place(row, col):
        ladder[row][col] = 1
        if dfs(next_row, next_col, cnt + 1, target):
            ladder[row][col] = 0
            return True
        ladder[row][col] = 0
    
    return False

# 초기 상태 확인
if check():
    print(0)
else:
    answer = -1
    # 1개, 2개, 3개 순서로 탐색 (최소값을 찾기 위해)
    for target in range(1, 4):
        if dfs(0, 0, 0, target):
            answer = target
            break
    print(answer)