def solution(emergency):
    answer = []
    emergency_sorted=sorted(emergency,reverse=True)
    print(emergency_sorted)
    for i in range(len(emergency)):
        for j in range(len(emergency)):
            if emergency[i]==emergency_sorted[j]:
                answer.append(j+1)
    return answer