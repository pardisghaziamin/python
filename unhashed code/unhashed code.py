def calculate_averages(input_file_name, output_file_name):
	import statistics
	import csv
	with open(input_file_name,newline='') as f:
		reader=csv.reader(f,delimiter=',',quotechar='|')
		z=[]
		h=[]
		c={}
		for row in reader:
			name=row[0]
			z.append(name)
			these_grades=[]
			for grades in row[1:]:
				these_grades.append(float(grades))
			these_grades=statistics.mean(these_grades)
			c[name]=these_grades
			h.append(float(these_grades))
	file=open(output_file_name,'a')
	for i in h:
		for name in c:
			if c[name]==i:
				x=('%s %s'%(name,i))
				file.write(x)
				x=''
	file.close()			

def calculate_sorted_averages(input_file_name, output_file_name):
	import statistics
	import csv
	with open(input_file_name,newline='') as f:
		reader=csv.reader(f,delimiter=',',quotechar='|')
		z=[]
		h=[]
		c={}
		for row in reader:
			name=row[0]
			z.append(name)
			these_grades=[]
			for grades in row[1:]:
				these_grades.append(float(grades))
				these_grades=statistics.mean(these_grades)
				c[name]=these_grades
				h.append(float(these_grades))
	h.sort()
	h.reverse()
	file=open(output_file_name,'a')
	for i in h:
		for name in c:
			if c[name]==i:
				x=('%s %s'%(name,i))
				file.write(x+'\n')
				x=0

def calculate_three_best(input_file_name, output_file_name):
	import statistics
	import csv
	with open(input_file_name,newline='') as f:
		reader=csv.reader(f,delimiter=',',quotechar='|')
		z=[]
		h=[]
		c={}
		for row in reader:
			name=row[0]
			z.append(name)
			these_grades=[]
			for grades in row[1:]:
				these_grades.append(float(grades))
				these_grades=statistics.mean(these_grades)
				c[name]=these_grades
				h.append(float(these_grades))
	h.sort()
	h.reverse()
	file=open(output_file_name,'a')
	for i in h[0:3]:
		for name in c:
			if c[name]==i:
				x=('%s %s'%(name,i))
				file.write(x+'\n')
				x=0

def calculate_three_worst(input_file_name, output_file_name):
	import statistics
	import csv
	with open(input_file_name,newline='') as f:
		reader=csv.reader(f,delimiter=',',quotechar='|')
		z=[]
		h=[]
		c={}
		for row in reader:
			name=row[0]
			z.append(name)
			these_grades=[]
			for grades in row[1:]:
				these_grades.append(float(grades))
				these_grades=statistics.mean(these_grades)
				c[name]=these_grades
				h.append(float(these_grades))
	h.sort()
	file=open(output_file_name,'a')
	for i in h[0:3]:
		for name in c:
			if c[name]==i:
				x=('%s'%(i))
				file.write(x+'\n')
				x=0
def calculate_average_of_averages(input_file_name, output_file_name):
	import statistics
	import csv
	with open(input_file_name,newline='') as f:
		reader=csv.reader(f,delimiter=',',quotechar='|')
		h=[]
		for row in reader:
			name=row[0]
			these_grades=[]
			for grades in row[1:]:
				these_grades.append(float(grades))
				these_grades=statistics.mean(these_grades)
				h.append(float(these_grades))
	h=statistics.mean(h)
	file=open(output_file_name,'a')
	file.write('%s'%(h))

