def solution(participant, completion):
    participant=sorted(participant)
    completion=sorted(completion)
    index=len(completion)
    for i in range(len(completion)):
        if participant[i]!=completion[i]:
            index=i
            break
    return participant[index]
        
    
    