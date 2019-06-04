import re
m=input()
s=re.search(r'[^\W]+\@\w+[^\d]\.\w[^\d]+$',m)
if s==None:
        print('WRONG')
else:
        if (s.span()[0]==0) & (s.span()[1]==len(m)):
                print('OK')
        else:
                print('WRONG')
          




 
	

