def solution(brown, yellow):
    answer = []
    hap=brown+yellow
    for i in range(1,hap//2+1):
        if hap%i==0:
            if (i-2)*(hap//i-2)==yellow:
                answer.append(max(i,hap//i))
                answer.append(min(i,hap//i))  
                break
    return answer