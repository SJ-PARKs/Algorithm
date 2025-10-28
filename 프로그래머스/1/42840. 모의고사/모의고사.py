def solution(answers):
    answer = []
    count1=0
    count2=0
    count3=0
    
    choose1=[1,2,3,4,5]*2000
    choose2=[2,1,2,3,2,4,2,5]*1250
    choose3=[3,3,1,1,2,2,4,4,5,5]*1000
    
    for i in range(len(answers)):
        if answers[i]==choose1[i]:
            count1+=1
        if answers[i]==choose2[i]:
            count2+=1
        if answers[i]==choose3[i]:
            count3+=1

    maximum=max(count1,count2,count3)
    if count1==maximum:
        answer.append(1)
    if count2==maximum:
        answer.append(2)
    if count3==maximum:
        answer.append(3)
    
    
    return answer