import re
import urllib2

text="There is no end to education. It is not that you read a book, pass an exam, and finish with education. The whole life, from the moment you are born to the moment you die, is the process of learning."
print re.search('is',text)
print re.match('is',text)
print re.findall('is',text)

print re.findall(r'book|life',text)
print re.findall(r'e[a-z]+',text) # without word boundary
print re.findall(r'\be[a-z]+\b',text) #with word boundary

#let us open a website and parse all the email IDs out of it. We will also
#extract all the URLs from it

site=urllib2.urlopen(r'http://www.bsnl.in/')
text = site.read()
urlstr = re.compile(r'http[s]*://[a-z|A-Z|0-9|.|/|~|?|+[.]+[a-z]+')
emails = re.compile(r'[a-z|A-Z]+[a-z|A-Z|.|_|-|0-9|*@[a-z]+.[a-z|.]+')
print set(re.findall(urlstr,text))

xml = '<xml><Customer>Jagan</Customer></xml>'
s = re.search(r'<(xml)><(.*)>(.*)</\2>',xml)
s.groups()

string='john@gmail.com,harry@yahoo.com,dean@gmail.com'
gmails = re.findall(r'[\w\.-]+@gmail[\w\.-]+',string)
for email in gmails:
	print email

#opening a file
f = open('/Users/willkotheimer/pythondrills/file1','r')
#Finding all the gmail accounts in File1
gmails = re.findall(r'[[\w\.-]+@gmail[\w\.-]+',f.read())
for email in gmails:
	print email

replacestring='john@gmail.com,harry@yahoo.com,dean@gmail.com'
#using sub to replace gmail with yahoo
re.sub('gmail','yahoo',replacestring)
print replacestring

#Using compile() to compile a python object
pattern = re.compile('abb')
#using the python object
match = pattern.search('abbreviated')
#Listing the match
print match.group()
