# SQL server

## working with regex and databases (SQL server)
# problem:

Save the email address and password was entered by user,
into the database.

> notice that it is important to email addres has general form as below:

**expression@string.string**


# solution:
## First

 - import **regex**:



 `import re`    
 

 - import **pyodbc** to connect to **SQL server**:
  
`import pyodbc`

## Second

Connect to SQL server:

    cnxn = pyodbc.connect('Driver={SQL Server};'
		'Server=SORUOSHSYSTEM\DUGINSIGHT;'
		'Database=pardis;'
		'Trusted_Connection=yes;')

> note:
> my database name is 'pardis' , also my server name is 'SORUOSHSYSTEM\DUGINSIGHT'
> you should use your own.

## Third

Then,search for correct form of email using **regex**:
for more explain go to [here](h)
    
## Forth
if email form was correct , then let user to enter pasword.
and check it by regex:

    s=re.findall(r'[^\W]+\d+\w+$',k)
## Fifth
now,excute it to SQL sever

    mycursor = cnxn.cursor()
	sql =  "INSERT INTO tbl22 (username, password) VALUES (?, ?)"
	val =(m, k)
	mycursor.execute(sql, val)
	mycursor.commit()
	cnxn.close()


> note:
> my table name is tbl22,
> you should first create your table ,then insert into it.
