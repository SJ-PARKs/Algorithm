import heapq

n = int(input())
gas_station = [list(map(int, input().split())) for _ in range(n)]
l, p = map(int, input().split())

gas_station.sort()  # 거리순 정렬

q = []
answer = 0

for dist, fuel in gas_station:
    # 현재 연료로 이 주유소까지 못 가면,
    # 지금까지 지나온 주유소 중 가장 많이 주는 곳부터 주유
    while p < dist:
        if not q:
            print(-1)
            exit()
        p += -heapq.heappop(q)
        answer += 1

    # 여기까지 왔으면 이 주유소는 도달 가능
    heapq.heappush(q, -fuel)

# 이제 마을까지 가기
while p < l:
    if not q:
        print(-1)
        exit()
    p += -heapq.heappop(q)
    answer += 1

print(answer)