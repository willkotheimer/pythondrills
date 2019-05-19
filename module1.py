import string
#1.Write a program to print the: 
#a.Number of lowercase "a" and "o" in the following sentence.
#b.Number of uppercase "L" and "N" in the following sentence.
sentence='Discover, Learning, with, Edureka'
print sentence.count("a")
print sentence.count("o")
print sentence.count("L")
print sentence.count("N")

#2.Write a program to remove the following from:

url='www.edureka.in'

#a.Remove all w's before and after .edureka.
print url.replace('w','')

#b.Remove all lowercase letter before and after .edureka.
print url.translate(None, string.ascii_lowercase)
#c.Remove all printable characters
filtered_string = filter(lambda x: x in string.printable, url)
print filtered_string
 

#3.Identify the type of numbers:
#a.numbers=0X7AE Hex constant
 #b.3+4j Complex number
#c.-01234 Octal Constant
#d.3.14e-24 Complex number


#//To do
#Write a program for String Formatting Operator % which should 
#include the following conversions:
#a.Character
#b.Signed decimal integer
#c.Octal integer
#d.Hexadecimal integer (UPPERcase letters)
#e.Floating point real number
#f.Exponential notation (with lowercase 'e')
print '%(char)c is char %(signdec)03d is signed dec %(oct)03o is octal %(hex)02x is hexadecimal %(float)03f is a float and %(exp)03e is an exponent .' % \
          {'char': "c", "signdec": 2, "oct":3,"hex":45,"float":52,"exp":6000}


