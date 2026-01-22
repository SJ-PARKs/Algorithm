s=input()
t=input()

while len(t)>len(s):
	if t[-1]=="A":
		t=t[0:-1]
	else:
		t=t[0:-1]
		temp_t=""
		for i in range(len(t)-1,-1,-1):
			temp_t+=t[i]
		t=temp_t
	
if s==t:
	print(1)
else:
	print(0)
	