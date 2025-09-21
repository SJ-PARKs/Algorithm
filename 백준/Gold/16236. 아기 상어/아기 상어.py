from collections import deque
import sys

input = sys.stdin.readline

n = int(input().strip())
board = [list(map(int, input().split())) for _ in range(n)]

sx = sy = -1
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            sx, sy = i, j
            board[i][j] = 0  
            break

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(start_x, start_y, size):
    q = deque()
    q.append((start_x, start_y, 0))
    visited = [[False]*n for _ in range(n)]
    visited[start_x][start_y] = True

    candidates = []
    min_dist = None

    while q:
        x, y, d = q.popleft()

        if min_dist is not None and d > min_dist:
            break

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] <= size:
                    visited[nx][ny] = True
                    if 0 < board[nx][ny] < size:
                        candidates.append((d+1, nx, ny))
                        min_dist = d+1  
                    else:
                        q.append((nx, ny, d+1))

    if not candidates:
        return None
    candidates.sort(key=lambda x: (x[0], x[1], x[2]))
    return candidates[0] 

size = 2
eat_cnt = 0
time = 0

while True:
    found = bfs(sx, sy, size)
    if found is None:
        break
    dist, nx, ny = found
    time += dist
    eat_cnt += 1
    board[nx][ny] = 0  
    sx, sy = nx, ny    

    if eat_cnt == size:
        size += 1
        eat_cnt = 0

print(time)
