# Unhash code


# problem:

Find out the password of each user from hashed password of them in the CSV file.


# solution:
## First

 - import **csv** to read and write CSV files:



 `import csv`    
 

 - import **hashlib** to can work with hashed code:
  
`import hashlib`

## Second

Now,define a function to build a dictionary which contains all paswords that we can have and also their hashed code.

    

> note:
    all our password are between 0000-9999.



    def  hash_password_hack(input_file_name, output_file_name):
		k={}
		for a in  range(0,10):
			for b in  range(0,10):
				for c in  range(0,10):
					for d in  range(0,10):
						string=('%s%s%s%s'%(a,b,c,d))
						string_1=string.encode('utf-8')
						hash_object=hashlib.sha256(string_1)
						hex_dig=hash_object.hexdigest()
						k[hex_dig]=string

 

## Third

Try to read from CSV file

    with  open(input_file_name,newline='') as f:
		reader=csv.reader(f,delimiter=',',quotechar='|')
    
## Forth
Then,seperate name from hashed cod.
and also find the equal password.
	 
	    for row in reader:
			name=row[0]
			password=row[1]
			str=("%s,%s"%(name,k[password]))
## Fifth
Open a text file and save them into it.

    file=open(output_file_name,'a')
	file.write(str+'\n')

