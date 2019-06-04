import pyodbc
import re
cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=SORUOSHSYSTEM\DUGINSIGHT;"
                      'Database=pardis;'
                      'Trusted_Connection=yes;')
m=input()
s=re.search(r'[^\W]+\@\w+[^\d]\.\w[^\d]+$',m)
if s==None:
        e='WRONG'
else:
        if (s.span()[0]==0) & (s.span()[1]==len(m)):
                e='OK'
        else:
                e='WRONG'
print(e)
while e=='WRONG':
    print('expression@string.string')
    m=input()
    s = re.search(r'[^\W]+\@\w+[^\d]\.\w[^\d]+$', m)
    if s == None:
        e = 'WRONG'
    else:
        if (s.span()[0] == 0) & (s.span()[1] == len(m)):
            e = 'OK'
        else:
            e = 'WRONG'
print('email was correct,now enter your pass:')
k=input()
s=re.findall(r'[^\W]+\d+\w+$',k)
if s==[]:
        e='WRONG'
else:
        if s[0]==k:
                e='OK'
        else:
                e='WRONG'
while e=='WRONG':
    print('number and string both')
    k=input()
    s = re.findall(r'[^\W]+\d+\w+$', k)
    if s == []:
        e = 'WRONG'
    else:
        if s[0]==k:
            e = 'OK'
        else:
            e = 'WRONG'
mycursor = cnxn.cursor()
sql = "INSERT INTO tbl22 (username, password) VALUES (?, ?)"
val =(m, k)

mycursor.execute(sql, val)

mycursor.commit()
cnxn.close()



