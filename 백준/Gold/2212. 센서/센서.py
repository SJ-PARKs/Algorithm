n=int(input())
k=int(input())
arr=list(map(int,input().split()))
arr=list(set(arr))
arr=sorted(arr)
distance=[]
for i in range(1,len(arr)):
	distance.append(arr[i]-arr[i-1])
	
distance=sorted(distance)
answer=0
for i in range(len(distance)-(k-1)):
	answer+=distance[i]


print(answer)