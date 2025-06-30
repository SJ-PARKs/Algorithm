n=int(input())
arr=list(map(int,input().split()))

arr1=sorted(arr)
answer=[0 for _ in range(len(arr))]
chk=[0 for _ in range(len(arr))]
place=0
for i in range(len(arr1)):
	for j in range(len(arr)):
		if arr[j]==arr1[i] and chk[j]==0:
			answer[j]=place
			chk[j]=1
			place+=1
			break

for i in range(len(answer)):
	print(answer[i], end=' ')
			