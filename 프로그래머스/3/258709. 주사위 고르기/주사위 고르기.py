import itertools
import bisect

def solution(dice):
    answer = []
    choiceA=list(itertools.combinations([i for i in range(len(dice))],len(dice)//2))
    choiceB=[]
    for i in range(len(choiceA)):
        tmp=[]
        for j in range(len(dice)):
            if j not in choiceA[i]:
                tmp.append(j)
        choiceB.append(tuple(tmp))

    maximum=0
    for i in range(len(choiceA)):
        productA=[]
        productB=[]
        
        if len(choiceA[0])>=2:
            tmp_productA=list(itertools.product(*(dice[x] for x in choiceA[i])))
            tmp_productB=list(itertools.product(*(dice[x] for x in choiceB[i])))

            for j in range(len(tmp_productA)):
                productA.append(sum(tmp_productA[j]))
                productB.append(sum(tmp_productB[j]))

            productB.sort()
            total=0
            for j in range(len(productA)):
                total+=bisect.bisect_left(productB,productA[j])

            if total>maximum:
                answer=[x+1 for x in choiceA[i]]
                maximum=total

        if len(choiceA[0])==1:
            count=0
            for a in range(6):
                for b in range(6):
                    if dice[0][a]>dice[1][b]:
                        count+=1
            if count>18:
                answer=[1]
            else:
                answer=[2]
                
    return answer