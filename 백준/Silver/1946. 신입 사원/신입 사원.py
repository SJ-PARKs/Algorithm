t=int(input())
for _ in range(t):
	n=int(input())
	arr=[]
	for i in range(n): 
		a,b=map(int,input().split())
		arr.append((a,b))
	arr=sorted(arr)
	minimum=arr[0][1]
	answer=1
	for i in range(1,n):
		if arr[i][1]<minimum:
			answer+=1
			minimum=arr[i][1]
	print(answer)