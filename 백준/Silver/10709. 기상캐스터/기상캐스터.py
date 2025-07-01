import sys

def find(y,x):
  maps[y][x] = 0
  stack = []
  stack.append(x)
  while stack:
    dx = stack.pop()
    if dx + 1 < W and sky[y][dx+1] == '.':
      maps[y][dx+1] = maps[y][dx]+1
      stack.append(dx+1)
    elif dx + 1 < W and sky[y][dx+1] == 'c':
      maps[y][dx+1] = 0
      stack.append(dx+1)

input = sys.stdin.readline
H, W = map(int,input().split())

sky = [list(input()) for _ in range(H)]
maps = [[-1]*W for _ in range(H)]

for i in range(H):
  for j in range(W):
    if sky[i][j] == 'c':
      find(i,j)
  print(' '.join(map(str,maps[i])))