#! /usr/bin/python

print 'Content-type: text/html'
print ''

age = 35

print age

pi = 3.14

print pi

name = "rob"

print name

print age / pi

number = "5"

print float(number) * pi

str = "My Name Is "

print str[0]
print str[0:5]
print str[5]

print str + name

myList = ["Rob", "Kirsten", "Tommy", "Ralphie"]

print myList
print myList[1]
print myList[2:4]

myTuple = (1, 2, 3, 4)

print myTuple
print myTuple[2]

myList[2] = 5

print myList

dict = {}
dict["dad"] = "Rob"
dict["mum"] = "Kirsten"
dict[1] = "Tommy"
dict[2] = "Ralphie"

print dict
print dict["mum"]

print dict.keys()
print dict.values()







