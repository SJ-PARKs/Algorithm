while True:
	n,k=map(int,input().split())
	if n==0 and k==0:
		break
	node=list(map(int,input().split()))
	parent_idx,before,ans=-1,0,0
	parent=[0 for _ in range(1000001)]
	for i in range(len(node)):
		data=node[i]
		if i==0: # 첫입력이면 루트노드임.
			before=data
			parent[data]=-1 # 자기가 자신의 부모임.
		else:
			if before+1==data: # 같은집합.
				parent[data]=node[parent_idx]
				before=data
			else:
				before=data
				parent_idx+=1
				parent[data]=node[parent_idx]
	# parent[data]에는 data의 부모가 있습니다.우리는 k의 사촌 수를 찾아야 합니다.
	if k==node[0]:
		ans=0
	else:
		for i in range(len(node)):
			#  k와 부모가 다르고, k의 부모들과 부모가 같아야합니다.
			if (parent[parent[node[i]]]==parent[parent[k]]) and (parent[node[i]] != parent[k]):
				ans+=1
				
	print(ans)
			