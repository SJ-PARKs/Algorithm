s=input()
t=input()

def DFS(ab):
	global flag
	if len(ab)<len(s):
		return
	if ab==s:
		flag=1
		return
	if ab[-1]=='A':
		DFS(ab[:-1])
	if ab[0]=='B':
		DFS(ab[1:][::-1])
		
flag=0	
DFS(t)

if flag==1:
	print(1)
else: 
	print(0)