from itertools import permutations

def solution(numbers):
    answer = 0
    arr=[]
    num_arr=set()
    for i in range(len(numbers)):
        arr.append(numbers[i])
    
    for i in range(1,len(numbers)+1):
        temp_arr=list(permutations(arr,i))
        for j in range(len(temp_arr)):
            temp_num=int("".join(temp_arr[j]))
            num_arr.add(temp_num)
            
    num_arr=list(num_arr)
    print(num_arr)
    for i in range(len(num_arr)):
        if is_prime(num_arr[i]):
                answer+=1
    return answer

def is_prime(num):
    if num==0 or num==1:
        return False
    i=2
    flag=True
    while True:
        if i*i>num:
            break
        if num%i==0:
            flag=False
            break
        else:
            i+=1
            
    return flag