from collections import Counter

n, m, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 평탄화 후보 높이: 0 ~ 256
height_counter = Counter()
for row in board:
    for val in row:
        height_counter[val] += 1

min_h = min(height_counter)
max_h = max(height_counter)

best_time = float('inf')
best_height = -1

for target in range(min_h, max_h + 1):
    remove = 0
    add = 0

    for h, count in height_counter.items():
        diff = h - target
        if diff > 0:
            remove += diff * count
        else:
            add -= diff * count  # diff < 0 → 추가 필요

    if remove + b >= add:
        time = remove * 2 + add * 1
        if time < best_time or (time == best_time and target > best_height):
            best_time = time
            best_height = target

print(best_time, best_height)
