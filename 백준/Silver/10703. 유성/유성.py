r,s=map(int,input().split())

picture=[list(input()) for _ in range(r)]
minimum=99999	
for j in range(s):
	a,b=-1,-1
	for i in range(r):
		if picture[i][j]=='X':
			a=i		
		if picture[i][j]=='#':
			b=i
			break
	if a==-1 or b==-1:
		continue
	if minimum>b-a-1:
		minimum=b-a-1

for j in range(s):
	for i in range(r-1,-1,-1):
		if picture[i][j]=="X":
			picture[i+minimum][j]=picture[i][j]
			picture[i][j]='.'

for i in range(len(picture)):
	for j in range(len(picture[i])):
		print(picture[i][j],end='')
	print()
	
	