def solution(progresses, speeds):
    answer = []
    days=[]
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i]==0:
            days.append((100-progresses[i])//speeds[i])
        else:
            days.append((100-progresses[i])//speeds[i]+1)
    
    cnt=1
    stack=[] 
    stack.append(days[0])
    for i in range(1,len(days)):
        if days[i]>stack[-1]:
            answer.append(cnt) 
            stack.append(days[i])
            cnt=1
        else:
            cnt+=1
    answer.append(cnt)
    return answer