# House price 


# problem:

Create a dataset of house price
you can use [ihome.ir](ihome.ir).

> note:
> ihome.ir is online house marketing. 

then use **scikit-learn** to to predict a house price via number of rooms and area.
# solution:
## First
import libraries:
 - **request** is a HTTP python library.

		  import requests
 - **beautyfulsoup** helps us to parsing HTML documents.

		  from bs4 import BeautifulSoup
		  

 - we import **regex** to use regex.
 

	    import re
	    

 - **scikit-learn** is a machine learning library that help us to solve our problem using **logistic regression**.

	    from sklearn import tree

## Second

Build a dataset,

   then on each 200 first page of the website,extract the room number of each house and likewise area and price of it.
and build a dataset which contains around 2500 houses.
 
    for i in  range(1,200):
		q='https://www.ihome.ir/????-????/????????/?????/'
		q=q+  str(i)
		pp=requests.get(q)
		soup=BeautifulSoup(pp.text,'html.parser')
		p=soup.find_all('div',attrs={'class': ['price']})
		for i in  range(1,len(p)):
			j=p[i].text
			y=re.sub(r'\s+','',j)
			h=y.replace('?????','')
			f=h.replace('???????????','0')#price
			g.append(f)
		d=soup.find_all('ul',attrs={'class': ['left 	slider_pinfo']})
		for i in d:
			f=i.text
			b=re.sub(r'\s+','',f)
			j=b.replace('????','.')#room(feature1)
			w=j.replace('????????????','t')#area(feature2)
			a=w.replace('?????','a')#age of building(feature3)
			if a.find('.')!=  -1:
				s=a.find('.')
				o.append(a[0:s])
				if a.find('a')==-1:
					if a.find('t')==-1:
						m.append('0')
					else:
						m.append(a[s+1:(len(w)-1)])
				if a.find('a')!=  -1:
					if a.find('t')==-1:
						m.append('0')
					else:
						q=a.find('t')
						m.append(a[s+1:q])
			if a.find('.')==-1:
				o.append('0')
				if a.find('a')==-1:
					if a.find('t')==-1:
						m.append('0')
					else:
						q=a.find('t')
						m.append(a[0:q])
				if a.find('a')!=  -1:
					if a.find('t')==-1:
						m.append('0')
					else:
						q=a.find('t')
						m.append(a[0:q])


## Third
Now,try to remove deficient data from our dataset.

> for example:if any of them doesnt have price or rooms number.
 

    for i in  range(0,len(g)):
		if (m[i]!='0')|(o[i]!='0')|(g[i]!='0'):#remove the deficient data
			s.append(int(o[i]))
			k=m[i].replace(',','')
			s.append(int(k))
			j.append(s)
			s=[]
			l=g[i].replace(',','')
			y.append(int(l))
## Forth
use **machine learning** for fitting.

    clf=tree.DecisionTreeRegressor()
	clf=clf.fit(j,y)
and predict the house price via rooms number and area which was entered.

    newdata=[[int(x1),int(x2)]]
	answer=clf.predict(newdata)
	print('price:%s'%(int(answer)))
