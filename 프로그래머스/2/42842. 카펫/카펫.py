def solution(brown, yellow):
    answer = []
    hap=brown+yellow
    for i in range(1,brown//2):
        a=i
        b=brown//2-i
        if (a-1)*(b-1)==yellow:
            answer.append(b+1)
            answer.append(a+1)
            break
    return answer