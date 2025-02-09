def solution(array, commands):
    answer = []
    for arr in commands:
        tmp=array[arr[0]-1:arr[1]]
        tmp=sorted(tmp)
        answer.append(tmp[arr[2]-1])
    
    return answer