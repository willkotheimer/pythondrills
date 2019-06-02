from functools import reduce

values = [1,2,3,4]

summed = reduce(lambda a,b: a+b, values)
print(summed)

#don't use first value

values = [1,2,3,4,5]

first_value = reduce(lambda a, _: a, values)
print(first_value)

values = [1,2,3,4,5,6,7,8,9,10]
#Map
add_10 = [x+ 10 for x in values]
print(add_10)

#Filter
even = [x for x in values if x % 2 ==0]
print(even)


def add_two(b):
	return 2 + b
print(add_two(4))

from functools import partial
def add(a,b):
	return a + b

add_two = partial(add,2)
add_ten = partial(add,10)

print(add_two(4))

print(add_ten(4))


#partial that grabs IP addresses using the map function

extract_ip = partial(
	map,
	lambda x: x.split(' ')[0]
)
lines = open("examplelog.txt","r")
ip_addresses = list(extract_ip(lines))
print(ip_addresses)


#Sorting

unsorted = [('b',6),('a',10),('d',0),('c',4)]

print(sorted(unsorted, key=lambda x: x[1]))

values = [1,2,3,4,5,6,7,8,9,]

add_10 = list(map(lambda x: x + 10, values))
add_20 = list(map(lambda x: x + 20, values))

print(add_10)
print(add_20)
