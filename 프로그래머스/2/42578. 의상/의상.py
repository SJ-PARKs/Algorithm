def solution(clothes):
    clothe=dict()
    for c in clothes:
        if c[1] not in clothe:
            clothe[c[1]]=0
        clothe[c[1]]+=1

    answer = 1
    for i in clothe.values():
        answer*=i+1
    answer-=1
    return answer