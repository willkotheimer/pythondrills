
from functools import partial
from inspect import signature
#Lambda
print (lambda a,b: a+b)(3,4)

multiplication = lambda a,b: a*b
print multiplication(3,4)

authors = ['Djuna Barnes','J.R.R. Tolkein', 'William Faulkner','Henry James','D.H. Lawrence', 'Virgina Woolf','Getrude Stein']
print sorted(authors,key=len) #returns list ordered by length of author's name
print sorted(authors,key=lambda name:name.split()[-1]) #returns list ordered by last name

val = [1,2,3,4,5,6,7,8]
#Multiply every item by two
print list(map(lambda x: x* 2, val))
#Get the factorial by multiplying the value so far to the next item
print reduce(lambda x, y: x+y, val,1)

#args
def myFun(arg1,*argv):
	print("First argument :", arg1)
	for arg in argv:
		print("Next argument through *argv :",arg)

myFun('Hello','Welcome','to','Geeks for Geeks')


#Kwargs

def myFun(ar1, **kwargs):
	for key,value in kwargs.items():
		print ("%s == %s" %(key,value))
myFun("Hi", first="Greeks", mid="for", last="Geeks")

#currying

def compose(g,f):
	def h(x):
		return g(f(x))
	return h

def celsious2fahrenheit(t):
	return 1.8 * t + 32
def readjust(t):
	return 0.9 * t - 0.5
convert = compose(readjust,celsious2fahrenheit)
print convert(10), celsious2fahrenheit(10)		
