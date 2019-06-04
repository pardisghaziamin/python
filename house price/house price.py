import requests
from bs4 import BeautifulSoup
from sklearn import tree
import re
x1=input('input tedad rooms:')
x2=input('input  area:')
print('it maybe takes a time,thanks for waiting:)')
g=[]
m=[]
o=[]
for i in range(1,200):
	q='https://www.ihome.ir/خرید-فروش/آپارتمان/تهران/'
	q=q+ str(i)
	pp=requests.get(q)
	soup=BeautifulSoup(pp.text,'html.parser')
	p=soup.find_all('div',attrs={'class': ['price']})
	for i in range(1,len(p)):
		j=p[i].text
		y=re.sub(r'\s+','',j)
		h=y.replace('تومان','')
		f=h.replace('اطلاعازقیمت','0')#price
		g.append(f)
	d=soup.find_all('ul',attrs={'class': ['left slider_pinfo']})	
	for i in d:
		f=i.text
		b=re.sub(r'\s+','',f)
		j=b.replace('خواب','.')#room(feature1)
		w=j.replace('مترمربعمتراژ','t')#area(feature2)
		a=w.replace('سنبنا','a')#age of building(feature3)
		if a.find('.')!= -1:
			s=a.find('.')
			o.append(a[0:s])
			if a.find('a')==-1:
				if a.find('t')==-1:
					m.append('0')
				else:
					m.append(a[s+1:(len(w)-1)])
			if a.find('a')!= -1:
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
			if a.find('a')!= -1:
				if a.find('t')==-1:
					m.append('0')
				else:
					q=a.find('t')
					m.append(a[0:q])
	
s=[]
j=[]
y=[]
for i in range(0,len(g)):
	if (m[i]!='0')|(o[i]!='0')|(g[i]!='0'):#remove the deficient data
		s.append(int(o[i]))
		k=m[i].replace(',','')	 
		s.append(int(k))
		j.append(s)
		s=[]
		l=g[i].replace(',','')	 
		y.append(int(l))	

clf=tree.DecisionTreeRegressor()
clf=clf.fit(j,y)
newdata=[[int(x1),int(x2)]]
answer=clf.predict(newdata)
print('price:%s'%(int(answer)))
                                                                                                                                                                                                                                                                                                                                 