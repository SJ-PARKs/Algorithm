def solution(jobs):
    n=len(jobs)
    answer = 0
    time=0
    while jobs:
        jobs=sorted(jobs,key=lambda x:x[0])
        jobs=sorted(jobs,key=lambda x:x[1])
        flag=False
        for i in range(len(jobs)):
            if time>=jobs[i][0]:
                time+=jobs[i][1]
                answer+=time-jobs[i][0]
                jobs.pop(i)
                flag=True
                break
        if flag==False:
             time = min(j[0] for j in jobs)
    return answer//n