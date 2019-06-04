class human:
	def __init__(self):
		self.list=['hosein','maziar','akbar','nima','mahdi','farhad','mohamad','khashayar','milad','mostafa','amin','saeed','pouya','pouria','reza','ali','behzad','soheil','behrooz','shahrooz','saman','mohsen']
import random
A=[]
B=[]
s=[]
tp=22
h=0
class footbaler(human):
	def chooseA(self):
		h=0
		s=[]
		while(h<11):
			t=random.randint(0,21)
			u=0
			for i in range(0,len(s)):
				if s[i]==t:
					u=1
			if u==0:
				h=h+1
				s.append(t)
				A.append(self.list[t])
		print('A : ')
		for i in range(0,11):
			print(A[i])
	def chooseB(self):
		for i in self.list:
			c=0
			for j in A:
				if i==j:
					c=c+1
			if c==0:
				B.append(i)
		print('B : ')		
		for i in range(0,11):
			print(B[i])
b=footbaler()
b.chooseA()
b.chooseB()

                        
