def roundUp(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n=int(input())
arr=[]
for i in range(n):
	arr.append(int(input()))
arr=sorted(arr)
m=roundUp(n*0.15)
arr1=arr[m:n-m]
if n==0: 
	print(0)
else:
	print(roundUp(sum(arr1)/(n-2*m)))