import heapq
import sys

input = sys.stdin.readline

n=int(input())
q=[]
for i in range(n):
	x=int(input())
	if x==0:
		if len(q)==0:
			print(0)
			
		elif len(q)>0:
			a=heapq.heappop(q)
			print(-a)
	else:
		heapq.heappush(q,-x)
	
		