n,m = map(int,input().split())

tree=[[] for _ in range(n+1)]

for _ in range(n-1):
	a,b,c=map(int,input().split())
	tree[a].append((b,c))
	tree[b].append((a,c))
	
def DFS(x,goal,chk,hap):
	if chk[x]==1:
		return None
	if x==goal:
		return hap
	chk[x]=1
	for i in range(len(tree[x])):
		res = DFS(tree[x][i][0], goal, chk, hap + tree[x][i][1])
		if res is not None:
			return res
	chk[x]=0
	
for _ in range(m):
	a,b=map(int,input().split())
	chk=[0 for _ in range(n+1)]
	print(DFS(a,b,chk,0))