while(True):
	n,k=map(int,input().split())
	if n==0 and k==0:
		break
	if n==1:
		arr=list(map(int,input().split()))
		print(0)
		continue

		
	arr=list(map(int,input().split()))

	idx=0
	cut=[]
	parent=[]

	cut.append([arr[0]])
	parent.append(0)
	temp=[]
	for i in range(1,len(arr)-1):
		if arr[i]+1==arr[i+1]:
			temp.append(arr[i])
		else:
			temp.append(arr[i])
			cut.append(temp)
			temp=[]
			parent.append(arr[idx])
			idx+=1
	cut.append(temp)		
	parent.append(arr[idx])
	if arr[-1]==arr[-2]+1:
		cut[-1].append(arr[-1])
	else:
		cut.append([arr[-1]])
		parent.append(arr[idx])

	idx1=0
	idx2=[]

	for i in range(len(cut)):
		if k in cut[i]:
			idx1=parent[i]
			break
	for i in range(len(cut)):
		if idx1 in cut[i]:
			idx2=cut[i]

	answer=0
	for i in range(len(idx2)):
		if idx2[i]==idx1:
			continue
		for j in range(len(parent)):
			if parent[j]==idx2[i]:
				answer+=len(cut[j])

	print(answer)