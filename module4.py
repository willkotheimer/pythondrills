import re
import math
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

#5.Below is the program to calculate the area of a box. 
#Check how it is working. Correct the program (if required).

class Box:
	def __init__(self,width,height):
		self.width=width
		self.height=height
 	def area(self):
                return self.width * self.height
#create instance of box
x= Box(10,2)
#print area.
print(x.area())

#6.Write a program to calculate distance so that it takes 
#two Points (x1, y1) and (x2, y2) as arguments and displays 
#the calculated distance, using Class.

class Distance:
	def __init__(self,x1,y1,x2,y2):
		self.x1=x1
		self.y1=y1
		self.x2=x2
		self.y2=y2
	def area(self):
		a = math.pow(self.x2-self.x1,2)
		b = math.pow(self.y2-self.y1,2)
		return math.sqrt(a+b)
inst = Distance(-1,2,0,7)
print (inst.area()) 

#7.Correct the below program so that output should appear like this.
#[Expected output: x-value: 5 y-value: 7]

class Point:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def __str__(self):
		return "x-value: "+str(self.x)+" y-value: "+str(self.y)
	
	def add(self,other):
		p=Point()
		p.x=self.x+other.x
		p.y=self.y+other.y
		return p
p1 = Point(3,4)
p2 = Point(2,3)
print Point.add(p1,p2)

