from collections import deque

a,b=map(int,input().split())

queue=deque()
queue.append((a,1))
count=0

while queue:
    x, count = queue.popleft()
    if x == b:
        print(count)
        break

    if x > b:
        continue  
		
    queue.append((x * 2, count + 1))
    queue.append((x * 10 + 1, count + 1))
else:
    print(-1)  