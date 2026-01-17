n=int(input())
time=[]
for _ in range(0,n):
	a,b=map(int,input().split())
	time.append((a,b))

time= sorted(time, key=lambda x:x[0])
time= sorted(time, key=lambda x:x[1])

count=0
end_time=0
for i in range(n):
	if end_time<=time[i][0]:
		end_time=time[i][1]
		count+=1
		
print(count)