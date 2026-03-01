n=int(input())
arr=[]
answer=0
for i in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))
    
arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1])

end=0
for i in range(len(arr)):
    if end<=arr[i][0]:
        end=arr[i][1]
        answer+=1
print(answer)