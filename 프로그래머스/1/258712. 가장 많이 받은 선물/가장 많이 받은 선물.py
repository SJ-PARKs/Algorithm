

def solution(friends, gifts):
    total=len(friends)
    friends_number=[[0,0] for _ in range(total)]
    friends_array=[[0]*total for _ in range(total)]

    for i in range(len(gifts)):
        a,b=gifts[i].split()
        a1=friends.index(a)
        b1=friends.index(b)
        friends_number[a1][0]+=1
        friends_number[b1][1]+=1
    
        friends_array[a1][b1]+=1
    
    answer=0

    for i in range(total):
        tmp=0
        for j in range(total):
            if i==j:
                continue
            if friends_array[i][j]>friends_array[j][i]:
                tmp+=1
                continue
            if friends_array[i][j]==friends_array[j][i]:
                if friends_number[i][0]-friends_number[i][1]>friends_number[j][0]-friends_number[j][1]:
                    tmp+=1
                    continue
        answer=max(answer,tmp)
        
    return answer