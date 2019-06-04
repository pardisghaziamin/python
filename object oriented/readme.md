# Object oriented


# problem:

we have a **footballer class** which inherits from a **human class**.
at the first,it is needed to create 22 footballer objects,
then allocate them to twe classes. (A and B randomly)

# solution:
## First

define a human class and also footballer name.

    class  human:
	    def  __init__(self):
		self.list=['hosein','maziar','akbar','nima','mahdi',
		'farhad','mohamad','khashayar','milad','mostafa',
		'amin','saeed','pouya','pouria','reza',
		'ali','behzad','soheil','behrooz','shahrooz',
		'saman','mohsen']

## Second

Then define a footballer class which inherits from a human class,
and define twe classes to allocate footballer to them.

> note:
> we imported **random** library to choose footballer randomly.

	class  footbaler(human):
		def  chooseA(self):
			h=0
			s=[]
			while(h<11):
				t=random.randint(0,21)
				u=0
				for i in  range(0,len(s)):
					if s[i]==t:
						u=1
					if u==0:
						h=h+1
						s.append(t)
						A.append(self.list[t])
			print('A : ')
			for i in  range(0,11):
					print(A[i])
	def  chooseB(self):
		for i in  self.list:
			c=0
			for j in A:
				if i==j:
					c=c+1
				if c==0:
					B.append(i)
		print('B : ')
		for i in  range(0,11):
			print(B[i])
 

and the output will be:

    >>A : 
	khashayar
	farhad
	pouya
	saman
	hosein
	akbar
	saeed
	milad
	shahrooz
	ali
	mohamad
	B : 
	maziar
	nima
	mahdi
	mostafa
	amin
	pouria
	reza
	behzad
	soheil
	behrooz
	mohsen
