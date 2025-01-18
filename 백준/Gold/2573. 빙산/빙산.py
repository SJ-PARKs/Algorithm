import sys
from collections import deque

sys.setrecursionlimit(10**4)

n, m = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(n)]

glacier = [(i, j) for i in range(n) for j in range(m) if sea[i][j] > 0]

year = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and sea[nx][ny] > 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

while glacier:
    year += 1
    melt = []  

    for x, y in glacier:
        melt_count = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and sea[nx][ny] == 0:
                melt_count += 1
        if melt_count > 0:
            melt.append((x, y, melt_count))

    for x, y, melt_count in melt:
        sea[x][y] = max(0, sea[x][y] - melt_count)

    glacier = [(x, y) for x, y in glacier if sea[x][y] > 0]

    if not glacier:
        print(0)
        sys.exit(0)

    visited = [[False] * m for _ in range(n)]
    cnt = 0

    for x, y in glacier:
        if not visited[x][y]:
            bfs(x, y, visited)
            cnt += 1

    if cnt >= 2:
        print(year)
        sys.exit(0)
