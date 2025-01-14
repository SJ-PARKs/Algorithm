t = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(x, y):
    if farm[x][y] == 0:
        return
    farm[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if farm[nx][ny] == 1:
                DFS(nx, ny)

for _ in range(t):
    M, N, K = map(int, input().split())  
    farm = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1  

    count = 0
    for x in range(N):
        for y in range(M):
            if farm[x][y] == 1:
                count += 1
                DFS(x, y)

    print(count)
