def solution(clothes):
    answer = 1
    cnt=dict()
    for clothe in clothes:
        if clothe[1] not in cnt:
            cnt[clothe[1]]=1
        else:
            cnt[clothe[1]]+=1
        
        
    for value in cnt.values():
        answer*=(value+1)
    
    return answer-1