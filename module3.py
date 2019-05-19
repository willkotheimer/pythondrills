from operator import itemgetter
import random
play = True
while (play):
	level = raw_input("Choose level (easy(E), intermediate(I), and hard(H): ")
	if(level!='E' or level!='I' or level!='H'): level='E'
	numberofquestions = raw_input("Please give us the number of question you want to attempt: ") 
	questiontype = raw_input("Specify the question type (multiplication:M, addition:A, subtraction:S, division:D): ")
	if(questiontype not in ['M','A','S','D']): print "Not in question"
	print level
	print numberofquestions
	print questiontype
	

	#each function takes a "level" argument (a)
	
	
	def gettworandomnumbers(level):
		
		newarr = []
		
		if(str(level) == 'E'):
			random1 = random.randrange(10,1000,10)
			random2 = random.randrange(10,1000,10)
			newarr.append(random1)
			newarr.append(random2)
			return newarr
		elif(str(level) == 'I'):
			random1 = random.randrange(5,1000,5)
                        random2 = random.randrange(5,1000,5)
			newarr.append(random1) 
                        newarr.append(random2)
                        return newarr
		elif(str(level) == 'H'):
			random1 = random.randrange(3,1000,3)
                        random2 = random.randrange(3,1000,3)
			newarr.append(random1) 
                        newarr.append(random2)
                        return newarr
		else:
			random1 = random.randrange(10,1000,10)
                        random2 = random.randrange(10,1000,10)
                        newarr.append(random1)
                        newarr.append(random2)
                        return newarr
		

	def askSubQuestion(arrayS):
		stringask = "What is "+str(arrayS[0])+" - "+str(arrayS[1])+" = ? "
		subA = raw_input(stringask)
		if(subA==""): subA=0
		if(Sub(arrayS)==int(subA)):
			print "Good job! You got it right"
			return
		else: 
                        print "Sorry the answer was: "+str(Sub(arrayS))
			return

	def askAddQuestion(arrayA):
                stringask = "What is "+str(arrayA[0])+" - "+str(arrayA[1])+" = "
                subA = raw_input(stringask)
                if(subA==""): subA=0
                if(Sub(arrayA)==int(subA)):
                        print "Good job! You got it right"
                        return
                else:
                        print "Sorry the answer was: "+str(Sub(arrayA))
                        return
	def askMultQuestion(arrayM):
                stringask =  "What is "+str(arrayM[0])+" * "+str(arrayM[1])+" = ? "
		multA = raw_input(stringask)
		if(multA==""): multA=0
		if(Mult(arrayM)==int(multA)): 
                        print "Good job! You got it right"
			return
		else: 
                        print "Sorry the answer was: "+str(Mult(arrayM))
			return
	
	def askDivQuestion(arrayD):
                stringask =  "What is "+str(arrayD[0])+" / "+str(arrayD[1])+" = ? "
                divA = raw_input(stringask)
		if(divA==""): divA=0
		if(Div(arrayD)==int(divA)): 
                        print "Good job! You got it right"
			return
		else: 
			print "Sorry the answer was: "+str(Div(arrayD))
			return

	def Mult(a):
		return a[0]*a[1]
	def Add(a):
		return a[0]+a[1]
	def Div(a):
		return a[0]/a[1]
	def Sub(a):
		return a[0]-a[1]

	def Subtract(a):
		
		askSubQuestion(gettworandomnumbers(a))
		return
		
	def Multiply(a):
		
		askMultQuestion(gettworandomnumbers(a))
		return

	def Add(a):
		askAddQuestion(gettworandomnumbers(a))
		return

	def Divide(a):
		
		askDivQuestion(gettworandomnumbers(a))
		return

	for x in range(int(numberofquestions)):
		
		if(questiontype=='M'):
            		Multiply(level)           	
            	elif(questiontype=='D'):
			Divide(level)
                elif(questiontype=='A'):
			
            		Add(level)
                elif(questiontype=='S'):
			Subtract(level)
                else:
		
            		Add(level)
                     	
	keepplaying = raw_input("Do you want to keep playing (Y/Press any other key to stop :")
	if(keepplaying!='Y'):
		play= False

#If the answer is right or wrong, appropriate messages should be printed 
#and move to next question if attempt count is not exceeded.


#The program should ask if the user wants to continue even after attempting 
#the number of questions specified and accordingly should loop or terminate.

#Sample:Choose level (easy, intermediate, and hard): easy

#Please give us the number of question you want to attempt: 3

#Specify the question type (multiplication:M, addition:A, subtraction:S, division:D):D

#What's 6 divided by 3?2
#That's right --well done
#What's 10 divided by 2? 5That's right --well done
#What's 18 divided by 3? 6That's right --well done
#Continue or exit (Continue:C, Exit: E): E

#2.Write a recursive function to compute x raised to the power of n.

def pow(x,n):
	if n==0: return 1
	else: return x*pow(x,n-1)

answer = pow(2,4)
print "2 to the 4th power: "
print answer

#3.Sort the list using lambda function mylist = [["john", 1, "a"], 
# ["larry", 0, "b"]]. Sort the list by second item 1 and 0.

mylist = [["john", 1, "a"],["larry", 0, "b"]]

print "sorting with lambda key 2:"
print sorted(mylist,key=lambda x:x[1])

#4.Sort the list using operator.itemgetter function mylist = [["john", 1, "a"],
# ["larry", 0, "b"]]. Sort the list by second item 1 and 0.

print "sorting with itemgetter key 2: "
print sorted(mylist,key=itemgetter(1))
