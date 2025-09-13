n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def can_pass(line, l):
    n = len(line)
    used = [False] * n
    j = 0
    while j < n - 1:
        if line[j] == line[j + 1]:
            j += 1
            continue

        # 내리막 (현재 > 다음): 다음 l칸 [j+1 .. j+l]
        if line[j] - line[j + 1] == 1:
            if j + l >= n:
                return False
            for k in range(1, l + 1):  # j+1..j+l
                if line[j + k] != line[j + 1] or used[j + k]:
                    return False
            for k in range(1, l + 1):
                used[j + k] = True
            j += l   # 경사로 구간을 한 번에 건너뜀
            continue

        # 오르막 (현재 < 다음): 직전 l칸 [j .. j-l+1]  ← j 포함!
        if line[j + 1] - line[j] == 1:
            if j - (l - 1) < 0:   # j-(l-1) == j-l+1 가 0 이상이어야 함
                return False
            for k in range(l):    # k=0..l-1 → j, j-1, ..., j-l+1
                idx = j - k
                if line[idx] != line[j] or used[idx]:
                    return False
            for k in range(l):
                used[j - k] = True
            j += 1
            continue

        # 높이 차가 2 이상이면 실패
        return False

    return True

answer = 0

# 가로
for i in range(n):
    if can_pass(board[i], l):
        answer += 1

# 세로
for c in range(n):
    col = [board[r][c] for r in range(n)]
    if can_pass(col, l):
        answer += 1

print(answer)
