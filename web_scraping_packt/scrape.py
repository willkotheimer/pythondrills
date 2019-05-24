from urllib2 import urlopen
import re

def download(url, user_agent='wswp',num_retries=2,charset='utf-8'):
	print('Downloading:',url)
	request = urlopen(url)
	html = request.read()
	print(html)
	
download("http://meetup.com")
