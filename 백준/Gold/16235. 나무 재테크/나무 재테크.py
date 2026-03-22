import sys
from collections import deque
input = sys.stdin.readline # 입력 속도 최적화 (필수)

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
nutrients = [[5] * n for _ in range(n)]

# 핵심: 1차원 리스트 대신, 각 칸마다 deque를 가지는 2차원 배열 사용
trees = [[deque() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(k):
    # 봄 & 여름
    for i in range(n):
        for j in range(n):
            if trees[i][j]: # 해당 칸에 나무가 있을 때만 진행
                survived = deque()
                dead_nutrients = 0
                
                # 어린 나무(앞쪽)부터 양분 섭취
                for age in trees[i][j]:
                    if nutrients[i][j] >= age:
                        nutrients[i][j] -= age
                        survived.append(age + 1)
                    else:
                        dead_nutrients += age // 2 # 죽은 나무는 바로 양분으로 계산
                
                # 살아남은 나무들로 갱신하고 양분 추가
                trees[i][j] = survived
                nutrients[i][j] += dead_nutrients

    # 가을
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                for age in trees[i][j]:
                    if age % 5 == 0:
                        for d in range(8):
                            ni, nj = i + dr[d], j + dc[d]
                            if 0 <= ni < n and 0 <= nj < n:
                                # 새로 태어난 나무는 항상 1살이므로 덱의 맨 앞에 추가 (자동 정렬)
                                trees[ni][nj].appendleft(1)

    # 겨울
    for i in range(n):
        for j in range(n):
            nutrients[i][j] += a[i][j]

# 살아남은 나무 수 세기
ans = 0
for i in range(n):
    for j in range(n):
        ans += len(trees[i][j])

print(ans)