import heapq

n=int(input())
arr=[]
for i in range(n):
    s,e=map(int,input().split())
    arr.append((s,e))

arr.sort(key=lambda x:x[1])
arr.sort(key=lambda x:x[0])
    
answer=0    
heap_arr=[]
heapq.heappush(heap_arr,(arr[0][1],arr[0][0]))
for i in range(1,len(arr)):
    if arr[i][0]>=heap_arr[0][0]:
        heapq.heappop(heap_arr)
        heapq.heappush(heap_arr,(arr[i][1],arr[i][0]))
    else:
        heapq.heappush(heap_arr,(arr[i][1],arr[i][0]))
    answer=max(answer,len(heap_arr))

print(answer)