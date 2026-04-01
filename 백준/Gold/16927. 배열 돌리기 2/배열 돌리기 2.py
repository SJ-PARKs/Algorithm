import sys

# 입력 속도 최적화 (백준 제출용)
input = sys.stdin.readline
n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 총 껍질(테두리)의 개수
layers = min(n, m) // 2

for s in range(layers):
    # 1. 현재 껍질의 둘레 길이 구하기
    # 가로 2개, 세로 2개에서 겹치는 모서리 4개를 뺀 값
    perimeter = 2 * ((n - 2 * s) + (m - 2 * s)) - 4
    
    # 2. 현재 껍질의 '실제 회전 횟수' 계산 (핵심 아이디어!)
    actual_r = r % perimeter
    
    # 회전할 필요가 없으면 다음 껍질로 넘어감
    if actual_r == 0:
        continue
        
    # 3. 현재 껍질을 1차원 리스트로 쭉 펴기
    temp = []
    # 위쪽 (왼쪽 -> 오른쪽)
    for j in range(s, m - s):
        temp.append(board[s][j])
    # 오른쪽 (위 -> 아래)
    for i in range(s + 1, n - s - 1):
        temp.append(board[i][m - 1 - s])
    # 아래쪽 (오른쪽 -> 왼쪽)
    for j in range(m - 1 - s, s - 1, -1):
        temp.append(board[n - 1 - s][j])
    # 왼쪽 (아래 -> 위)
    for i in range(n - s - 2, s, -1):
        temp.append(board[i][s])
        
    # 4. 파이썬 리스트 슬라이싱을 이용해 한 번에 회전시키기
    # actual_r 만큼 원소들이 앞으로 당겨짐 (반시계 방향 회전)
    temp = temp[actual_r:] + temp[:actual_r]
    
    # 5. 회전된 1차원 리스트를 다시 원래 배열 자리에 덮어쓰기
    idx = 0
    # 위쪽
    for j in range(s, m - s):
        board[s][j] = temp[idx]
        idx += 1
    # 오른쪽
    for i in range(s + 1, n - s - 1):
        board[i][m - 1 - s] = temp[idx]
        idx += 1
    # 아래쪽
    for j in range(m - 1 - s, s - 1, -1):
        board[n - 1 - s][j] = temp[idx]
        idx += 1
    # 왼쪽
    for i in range(n - s - 2, s, -1):
        board[i][s] = temp[idx]
        idx += 1

# 정답 출력
for row in board:
    print(*row)