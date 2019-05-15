from string import ascii_lowercase

total = raw_input('What is the total amount for your online shopping?')
country = raw_input('Shipping within the US or Canada?')
if country == "US":
	if total <= "50":
		print "Shipping Costs $6.00"
	elif total <= "100":
		print "Shipping Costs $9.00"
	elif total <= "150":
		print "Shipping Costs $12.00"
	else:print "FREE"
if country == "Canada":
	if total <= "50":
		print "Shipping Costs $8.00"
	elif total <="100":
		print "Shipping Costs $12.00"
	elif total <= "150":
		print "Shipping Costs $15.00"
	else:
		print "FREE"

#Program that prompts a user for name then welcomes them:


name = raw_input('What is your name?')
print "Welcome "+name

#Program that converts fahrenheit to celsius

far = raw_input('Name a fahrenheit temperature: ')
cel = (int(far)-32)/1.8
print cel

#Write a program to prompt the user for hours and rate per hour to compute 
#gross pay.

hours = raw_input('Enter Hours: ')
rate = raw_input('Enter Rate: ')
pay = (int(hours))*(int(rate))
print 'Pay: '+str(pay)

#Write a for loop that prints all elements of a list and their position in the list

a = [4,7,3,2,5,9]
pos = 0
for i in a:
	print str(i)+":"+str(pos)
        pos+=1

#Write a program that creates a dictionary of key:values a:1 z:26

dict= {}
num=1
for i in ascii_lowercase:
	dict [i]=num
	num+=1
print dict

#Write a program to reverse/inverse key:value like below.

dict1 = { 'a': 1, 'b':2 }
dict2= {}
for key,val in dict1.items():
	dict2[val]=key
print dict2

#Using given list L = ['a', 'b', 'c', 'd'] create a dictionary of key:values, use enumerate function

L = ['a', 'b', 'c', 'd']
obj1 = enumerate(L)
print list(enumerate(L,1))

