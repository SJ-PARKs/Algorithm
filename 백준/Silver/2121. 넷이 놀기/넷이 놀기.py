n=int(input())
a,b=map(int,input().split())

dot=[]
dot_set=set()
for i in range(n):
	x,y=map(int,input().split())
	dot.append((x,y))
	dot_set.add((x,y))
answer=0
for i in range(len(dot)):
	flag=True
	if (dot[i][0]+a,dot[i][1]) in dot_set and (dot[i][0],dot[i][1]+b) in dot_set and (dot[i][0]+a,dot[i][1]+b) in dot_set:
		answer+=1
	
print(answer)
		
		
		
		
	