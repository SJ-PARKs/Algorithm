import sys

sys.setrecursionlimit(100000)

n,m=map(int,input().split())
s=[0]*(n+1)
for i in range(1,n+1):
    s[i]=i

def union(a,b):
    aa=find(a)
    bb=find(b)
    if aa!=bb:
        s[aa]=bb

def find(a):
    if a!=s[a]:
        s[a]=find(s[a])
        return s[a]
    else:
        return a
for i in range(m):
    a,b,c=map(int,input().split())
    if a==0:
        union(b,c)
    if a==1:
        bb=find(b)
        cc=find(c)
        if bb==cc:
            print("YES")
        else:
            print("NO")