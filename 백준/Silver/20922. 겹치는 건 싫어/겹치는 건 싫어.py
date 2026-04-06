class Solution:
	def __init__(self,n,k,arr):
		self.n=n
		self.k=k
		self.arr=arr
		self.count_num=dict()
		self.answer=0
		
	def find_longest_sequence(self):
		n=self.n
		k=self.k
		arr=self.arr
		count_num=self.count_num
		answer=self.answer
		
		l=0
		for r in range(n):
			num=arr[r]
			if num not in count_num:
				count_num[num]=0
			count_num[num]+=1
			if count_num[num]>k:
				while arr[l]!=num:
					count_num[arr[l]]-=1
					l+=1
				count_num[arr[l]]-=1
				l+=1
			
			answer=max(answer,r-l+1)
			
		print(answer)
		
class Main:
	def run(self):
		n,k=map(int,input().split())
		arr=list(map(int,input().split()))
		sol=Solution(n,k,arr)
		sol.find_longest_sequence()

Main().run()
		