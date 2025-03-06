def solution(sizes):
    answer = 0
    
    arr1=[]
    arr2=[]
    for i in range(len(sizes)):
        arr1.append(max(sizes[i][0],sizes[i][1]))
        arr2.append(min(sizes[i][0],sizes[i][1]))
    answer=max(arr1)*max(arr2)
    return answer