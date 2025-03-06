def solution(tickets):
    tickets.sort(key=lambda x: x[1])  # 도착지를 기준으로 정렬
    chk = [0] * len(tickets)  # 방문 여부 체크 배열
    places = ["ICN"]  # 경로 저장 리스트

    global answer
    answer = []

    for i in range(len(tickets)):  # ICN에서 출발하는 첫 번째 경로 찾기
        if tickets[i][0] == "ICN":
            chk[i] = 1
            DFS(i, tickets, chk, places, 1)
            if answer:  # 경로를 찾았다면 더 이상 실행하지 않음
                return answer
            chk[i] = 0  # 백트래킹

    return answer  # 혹시라도 경로가 없는 경우 빈 리스트 반환

def DFS(x, tickets, chk, places, cnt):
    global answer

    if answer:  # 이미 정답이 있으면 더 이상 탐색하지 않음
        return

    if cnt == len(tickets):
        places.append(tickets[x][1])
        answer = places[:]  # 정답을 저장
        return

    for i in range(len(tickets)):
        if chk[i] == 0 and tickets[x][1] == tickets[i][0]:
            chk[i] = 1
            places.append(tickets[x][1])
            DFS(i, tickets, chk, places, cnt + 1)
            if answer:  
                return
            places.pop()  
            chk[i] = 0  
