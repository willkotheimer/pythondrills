import requests
import re
import urllib2
from bs4 import BeautifulSoup
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print page
print page.status_code
soup = BeautifulSoup(page.content,'html.parser')


for tag in soup.find_all(re.compile("t")):
    print(tag.name)
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
print soup.find_all(["a","b"])

for tag in soup.find_all(True):
	print (tag.name)

print soup.body.string

url = "https://www.pythonforbeginners.com"
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content)
#print soup.prettify()

print soup.title.string

for link in soup.find_all('a'):
	print(link.get('href'))

print(soup.get_text())

