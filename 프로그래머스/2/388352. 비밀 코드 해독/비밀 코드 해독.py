import itertools

def solution(n, q, ans):
    answer = 0
    numbers=[i for i in range(1,n+1)]
    num_set=list(itertools.combinations(numbers,5))
    
    for i in range(len(num_set)):
        flag=True
        for j in range(len(q)):
            count=0
            for k in range(5):
                if q[j][k] in num_set[i]:
                    count+=1
            if count!=ans[j]:
                flag=False
                break
        if flag==True:
            answer+=1
            
    
    return answer