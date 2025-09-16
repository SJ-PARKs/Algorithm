from collections import deque

s=[]
for i in range(4):
	s.append(deque(list(map(int,input()))))
	
k=int(input())
spin=[]
for i in range(k):
	spin.append(list(map(int,input().split())))

def left(n,d):
	if n<0:
		return
	if s[n][2]!=s[n+1][6]:
		left(n-1,-d)
		s[n].rotate(d)
	
def right(n,d):
	if n>3:
		return
	if s[n][6]!=s[n-1][2]:
		right(n+1,-d)
		s[n].rotate(d)
	
for i in range(k):
	right(spin[i][0],-spin[i][1])
	left(spin[i][0]-2,-spin[i][1])
	s[spin[i][0]-1].rotate(spin[i][1])
	
res =0
if s[0][0]==1:
	res+=1
if s[1][0]==1:
	res+=2
if s[2][0]==1:
	res+=4
if s[3][0]==1:
	res+=8
	
print(res)