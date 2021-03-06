html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,'html.parser')
#print(soup.prettify())
print soup.title
print soup.title.name
print soup.title.string
print soup.title.parent.name
print soup.p
print soup.p['class']
print soup.a
print soup.find_all('a')
print soup.find(id="link3")

for link in soup.find_all('a'):
	print(link.get('href'))

import urllib2
quote_page = "http://www.jackroeusa.com"
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page,'html.parser')
#print (soup.get_text())
for link in soup.find_all('a'):
	print link.get('href')

#to do: recursive search
import urllib2
quote_page = "http://www.jackroeusa.com"
def lookup(html):
	page = urllib2.urlopen(html)
	soup = BeautifulSoup(page,'html.parser')
	#print (soup.get_text())
	for link in soup.find_all('a'):
		html2 = link.get('href')
		print(html2)
		if html2!=None: 
			htmltemp = urllib2.urlopen(html2).read()
			soup2 = BeautifulSoup(htmltemp,'html.parser')
			print soup2.get_text()
			
lookup(quote_page)
