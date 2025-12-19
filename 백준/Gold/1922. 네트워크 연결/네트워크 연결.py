n=int(input())
m=int(input())

network=[]
for i in range(m):
    network.append(list(map(int,input().split())))

network=sorted(network,key=lambda x:x[2])

unf=[0]*(n+1)
for i in range(1,n+1):
    unf[i]=i

def union(a,b):
    aa=find(a)
    bb=find(b)
    if aa!=bb:
        unf[aa]=bb
def find(a):
    if a==unf[a]:
        return a
    else:
        unf[a]=find(unf[a])
        return unf[a]
count=0
answer=0
for i in range(len(network)):
    if count==n-1:
        break
    aa=find(network[i][0])
    bb=find(network[i][1])
    if aa==bb:
        continue
    else:
        union(aa,bb)
        answer+=network[i][2]
print(answer)