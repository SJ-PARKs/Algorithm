from sys import stdin
input = stdin.readline

def bf():
      for i in range(n):
            for j in range(len(edges)):
                  cur, next, cost = edges[j]
                  if dist[next] > dist[cur] + cost:
                        dist[next] = dist[cur] + cost
                        if i == n - 1:
                              return True
      return False
                        
TC = int(input())

for _ in range(TC):
      n, m, w = map(int, input().split())
      edges = []
      dist = [1e9] * (n + 1)
      for i in range(m + w):
            s, e, t = map(int, input().split())
            if i >= m:
                  t = -t
            else:
                  edges.append((e, s, t))
            edges.append((s, e, t))
      if bf():
            print("YES")
      else:
            print("NO")


# tc=int(input())

# for _ in range(tc):
# 	n,m,w=map(int,input().split())
# 	edge=[]
# 	for _ in range(m):
# 		s,e,t=map(int,input().split())
# 		edge.append((s,e,t))
# 		edge.append((e,s,t))
# 	for _ in range(w):
# 		s,e,t=map(int,input().split())
# 		edge.append((s,e,-t))
	
# 	dist=[float("inf")]*(n+1)
# 	flag=0
# 	for k in range(1,n+1):
# 		dist[k]=0
# 		for i in range(1,n):
# 			for j in range(len(edge)):
# 				u=edge[j][0]
# 				v=edge[j][1]
# 				weight=edge[j][2]
# 				if dist[u]!=float("inf") and dist[u]+weight<dist[v]:
# 					dist[v]=dist[u]+weight
# 		for j in range(1,n+1):
# 			if dist[j]<0:
# 				flag=1
# 				break
# 		if flag==1:
# 			break
# 		for j in range(len(edge)):
# 			u=edge[j][0]
# 			v=edge[j][1]
# 			weight=edge[j][2]
# 			if dist[u] != float and dist[u]+weight<dist[v]:
# 				flag=1
# 				break
# 		if flag==1:
# 			break
# 	if flag==1:
# 		print("YES")
# 	else: 
# 		print("NO")