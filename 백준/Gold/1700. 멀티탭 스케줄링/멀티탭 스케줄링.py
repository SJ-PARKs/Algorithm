n,k=map(int,input().split())
arr=list(map(int,input().split()))

plug=[0]*n
distance=[float("inf")]*n

answer=0
for i in range(len(arr)):
	for j in range(len(distance)):
		distance[j]-=1
	
	if arr[i] in plug:
		dis=float("inf")
		for j in range(i+1,len(arr)):
			if arr[j]==arr[i]:
				dis=j-i
				break
		idx=plug.index(arr[i])
		distance[idx]=dis
		continue
	
	# 빈 칸 있으면 그냥 꽂기 (언플러그 X)
	if 0 in plug:
		idx = plug.index(0)
	else:
        # 빈 칸 없을 때만 "빼기" 발생
		answer += 1
		# 최대 거리 남은거 찾기
		dis=max(distance)
		idx=distance.index(dis)
	
	# 채우고 거리도 
	plug[idx]=arr[i]
	dis=float("inf")
	for j in range(i+1,len(arr)):
		if arr[j]==arr[i]:
			dis=j-i
			break
	distance[idx]=dis
	
	
	
print(answer)