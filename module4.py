import re
#1.Write a Regular Expression that will match a date that 
#follows the following standard "YYYY-MM-DD".
mydates = '2018-03-21 2019-01-01 01-01-2019'
dates = re.findall(r'\d{4}-\d{1,2}-\d{1,2}',mydates)
print dates

#2.Write a Regular Expression that will match a traditional SSN.
mysocials = '444-44-3232 4324-434-4324 011-11-2324'
socials = re.findall(r'\d{3}-\d{1,2}-\d{1,4}',mysocials)
print socials

#3.Write a Regular Expression that will match an IPv4 address.
ipv4s = '127.0.0.1 192.168.10.180 3.4.3.4.5'
ipv4patternmatch = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',ipv4s)
print ipv4patternmatch

#4.Write a Regular Expression that will match an email address.
emails = 'will@gmail.com and some other emails hello@gmail, hello@, and whataboutme@yahoo.com'
emailpatternmatch = re.findall(r'\b[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]{2,}\b',emails)
print emailpatternmatch 

