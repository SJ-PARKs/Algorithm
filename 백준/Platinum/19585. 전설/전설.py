c,n=map(int,input().split())
color=set()
name=set()
length=set()

for i in range(c):
	s=input()
	color.add(s)
	length.add(len(s))
	
for i in range(n):
	s=input()
	name.add(s)

q=int(input())
for i in range(q):
	s=input()
	flag=False
	for l in length:
		front=s[:l]
		back=s[l:]
		if front in color and back in name:
			flag=True
			break
	if flag==True:
		print("Yes")
	else:
		print("No")