n=int(input())
arr=[]
for i in range(n):
	arr.append(int(input()))
maximum1=0
answer1=0
maximum2=0
answer2=0
for i in range(n):
	if arr[i]>maximum1:
		answer1+=1
		maximum1=arr[i]
		
for i in range(n-1,-1,-1):
	if arr[i]>maximum2:
		answer2+=1
		maximum2=arr[i]
		
print(answer1)
print(answer2)