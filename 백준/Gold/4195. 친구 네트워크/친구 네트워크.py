t=int(input())

def union(a,b):
    aa=find(a)
    bb=find(b)
    if aa!=bb:
        unf[aa]=bb
        size[bb]+=size[aa]

def find(a):
    if a==unf[a]:
        return a
    else:
        unf[a]=find(unf[a])
        return unf[a]

for _ in range(t):
    unf=dict()
    size=dict()
    n=int(input())
    for i in range(n):
        a,b=input().split()
        if a not in unf:
            unf[a]=a
            size[a]=1
        if b not in unf:
            unf[b]=b
            size[b]=1
        union(a,b)
        aa=find(a)
        print(size[aa])

