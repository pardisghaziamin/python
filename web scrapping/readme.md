# Web scrapping


# problem:

extract all the courses which provided on Maktabkhooneh website.
[https://maktabkhooneh.org/plus](https://maktabkhooneh.org/plus)
then ,print all courses which have Maktabplus tag.
# solution:
## First
import libraries:
 - **request** is a HTTP python library.

		  import requests
  - **beautyfulsoup** helps us to parsing HTML documents.

		  from bs4 import BeautifulSoup
## Second

go to website,

    r=requests.get('https://maktabkhooneh.org/plus')

if it works well **r** will be:

    <Response [200]>


## Third
Now,start to extract our desired courses from website.

    soup=BeautifulSoup(r.text,'html.parser')
	u=soup.find_all('span',attrs={'id': 'name', 'style': ''})
	s=[]
	for i in u:
		g=i.text
		i=g.replace(' ','')
		k=i.replace('\n','')
		l=k.replace('\u200c','')
		s.append(l)
	m=soup.find_all('span',attrs={'id': 'org', 'style': ''})
	b=[]
	for i in m:
		g=i.text
		i=g.replace(' ','')
		k=i.replace('\n','')
		l=k.replace('\u200c','')
		b.append(l)
	x={}
	for i in  range(0,len(s)):
		x[s[i]]=b[i]
	for i in s:
		if x[i]==b[0]:
			w.append(i)
		if x[i]==b[-1]:
			q.append(i)
	print(':%s\n'%b[0])
	for i in w:
		print(i)
	print('\n\n:%s\n'%b[-1])
	for i in q:
		print(i)

