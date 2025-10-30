from itertools import permutations

def solution(k, dungeons):
    answer = -1
    arr=list(permutations(dungeons))
    maximum=0
    for i in range(len(arr)):
        num=0
        start=k
        for j in range(len(arr[i])):
            if start>=arr[i][j][0]:
                start-=arr[i][j][1]
                num+=1
        if num>maximum:
            maximum=num
    answer=maximum
    return answer