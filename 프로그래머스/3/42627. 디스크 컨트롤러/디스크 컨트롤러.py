import heapq

def solution(jobs):
    disk=[]

    for i in range(len(jobs)):
        disk.append((jobs[i][1],jobs[i][0],i))
    disk=sorted(disk)
    
    time=0
    answer=0
    while len(disk)!=0:
        flag=False
        for i in range(len(disk)):
            if time>=disk[i][1]:
                x=disk.pop(i)
                flag=True
                break
        if flag==True:
            answer+=time-x[1]+x[0]
            time+=x[0]
        else:
            time = min(disk, key=lambda x: x[1])[1]

    return answer//len(jobs)