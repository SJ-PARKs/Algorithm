import sys
from collections import deque
input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V+1)]
# 2차원 리스트에 트리 저장(연결 그래프)
for _ in range(V):
    line = list(map(int, input().split()))
    cnt_node = line[0]
    idx = 1
    while line[idx] != -1:
        adj_node, adj_cost = line[idx], line[idx+1]
        tree[cnt_node].append((adj_node, adj_cost))
        idx += 2

def BFS(start):
    q = deque()
    q.append((start, 0))
    visited = [-1]*(V+1)
    visited[start] = 0
    res = [0, 0] # start로부터 가장 먼 거리에 있는 노드와 거리 값
    
    while q:
        cnt_node, cnt_dist = q.popleft()
        
        for adj_node, adj_dist in tree[cnt_node]:
            if visited[adj_node] == -1:
                cal_dist = cnt_dist + adj_dist
                q.append((adj_node, cal_dist))
                visited[adj_node] = cal_dist
                if res[1] < cal_dist:
                    res[0] = adj_node
                    res[1] = cal_dist
        
    return res
    
# 트리 지름 공식 참고
# u-v가 지름이라고 하자. 임의의 점 x에서 가장 먼 거리의 노드 y는
# 반드시 u 또는 v이다. 따라서 y에서 BFS를
# 한번 더 해주면 지름을 구할 수 있다.
point, _ = BFS(1)
print(BFS(point)[1])
