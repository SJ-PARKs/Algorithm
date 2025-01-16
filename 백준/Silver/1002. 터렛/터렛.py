import math

n=int(input())

for _ in range(n):
	arr=list(map(int,input().split()))
	if arr[0]==arr[3] and arr[1]==arr[4] and arr[2]==arr[5]:
		print(-1)
	else:
		distance=math.sqrt((arr[3]-arr[0])*(arr[3]-arr[0])+(arr[4]-arr[1])*(arr[4]-arr[1]))
		seq=[]
		seq.append(distance)
		seq.append(arr[2])
		seq.append(arr[5])
		seq=sorted(seq)

		if seq[0]+seq[1]==seq[2]:
			print(1)
		elif seq[0]+seq[1]>seq[2]:
			print(2)
		else:
			print(0)